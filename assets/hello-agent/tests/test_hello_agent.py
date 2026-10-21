"""Integration test for the Hello Agent greeting capability."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# Ensure app/ is on the path
APP_DIR = Path(__file__).parent.parent / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


@pytest.fixture
def mock_llm_response():
    """Return a canned LLM hello response."""
    msg = MagicMock()
    msg.content = "Hello! Welcome! How can I assist you today?"
    return msg


@pytest.fixture
def mock_chain(mock_llm_response):
    """Mock the LangGraph graph invocation to return a canned response."""
    result = {"messages": [mock_llm_response]}

    graph_mock = MagicMock()
    graph_mock.ainvoke = AsyncMock(return_value=result)
    return graph_mock


@pytest.mark.asyncio
async def test_invoke_returns_greeting(mock_chain):
    """Agent invoke() returns a response that contains a greeting."""
    with (
        patch("agent.create_agent", return_value=mock_chain),
        patch("agent.create_checkpointer", return_value=None),
        patch("agent.ChatLiteLLM"),
        patch("agent.SummarizationMiddleware"),
        patch("mcp_providers.agw.get_user_sub", return_value="test-user"),
    ):
        from agent import SampleAgent

        agent = SampleAgent()
        response = await agent.invoke(
            query="Hello!",
            context_id="test-context-001",
            tools=[],
        )

    assert response.status == "completed"
    assert "hello" in response.message.lower() or "welcome" in response.message.lower()


@pytest.mark.asyncio
async def test_stream_yields_greeting(mock_chain):
    """Agent stream() yields a completed status with a greeting message."""
    with (
        patch("agent.create_agent", return_value=mock_chain),
        patch("agent.create_checkpointer", return_value=None),
        patch("agent.ChatLiteLLM"),
        patch("agent.SummarizationMiddleware"),
        patch("mcp_providers.agw.get_user_sub", return_value="test-user"),
    ):
        from agent import SampleAgent

        agent = SampleAgent()
        chunks = []
        async for chunk in agent.stream(
            query="Say hello to Alice",
            context_id="test-context-002",
            tools=[],
        ):
            chunks.append(chunk)

    # Last chunk should be completed
    final = chunks[-1]
    assert final["is_task_complete"] is True
    assert final["require_user_input"] is False
    assert len(final["content"]) > 0


@pytest.mark.asyncio
async def test_invoke_handles_error_gracefully():
    """Agent invoke() returns error status gracefully when LLM fails."""
    graph_mock = MagicMock()
    graph_mock.ainvoke = AsyncMock(side_effect=RuntimeError("LLM unavailable"))

    with (
        patch("agent.create_agent", return_value=graph_mock),
        patch("agent.create_checkpointer", return_value=None),
        patch("agent.ChatLiteLLM"),
        patch("agent.SummarizationMiddleware"),
        patch("mcp_providers.agw.get_user_sub", return_value="test-user"),
    ):
        from agent import SampleAgent

        agent = SampleAgent()
        response = await agent.invoke(
            query="Hello",
            context_id="test-context-003",
            tools=[],
        )

    # Should still return completed (error message) rather than raise
    assert response.status in ("completed", "error")
    assert response.message is not None
