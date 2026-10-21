# Runtime Skills Guidelines

Runtime skills are task-specific instructions and resources that live alongside your agent code. They enable complex workflows without bloating the system prompt.

For universal agent patterns, see [guidelines-agent.md](./guidelines-agent.md).

## When to Create Runtime Skills

**Create a runtime skill when ANY of these apply:**

| Scenario | Example |
|----------|---------|
| Complex multi-step workflows | Approval processes with escalation paths |
| Domain-specific knowledge | Industry compliance rules, regulatory constraints |
| Task-specific instructions | Report formatting, data validation rules |
| Reference material needed | Templates, lookup tables, example payloads |

**Skip runtime skills when:**
- Instructions are simple enough for the system prompt
- The task is a one-liner with no branching logic
- No reference material is needed
