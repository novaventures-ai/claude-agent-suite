---
description: Route any task to the best specialist agent(s) automatically
---

Act as the Master Orchestrator. Read the agent registry at ~/.claude/agents/AGENT_REGISTRY.md to understand all available agents.

Analyze the following task, select the best agent(s), and execute:

$ARGUMENTS

Follow this process:
1. **Analyze** — Break down the task into domains and sub-tasks
2. **Route** — Search the registry and pick the best agent(s) for each sub-task
3. **Announce** — Tell me which agents you selected and why
4. **Execute** — Launch the agents (parallel when independent, sequential when dependent)
5. **Synthesize** — Combine all outputs into one unified deliverable

If the task spans multiple domains, coordinate a multi-agent pipeline. If it's a single domain, pick the single best specialist and delegate fully.
