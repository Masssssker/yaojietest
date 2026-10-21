# Hello Agent

Simple demo AI agent that greets users.

## Business Challenge

Build a minimal demonstration agent that responds with a hello greeting to verify the agent framework is set up and working correctly.

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Agent framework readiness | Not deployed | Agent deployed and responding | Immediately | IT / Platform Validation | user |

## Key Milestones

1. **Agent initialized** — Agent project is bootstrapped and running locally.
2. **Greeting capability active** — Agent responds with a hello message to any user input.
3. **Agent deployed** — Agent is deployed and accessible on SAP BTP.

## Business Architecture (RBA)

### End-to-End Process

Governance & IT Management

### Process Hierarchy

```
Corporate
└── Governance
    └── IT Management
        └── Platform Enablement
            └── Agent Framework Validation
```

### Summary

This is a simple demo/test agent to validate the agent development framework on SAP BTP. No core business process is targeted.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Webhook API ORD ID | Data Product ORD ID | Gap? | Notes / assumptions |
|------------------------|------------------------|------------|-------------------|-------------------|-------------------|-------------------|------|---------------------|
| Greet users via agent | None — custom agent build | — | — | — | — | — | Yes | Simple demo; no SAP API integration needed |

### Key findings

- No standard SAP product covers a hello-world greeting agent; custom build is required.
- No MCP server or API integration is needed for this minimal demo.
- The solution serves as a baseline to validate the A2A agent framework on SAP BTP.

## Recommendations

### Hello Agent — Demo AI Agent

#### Executive Summary

Minimal Python A2A agent that greets users to validate the framework.

#### Recommended Solution

Build a lightweight Python-based A2A protocol agent on SAP BTP that responds to any user message with a greeting. This serves as a platform readiness check and starting point for more complex agent development.

#### Recommended solution category

AI Agent

#### Intent fit
95%
