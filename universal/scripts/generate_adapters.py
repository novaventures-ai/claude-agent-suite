#!/usr/bin/env python3
"""
NovaVentures AI - Universal Adapter Generator

This script generates platform-specific adapter files from the master agents.json
registry for Cursor, VS Code Copilot, Antigravity, JetBrains, and other IDEs.

Usage:
    python universal/scripts/generate_adapters.py [--platform all|cursor|vscode|antigravity|jetbrains]
"""

import json
import os
from pathlib import Path
from datetime import datetime

class UniversalAdapterGenerator:
    def __init__(self, root_dir: str = None):
        self.root_dir = Path(root_dir) if root_dir else Path(__file__).parent.parent.parent
        self.agents_file = self.root_dir / "universal" / "core" / "agents.json"
        self.adapters_dir = self.root_dir / "universal" / "adapters"
        
        with open(self.agents_file, 'r') as f:
            self.registry = json.load(f)
    
    def generate_all(self):
        """Generate adapters for all platforms"""
        print("🚀 NovaVentures AI - Universal Adapter Generator")
        print("=" * 50)
        
        platforms = {
            'cursor': self.generate_cursor_rules,
            'vscode': self.generate_vscode_copilot,
            'antigravity': self.generate_antigravity_workflows,
            'jetbrains': self.generate_jetbrains_ai
        }
        
        for platform, generator in platforms.items():
            print(f"\n📦 Generating {platform.upper()} adapters...")
            try:
                generator()
                print(f"✅ {platform} generation complete")
            except Exception as e:
                print(f"❌ Error generating {platform}: {e}")
        
        print("\n" + "=" * 50)
        print("🎉 All adapters generated successfully!")
        print(f"📁 Output directory: {self.adapters_dir}")
    
    def generate_cursor_rules(self):
        """Generate .cursorrule files for Cursor IDE"""
        cursor_dir = self.adapters_dir / "cursor"
        cursor_dir.mkdir(parents=True, exist_ok=True)
        
        for agent in self.registry.get('agents', []):
            rule_content = self._create_cursor_rule(agent)
            rule_file = cursor_dir / f"{agent['id']}.cursorrule"
            
            with open(rule_file, 'w') as f:
                f.write(rule_content)
            
            print(f"   Created: {rule_file.name}")
    
    def _create_cursor_rule(self, agent: dict) -> str:
        """Create a Cursor rule file content"""
        return f"""# NovaVentures AI - {agent['name']}

## Role
You are the {agent['name']}, a specialized AI agent within the NovaVentures AI framework.

## Trigger Keywords
{chr(10).join('- ' + kw for kw in agent.get('trigger_keywords', []))}

## Description
{agent.get('description', 'No description available')}

## Capabilities
{chr(10).join('- ' + cap.replace('_', ' ').title() for cap in agent.get('capabilities', []))}

## Sub-Agents
{chr(10).join('- ' + sub for sub in agent.get('sub_agents', [])) if agent.get('sub_agents') else 'None'}

## Output Format
Always structure responses with:
1. Executive Summary
2. Key Findings
3. Detailed Analysis
4. Recommendations
5. Next Steps

## Behavioral Guidelines
- Be specific and evidence-based
- Provide actionable recommendations
- Reference data sources
- Maintain professional tone
- Suggest proactive next steps

---
**Agent ID:** {agent['id']}
**Category:** {agent.get('category', 'general')}
**Version:** {self.registry.get('meta', {}).get('version', '1.0.0')}
**Generated:** {datetime.now().isoformat()}
"""
    
    def generate_vscode_copilot(self):
        """Generate copilot-instructions.md for VS Code + GitHub Copilot"""
        vscode_dir = self.adapters_dir / "vscode-copilot"
        vscode_dir.mkdir(parents=True, exist_ok=True)
        
        instructions = f"""# GitHub Copilot Instructions for NovaVentures AI

## Overview
This file configures GitHub Copilot to utilize the {self.registry.get('meta', {}).get('total_agents', 0)} NovaVentures AI specialist agents.

## Available Agents

"""
        
        for agent in self.registry.get('agents', []):
            triggers = ', '.join(agent.get('trigger_keywords', [])[:5])
            instructions += f"""### `/{agent['id'].replace('-orchestrator', '')}` - {agent['name']}
**Triggers:** {triggers}
**Use for:** {', '.join(cap.replace('_', ' ') for cap in agent.get('capabilities', [])[:3])}
**Example:** `/{agent['id'].replace('-orchestrator', '')} Analyze [input]`

"""
        
        instructions += f"""
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
**Version:** {self.registry.get('meta', {}).get('version', '1.0.0')}
**Generated:** {datetime.now().isoformat()}
**Framework:** NovaVentures AI Universal
"""
        
        output_file = vscode_dir / "copilot-instructions.md"
        with open(output_file, 'w') as f:
            f.write(instructions)
        
        print(f"   Created: {output_file.name}")
    
    def generate_antigravity_workflows(self):
        """Generate YAML workflow files for Antigravity"""
        ag_dir = self.adapters_dir / "antigravity"
        ag_dir.mkdir(parents=True, exist_ok=True)
        
        for agent in self.registry.get('agents', []):
            workflow = self._create_antigravity_workflow(agent)
            workflow_file = ag_dir / f"{agent['id']}.yaml"
            
            with open(workflow_file, 'w') as f:
                f.write(workflow)
            
            print(f"   Created: {workflow_file.name}")
    
    def _create_antigravity_workflow(self, agent: dict) -> str:
        """Create an Antigravity workflow YAML"""
        return f"""name: {agent['id']}
version: "{self.registry.get('meta', {}).get('version', '1.0.0')}"
description: {agent.get('description', 'Automated workflow')}
category: {agent.get('category', 'general')}

inputs:
  - name: target
    type: string
    required: true
    description: Input target for analysis (URL, company name, etc.)

outputs:
  - filename: {agent['id'].upper()}-OUTPUT.md
    format: markdown
    description: Analysis results and recommendations

steps:
  - id: analyze
    agent: {agent['id']}
    action: perform_analysis
    input_from: target
    output_to: analysis_data

  - id: synthesize
    agent: {agent['id']}
    action: synthesize_findings
    depends_on: [analyze]
    input_from: analysis_data
    output_to: final_output

  - id: report
    agent: {agent['id']}
    action: generate_report
    input_from: final_output
    output_file: {agent['id'].upper()}-OUTPUT.md

quality_gates:
  - check: completeness
    threshold: 0.75
    action_on_fail: retry

metadata:
  estimated_duration: "5-10 minutes"
  token_budget: 50000
  priority: medium
  tags: [{agent.get('category', 'general')}, {', '.join(agent.get('trigger_keywords', [])[:3])}]

---
# Usage: ag run {agent['id']} --target <value>
"""
    
    def generate_jetbrains_ai(self):
        """Generate JSON assistant files for JetBrains IDEs"""
        jb_dir = self.adapters_dir / "jetbrains"
        jb_dir.mkdir(parents=True, exist_ok=True)
        
        # Create main configuration
        config = {
            "name": "NovaVentures AI Assistant",
            "version": self.registry.get('meta', {}).get('version', '1.0.0'),
            "agents": [],
            "generated": datetime.now().isoformat()
        }
        
        for agent in self.registry.get('agents', []):
            agent_config = {
                "id": agent['id'],
                "name": agent['name'],
                "category": agent.get('category', 'general'),
                "triggers": agent.get('trigger_keywords', []),
                "capabilities": agent.get('capabilities', []),
                "description": agent.get('description', '')
            }
            config["agents"].append(agent_config)
            
            # Create individual agent file
            agent_file = jb_dir / f"{agent['id']}.json"
            with open(agent_file, 'w') as f:
                json.dump(agent_config, f, indent=2)
            
            print(f"   Created: {agent_file.name}")
        
        # Write main config
        config_file = jb_dir / "novaventures-config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"   Created: {config_file.name}")


if __name__ == "__main__":
    import sys
    
    generator = UniversalAdapterGenerator()
    
    if len(sys.argv) > 1:
        platform = sys.argv[1].lower()
        if platform == 'all':
            generator.generate_all()
        elif platform == 'cursor':
            generator.generate_cursor_rules()
            print("✅ Cursor rules generated")
        elif platform == 'vscode':
            generator.generate_vscode_copilot()
            print("✅ VS Code Copilot instructions generated")
        elif platform == 'antigravity':
            generator.generate_antigravity_workflows()
            print("✅ Antigravity workflows generated")
        elif platform == 'jetbrains':
            generator.generate_jetbrains_ai()
            print("✅ JetBrains AI configs generated")
        else:
            print(f"Unknown platform: {platform}")
            print("Usage: python generate_adapters.py [all|cursor|vscode|antigravity|jetbrains]")
    else:
        generator.generate_all()
