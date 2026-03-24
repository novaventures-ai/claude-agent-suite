#!/bin/bash
# NovaVentures AI — Claude Agent Suite Installer
# Installs 346+ agents, 324+ commands, and skills to ~/.claude/

set -e

CLAUDE_DIR="$HOME/.claude"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "============================================"
echo "  NovaVentures AI — Claude Agent Suite"
echo "  346+ Agents | 324+ Commands | Skills"
echo "============================================"
echo ""

# Create directories if they don't exist
mkdir -p "$CLAUDE_DIR/agents"
mkdir -p "$CLAUDE_DIR/commands"
mkdir -p "$CLAUDE_DIR/skills"

# Install jCodeMunch MCP (Token-efficient AST parsing)
echo "[0/3] Installing jCodeMunch MCP Server..."
pip install jcodemunch-mcp || echo "  -> Warning: pip install failed"
claude mcp add jcodemunch uvx jcodemunch-mcp || echo "  -> Warning: claude mcp add failed"

# Install agents
echo "[1/3] Installing agents..."
cp -r "$SCRIPT_DIR/agents/"* "$CLAUDE_DIR/agents/" 2>/dev/null
AGENT_COUNT=$(ls "$CLAUDE_DIR/agents/"*.md 2>/dev/null | wc -l)
echo "  -> $AGENT_COUNT agents installed"

# Install commands
echo "[2/3] Installing commands..."
cp -r "$SCRIPT_DIR/commands/"* "$CLAUDE_DIR/commands/" 2>/dev/null
CMD_COUNT=$(find "$CLAUDE_DIR/commands" -name "*.md" 2>/dev/null | wc -l)
echo "  -> $CMD_COUNT commands installed"

# Install skills
echo "[3/3] Installing skills..."
cp -r "$SCRIPT_DIR/skills/"* "$CLAUDE_DIR/skills/" 2>/dev/null
SKILL_COUNT=$(ls -d "$CLAUDE_DIR/skills/"*/ 2>/dev/null | wc -l)
echo "  -> $SKILL_COUNT skills installed"

echo ""
echo "============================================"
echo "  Installation complete!"
echo "  Restart Claude Code to activate."
echo ""
echo "  Quick start:"
echo "    'hey jarvis'     — Master orchestrator"
echo "    /orchestrate     — Multi-agent workflow"
echo "    /geo             — GEO/SEO audit"
echo "    /market           — Marketing suite"
echo "    /sales            — Sales automation"
echo "============================================"
