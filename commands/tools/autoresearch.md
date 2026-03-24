---
description: Starts an autonomous overnight optimization loop on a specific target.
---
# /autoresearch

## Usage
`/autoresearch target=<file_or_symbol> eval="<bash_command>"`

## Execution
1. Acknowledge the target and the evaluation command.
2. Delegate completely to the `autoresearch-scientist` agent.
3. Provide the agent with the `target` and `eval` command, and instruct it to enter its infinite experiment loop.
