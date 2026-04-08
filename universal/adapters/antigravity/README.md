# NovaVentures AI - Antigravity Workflow Definitions

## Overview
This directory contains YAML workflow definitions for running NovaVentures AI agents in Antigravity and other workflow-based AI environments.

## Installation
```bash
# Copy workflows to your Antigravity workflows directory
cp universal/adapters/antigravity/*.yaml ~/antigravity/workflows/

# Or link them
ln -s $(pwd)/universal/adapters/antigravity/*.yaml ~/antigravity/workflows/
```

## Available Workflows

### 1. Sales Prospect Analysis (`sales-prospect-analysis.yaml`)
**Purpose:** Comprehensive prospect research and scoring  
**Input:** Company URL or name  
**Output:** PROSPECT-ANALYSIS.md with score and recommendations  
**Usage:** `ag run sales-prospect-analysis --input https://example.com`

### 2. GEO Audit (`geo-audit.yaml`)
**Purpose:** Technical SEO and generative engine optimization audit  
**Input:** Website URL  
**Output:** GEO-AUDIT.md with fixes and optimization plan  
**Usage:** `ag run geo-audit --input https://oursite.com`

### 3. Market Intelligence (`market-research.yaml`)
**Purpose:** Competitive landscape analysis and market sizing  
**Input:** Industry description and competitor list  
**Output:** COMPETITIVE-INTEL.md with strategic recommendations  
**Usage:** `ag run market-research --industry "SaaS project management"`

### 4. Autonomous Optimization Loop (`auto-optimize.yaml`)
**Purpose:** Continuous improvement through benchmark-driven iterations  
**Input:** Target metric and baseline  
**Output:** Iterative improvements with before/after comparisons  
**Usage:** `ag run auto-optimize --metric "page_load_time" --target "2s"`

### 5. Session Handoff (`session-handoff.yaml`)
**Purpose:** Create comprehensive session documentation for team continuity  
**Input:** Session context and key decisions  
**Output:** HANDOFF.md with context, decisions, and next steps  
**Usage:** `ag run session-handoff --context "Q4 planning session"`

## Workflow Structure

Each YAML workflow follows this schema:

```yaml
name: workflow-name
version: "2.0.0"
description: Clear purpose statement
category: sales|geo|market|security|devops

inputs:
  - name: input_name
    type: string|url|file|list
    required: true|false
    description: What this input is for

outputs:
  - filename: OUTPUT.md
    format: markdown|json|yaml
    description: What gets generated

steps:
  - id: step_1
    agent: agent-name
    action: specific_action
    input_from: previous_step_or_input
    output_to: intermediate_result
    
  - id: step_2
    agent: another-agent
    action: another_action
    parallel: true|false
    depends_on: [step_1]

quality_gates:
  - check: validation_type
    threshold: minimum_score
    action_on_fail: retry|abort|manual_review

metadata:
  estimated_duration: "5-10 minutes"
  token_budget: 50000
  priority: high|medium|low
```

## Running Workflows

### Basic Execution
```bash
ag run <workflow-name> --input <value>
```

### With Multiple Inputs
```bash
ag run sales-prospect-analysis \
  --company_url "https://example.com" \
  --target_role "VP Marketing" \
  --output_format "markdown"
```

### Dry Run (Preview)
```bash
ag run geo-audit --input https://oursite.com --dry-run
```

### With Custom Configuration
```bash
ag run market-research \
  --config custom-config.yaml \
  --industry "fintech" \
  --competitors "stripe,square,adyen"
```

## Parallel Execution

Workflows support parallel agent execution for faster results:

```yaml
steps:
  - id: research_phase
    parallel: true
    agents:
      - agent: company-research
        action: analyze_firmographics
      - agent: contact-mapping
        action: identify_decision_makers
      - agent: tech-stack-analysis
        action: enumerate_tools
    join_at: synthesis_step
  
  - id: synthesis_step
    agent: orchestrator
    action: synthesize_findings
    depends_on: [research_phase]
```

## Integration with Other Tools

### MCP (Model Context Protocol)
Workflows can call MCP servers for enhanced capabilities:

```yaml
mcp_servers:
  - name: filesystem
    capabilities: [read, write, search]
  - name: browser
    capabilities: [navigate, screenshot, extract]
  - name: database
    capabilities: [query, insert, update]
```

### Webhook Notifications
Send results to external systems:

```yaml
notifications:
  on_complete:
    webhook: https://your-server.com/webhook
    method: POST
    payload:
      workflow: "{{workflow_name}}"
      status: "{{status}}"
      output_file: "{{output_filename}}"
```

## Error Handling

Workflows include automatic retry and fallback logic:

```yaml
error_handling:
  max_retries: 3
  retry_delay: "30s"
  fallback_agent: human-review
  abort_conditions:
    - quality_score < 0.6
    - token_limit_exceeded
    - critical_validation_failed
```

## Monitoring & Logging

Track workflow execution:

```bash
# View running workflows
ag workflows list

# Check status of specific run
ag workflows status <run-id>

# View logs
ag workflows logs <run-id>

# Cancel running workflow
ag workflows cancel <run-id>
```

## Creating Custom Workflows

1. Copy an existing workflow as template
2. Modify inputs, steps, and outputs
3. Test with `--dry-run` flag
4. Validate with sample data
5. Deploy to production workflows directory

Example template:
```yaml
name: my-custom-workflow
version: "1.0.0"
description: My custom automation

inputs:
  - name: target
    type: string
    required: true
    description: The target to analyze

outputs:
  - filename: CUSTOM-OUTPUT.md
    format: markdown
    description: Custom analysis results

steps:
  - id: analyze
    agent: specialist-agent
    action: perform_analysis
    input_from: target
    
  - id: report
    agent: reporter-agent
    action: generate_report
    depends_on: [analyze]

quality_gates:
  - check: completeness
    threshold: 0.8
```

---

**Version:** 2.0.0  
**Compatible:** Antigravity v1.0+, Workflow-based AI systems  
**Framework:** NovaVentures AI Universal
