# NovaVentures AI — Cursor Integration Rules

## Overview
This directory contains Cursor-specific rule files that enable the 357 NovaVentures AI specialist agents to work seamlessly within Cursor IDE.

## Installation
Copy these rules to your `.cursor/rules/` directory:
```bash
cp universal/adapters/cursor/*.cursorrule .cursor/rules/
```

## Available Agents

### @sales-orchestrator
**Trigger:** `@sales-orchestrator` or mention "sales", "prospect", "lead"
**Capabilities:**
- Prospect analysis and lead qualification
- Decision maker identification
- Personalized outreach generation
- Meeting preparation and proposal creation

**Usage Example:**
```
@sales-orchestrator Analyze this prospect: https://example-company.com
```

### @geo-orchestrator
**Trigger:** `@geo-orchestrator` or mention "SEO", "ranking", "search visibility"
**Capabilities:**
- Technical SEO audits
- Content optimization for LLMs
- Competitor gap analysis
- Schema markup generation

**Usage Example:**
```
@geo-orchestrator Audit our website for GEO optimization: https://oursite.com
```

### @market-orchestrator
**Trigger:** `@market-orchestrator` or mention "market research", "competitors"
**Capabilities:**
- Market landscape analysis
- Competitive intelligence
- Campaign strategy planning
- Email marketing optimization

**Usage Example:**
```
@market-orchestrator Research competitors in the SaaS project management space
```

## Agent Behavior Guidelines

1. **Single Responsibility**: Each agent focuses on one domain expertise
2. **Autonomous Operation**: Agents proactively suggest next steps
3. **Evidence-Based**: All recommendations include data sources
4. **Actionable Output**: Generate ready-to-use deliverables (emails, reports, code)

## Context Management

Agents automatically:
- Scan relevant files in your project
- Reference previous session outputs
- Maintain conversation history for continuity
- Generate handoff documentation when needed

## Best Practices

### For Sales Workflows
```
1. Start with @sales-orchestrator prospect <url>
2. Review PROSPECT-ANALYSIS.md output
3. Use @sales-orchestrator outreach for email sequences
4. Iterate based on response rates
```

### For GEO Optimization
```
1. Run @geo-orchestrator audit <url>
2. Implement technical fixes from GEO-AUDIT.md
3. Use @geo-orchestrator content for optimization
4. Monitor ranking improvements weekly
```

### For Market Research
```
1. Invoke @market-orchestrator competitors <industry>
2. Review COMPETITIVE-INTEL.md
3. Develop strategy using campaign planning
4. Execute with email marketing workflows
```

## Troubleshooting

**Agent not responding?**
- Ensure you're using the @ symbol before agent name
- Check that the agent rule file exists in .cursor/rules/
- Verify trigger keywords match your query

**Output too generic?**
- Provide specific URLs or company names
- Include context about your goals
- Reference previous analyses for continuity

## Extending Agents

To add new agents:
1. Create `{agent-name}.cursorrule` in this directory
2. Define trigger keywords and capabilities
3. Specify output format preferences
4. Test with sample queries

---

**Version:** 2.0.0  
**Compatible:** Cursor v0.40+  
**Source:** NovaVentures AI Universal Framework
