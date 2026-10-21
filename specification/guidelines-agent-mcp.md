# MCP Tool Integration Guidelines

Universal patterns for MCP (Model Context Protocol) tool integration in agents.

## Core Principle

**NEVER call SAP APIs directly.** All API consumption MUST go through MCP servers.

## MCP Server Dependencies in asset.yaml

For **every** MCP server the agent uses, add a corresponding entry to the agent's `asset.yaml`:

```yaml
requires:
  - name: <mcp-server-name>
    kind: mcp-server
    ordId: <ord-id>
    version: <version>  # optional
```

## Skip Conditions for MCP

Skip MCP wiring entirely if:
- The agent has no SAP API integrations
- The spec has only Data Product ORD IDs in `## Data Dependencies`
