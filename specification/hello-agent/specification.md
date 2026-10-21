# Specification: hello-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md`, `intent.md`)
- [x] Bootstrap agent code in `assets/hello-agent/` using instructions from the sap-agent-bootstrap section. (invoke from inside `assets/hello-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

No runtime skills needed — the greeting task is a simple one-liner that belongs in the system prompt.

---

## Project-Specific Tasks

## Hello Greeting Feature

- [x] Open `assets/hello-agent/app/agent.py` and update the `@prompt_section` / `get_system_prompt()` body to include: "You are a friendly greeting agent. Respond to every message with a warm hello greeting, addressing the user by name if they provided one, or with a general friendly greeting otherwise."
- [x] Ensure the agent processes any incoming message and returns a greeting response (no tools needed — pure LLM response)
- [x] Verify the agent responds with a hello greeting to a test message

---

## Business Instrumentation

- [x] Implement business step instrumentation for each milestone from the PRD:
  - **M1** (Agent Initialized): emit `M1.achieved: agent initialized and ready to accept messages` on startup; `M1.missed: agent failed to initialize` on failure
  - **M2** (Greeting Active): emit `M2.achieved: greeting response delivered to user` after sending a greeting; `M2.missed: greeting response was not delivered` on error
  - **M3** (Agent Deployed): emit `M3.achieved: agent deployed and accessible on SAP BTP` at deployment readiness; `M3.missed: agent deployment did not complete successfully` on failure
  - Use pattern `[MILESTONE_ID].[achieved|missed]: [description]` for all log statements
  - Add OpenTelemetry custom spans for M1 and M2 using the decorator or context-manager form (never inside an async generator)
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

No SAP API integrations required for this agent — skip all MCP tool integration tasks.

---

## Testing

- [x] Install test dependencies: `pip install -r requirements-test.txt` (from `assets/hello-agent/`)
- [x] Write one integration test in `assets/hello-agent/tests/` that:
  - Calls the agent's `invoke` function with a sample greeting request
  - Mocks the LLM (ChatLiteLLM) to return a canned hello response
  - Asserts the response contains a greeting
- [x] Run `pytest` from `assets/hello-agent/` (no args)
- [x] If coverage < 70%, add additional tests and re-run
- [x] Run `pytest` again from `assets/hello-agent/` (no args) to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/hello-agent/`
