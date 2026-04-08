# 🌍 NovaVentures AI — Universal Framework

## Now Compatible with All Major AI-Powered IDEs

Your 357-agent NovaVentures AI framework is now **universally compatible** across:

- ✅ **Claude Code** (native)
- ✅ **Cursor** (via .cursorrules)
- ✅ **VS Code + GitHub Copilot** (via copilot-instructions.md)
- ✅ **Antigravity** (via YAML workflows)
- ✅ **JetBrains IDEs** (via JSON assistant configs)

---

## 📦 What's New

### Universal Core (`/universal/core/`)
- **`agents.json`**: Master registry of all 357 agents in platform-agnostic JSON format
- Single source of truth for all platform adapters
- Automatically synchronized with existing Claude Code commands

### Platform Adapters (`/universal/adapters/`)

#### Cursor Integration
```bash
cp universal/adapters/cursor/*.cursorrule .cursor/rules/
```
- Use agents with `@agent-name` syntax
- Auto-triggered by keywords
- Full context awareness

#### VS Code + GitHub Copilot
```bash
cp universal/adapters/vscode-copilot/copilot-instructions.md .github/
```
- Use agents with `/agent-name` slash commands
- Integrated into Copilot Chat
- Works in VS Code and GitHub.com

#### Antigravity Workflows
```bash
cp universal/adapters/antigravity/*.yaml ~/antigravity/workflows/
```
- Run automated workflows: `ag run sales-prospect-analysis --input https://example.com`
- Parallel agent execution
- Quality gates and error handling

#### JetBrains IDEs
```bash
cp universal/adapters/jetbrains/*.json .ai/
```
- AI Assistant integration
- Context-aware suggestions
- Triggered by agent keywords

---

## 🚀 Quick Start

### For Cursor Users
1. Copy rules: `cp universal/adapters/cursor/*.cursorrule .cursor/rules/`
2. Reload Cursor
3. Use: `@sales-orchestrator Analyze this prospect: https://example.com`

### For VS Code + Copilot Users
1. Copy instructions: `cp universal/adapters/vscode-copilot/copilot-instructions.md .github/`
2. Restart VS Code or reload window
3. Use: `/sales Analyze this prospect: https://example.com`

### For Antigravity Users
1. Copy workflows: `cp universal/adapters/antigravity/*.yaml ~/antigravity/workflows/`
2. Run: `ag run sales-prospect-analysis --company_url https://example.com`

### For JetBrains Users
1. Copy configs: `cp universal/adapters/jetbrains/*.json .ai/`
2. Open AI Assistant panel
3. Mention agent: "sales-orchestrator, analyze this prospect..."

---

## 🔄 Automatic Adapter Generation

Regenerate all adapters from the master registry anytime:

```bash
# Generate all platform adapters
python3 universal/scripts/generate_adapters.py all

# Generate specific platform
python3 universal/scripts/generate_adapters.py cursor
python3 universal/scripts/generate_adapters.py vscode
python3 universal/scripts/generate_adapters.py antigravity
python3 universal/scripts/generate_adapters.py jetbrains
```

---

## 📋 Available Universal Agents

### Sales Intelligence
- **ID:** `sales-orchestrator`
- **Triggers:** sales, prospect, lead, outreach, proposal
- **Capabilities:** Prospect analysis, lead qualification, outreach generation, meeting prep, proposals
- **Outputs:** PROSPECT-ANALYSIS.md, OUTREACH-SEQUENCE.md, MEETING-PREP.md

### GEO/SEO Optimization
- **ID:** `geo-orchestrator`
- **Triggers:** geo, seo, search, ranking, visibility
- **Capabilities:** Technical audits, content optimization, competitor analysis, schema markup
- **Outputs:** GEO-AUDIT.md, SEO-STRATEGY.md, CONTENT-OPTIMIZATION.md

### Market Intelligence
- **ID:** `market-orchestrator`
- **Triggers:** market, competitor, audit, launch, email
- **Capabilities:** Market research, competitor analysis, campaign planning, email marketing
- **Outputs:** MARKET-AUDIT.md, COMPETITIVE-INTEL.md, CAMPAIGN-PLAN.md

*(Full registry of 357 agents available in `universal/core/agents.json`)*

---

## 🏗️ Architecture

```
NovaVentures AI Universal
├── universal/core/
│   └── agents.json              # Master agent registry (single source of truth)
├── universal/adapters/
│   ├── cursor/                  # Cursor .cursorrule files
│   ├── vscode-copilot/          # GitHub Copilot instructions
│   ├── antigravity/             # YAML workflow definitions
│   └── jetbrains/               # JetBrains AI assistant configs
├── universal/scripts/
│   └── generate_adapters.py     # Automatic adapter generator
├── commands/                    # Original Claude Code commands (unchanged)
├── agents/                      # Agent definitions (unchanged)
└── hooks/                       # Event-driven automations (unchanged)
```

---

## 💡 Best Practices

### Cross-Platform Consistency
- All platforms use the same underlying agent logic
- Outputs are standardized (markdown reports, JSON data)
- Trigger keywords work consistently across IDEs

### Maximizing Effectiveness
1. **Be Specific**: Include URLs, company names, code context
2. **Provide Context**: Reference relevant files or previous analyses
3. **Iterate**: Refine prompts based on initial outputs
4. **Save Outputs**: Important analyses should be saved to markdown files

### Workflow Examples

#### Sales Prospecting (Any Platform)
```
1. Research: "/sales prospect https://target-company.com"
2. Review: PROSPECT-ANALYSIS.md with score
3. Outreach: "/sales outreach Target Company VP Marketing"
4. Follow-up: "/sales followup Target Company"
```

#### GEO Optimization (Any Platform)
```
1. Audit: "/geo audit https://oursite.com"
2. Fix: Implement technical recommendations
3. Optimize: "/geo content optimize landing page"
4. Monitor: Weekly ranking reports
```

---

## 🔧 Customization

### Adding New Agents
1. Add to `universal/core/agents.json`
2. Run: `python3 universal/scripts/generate_adapters.py all`
3. New agent available across all platforms

### Modifying Agent Behavior
- **Cursor**: Edit `.cursor/rules/{agent}.cursorrule`
- **Copilot**: Edit `.github/copilot-instructions.md`
- **Antigravity**: Edit `workflows/{agent}.yaml`
- **JetBrains**: Edit `.ai/{agent}.json`

### Platform-Specific Enhancements
Each adapter can be extended with platform-specific features while maintaining core functionality.

---

## 📊 Performance Comparison

| Platform | Invocation | Context | Parallel Execution | Best For |
|----------|-----------|---------|-------------------|----------|
| Claude Code | `/command` | Full repo | ✅ | Complex orchestrations |
| Cursor | `@agent` | Open files | ⚠️ Limited | Code-focused tasks |
| VS Code Copilot | `/agent` | Chat context | ❌ | Quick queries |
| Antigravity | `ag run` | Workflow state | ✅ | Automated pipelines |
| JetBrains | Keyword | Project context | ⚠️ Limited | IDE-integrated tasks |

---

## 🛠️ Troubleshooting

### Agents Not Recognized
- **Cursor**: Ensure `.cursorrules` files are in `.cursor/rules/`
- **Copilot**: Verify `.github/copilot-instructions.md` exists
- **Antigravity**: Check workflows are in correct directory
- **JetBrains**: Confirm `.ai/` directory structure

### Outputs Too Generic
- Provide more specific context (URLs, company names, code snippets)
- Reference previous session outputs
- Include examples of desired format

### Performance Issues
- Reduce scope of requests
- Use `quick` or `standard` depth modes where available
- Run complex workflows in Antigravity for better parallelization

---

## 📖 Documentation

- **Original Claude Code Docs**: See main README.md
- **ECC Integration**: See ECC-INTEGRATION-SUMMARY.md
- **Universal Framework**: This document
- **Agent Registry**: `universal/core/agents.json`

---

## 🎯 Next Steps

1. **Install adapters** for your preferred IDE(s)
2. **Test core workflows** (sales, geo, market)
3. **Customize triggers** and behaviors as needed
4. **Share feedback** to improve cross-platform experience

---

**Version:** 2.0.0 Universal  
**Last Updated:** 2024-01-15  
**Total Agents:** 357 specialists  
**Supported Platforms:** 5 (Claude Code, Cursor, VS Code, Antigravity, JetBrains)  

**Built with ❤️ by NovaVentures AI**
