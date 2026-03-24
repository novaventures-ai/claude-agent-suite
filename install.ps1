$CLAUDE_DIR = "$HOME\.claude"
$SCRIPT_DIR = $PSScriptRoot

Write-Host "============================================"
Write-Host "  NovaVentures AI - Claude Agent Suite"
Write-Host "  346+ Agents | 324+ Commands | Skills"
Write-Host "============================================"
Write-Host ""

New-Item -ItemType Directory -Force -Path "$CLAUDE_DIR\agents" | Out-Null
New-Item -ItemType Directory -Force -Path "$CLAUDE_DIR\commands" | Out-Null
New-Item -ItemType Directory -Force -Path "$CLAUDE_DIR\skills" | Out-Null

Write-Host "[0/3] Installing jCodeMunch MCP Server..."
try {
    pip install jcodemunch-mcp
} catch {
    Write-Host "  -> Warning: pip install failed"
}
try {
    claude mcp add jcodemunch uvx jcodemunch-mcp
} catch {
    Write-Host "  -> Warning: claude mcp add failed"
}

Write-Host "[1/3] Installing agents..."
Copy-Item -Path "$SCRIPT_DIR\agents\*" -Destination "$CLAUDE_DIR\agents\" -Recurse -Force -ErrorAction SilentlyContinue
$agentCount = (Get-ChildItem -Path "$CLAUDE_DIR\agents\*.md" | Measure-Object).Count
Write-Host "  -> $agentCount agents installed"

Write-Host "[2/3] Installing commands..."
Copy-Item -Path "$SCRIPT_DIR\commands\*" -Destination "$CLAUDE_DIR\commands\" -Recurse -Force -ErrorAction SilentlyContinue
$cmdCount = (Get-ChildItem -Path "$CLAUDE_DIR\commands\" -Filter "*.md" -Recurse | Measure-Object).Count
Write-Host "  -> $cmdCount commands installed"

Write-Host "[3/3] Installing skills..."
Copy-Item -Path "$SCRIPT_DIR\skills\*" -Destination "$CLAUDE_DIR\skills\" -Recurse -Force -ErrorAction SilentlyContinue
$skillCount = (Get-ChildItem -Path "$CLAUDE_DIR\skills" -Directory | Measure-Object).Count
Write-Host "  -> $skillCount skills installed"

Write-Host ""
Write-Host "============================================"
Write-Host "  Installation complete!"
Write-Host "  Restart Claude Code to activate."
Write-Host "============================================"
