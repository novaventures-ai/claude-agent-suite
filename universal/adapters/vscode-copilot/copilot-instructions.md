# GitHub Copilot Instructions for NovaVentures AI

## Overview
This file configures GitHub Copilot to utilize the 357 NovaVentures AI specialist agents.

## Available Agents

### `/sales` - AI Sales Team Orchestrator
**Triggers:** sales, prospect, lead, outreach, proposal
**Use for:** prospect analysis, lead qualification, decision maker identification
**Example:** `/sales Analyze [input]`

### `/geo` - GEO Optimization Engine
**Triggers:** geo, seo, search, ranking, visibility
**Use for:** technical audit, content optimization, competitor analysis
**Example:** `/geo Analyze [input]`

### `/market` - Market Intelligence Hub
**Triggers:** market, competitor, audit, launch, email
**Use for:** market audit, competitor analysis, campaign planning
**Example:** `/market Analyze [input]`


## Best Practices

1. **Be Specific**: Include URLs, company names, or code context
2. **Reference Files**: Mention relevant files in your project
3. **Iterate**: Refine prompts based on initial outputs
4. **Save Outputs**: Important analyses should be saved to markdown files

## Workflow Examples

### Sales Intelligence
```
1. Ask: "/sales Analyze this prospect: https://example.com"
2. Review PROSPECT-ANALYSIS.md
3. Request: "/sales Create outreach sequence"
4. Customize and send
```

### GEO Optimization
```
1. Ask: "/geo Audit our website: https://oursite.com"
2. Implement fixes from GEO-AUDIT.md
3. Request: "/geo Optimize content for LLMs"
4. Monitor improvements
```

---
**Version:** 2.0.0
**Generated:** 2026-04-08T13:13:08.374582
**Framework:** NovaVentures AI Universal
