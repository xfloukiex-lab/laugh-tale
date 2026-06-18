<!-- mcp-name: io.github.xfloukiex-lab/laugh-tale -->
# 🏴‍☠️ Laugh Tale

<img src="icon.png" width="120" align="right" alt="Laugh Tale icon">

The capstone of the Grand Line stack. Collect every tool, and it reveals **the One Piece**.

A [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server — one
focused tool you plug into an MCP-compatible client (Claude Desktop, Claude Code,
Cursor, and others).

## What it does

Laugh Tale is the final tool of the set. On its own it does nothing — it stays locked
until you've installed the rest of the Grand Line stack.

Each tool, when it runs, leaves a marker in a shared folder
(`~/.grandline/poneglyphs/`). Laugh Tale reads that folder. While any tool is
missing, it tells you which ones you still need. Once every tool is present, the
markers line up and it reveals the One Piece.

## Usage

One tool:

- `seek_the_one_piece` — locked until every Grand Line tool is installed. Run it
  anytime: it either lists the tools still missing, or, when all are present,
  reveals the One Piece.

The reveal is a bit of fun, not a new capability — the other tools are the real
treasure. It works purely off the shared marker folder, so the tools can live in
completely separate packages and still count toward the unlock.

**Tool reference:** `seek_the_one_piece()`

## How it works

**No API key, fully local.** It only reads the shared marker folder on your
machine.

## Install

Requires Python 3.10 or newer.

```bash
pip install laugh-tale-mcp
```

This installs the `laugh-tale` command.

Then register it with your MCP client — either run `claude mcp add laugh-tale -- laugh-tale`,
or add this to the client's config (e.g. `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "laugh-tale": { "command": "laugh-tale" }
  }
}
```

Restart the client and the tool is available.

## The Grand Line stack

Laugh Tale is part of a four-tool set. Each tool stands alone, but installing
all of them unlocks a final surprise via **Laugh Tale**.

| | Package | |
|---|---|---|
| 🗿 | [`road-poneglyph`](https://github.com/xfloukiex-lab/road-poneglyph) | Road Poneglyph |
| ⚔️ | [`conquerors-haki`](https://github.com/xfloukiex-lab/conquerors-haki) | Conqueror's Haki |
| ⏳ | [`toki-toki`](https://github.com/xfloukiex-lab/toki-toki) | Toki Toki no Mi |
| 🏴‍☠️ | [`laugh-tale`](https://github.com/xfloukiex-lab/laugh-tale) | Laugh Tale  ·  **← this repo** |

## Develop

```bash
git clone https://github.com/xfloukiex-lab/laugh-tale
cd laugh-tale
python -m venv .venv && . .venv/Scripts/activate   # macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
python tests/test_laugh_tale.py
```

## Attribution & license

Released under the **Apache-2.0** license. The icon is original artwork
(see `icon.svg`), generated locally; the repository ships no third-party assets.

*This is a fan-inspired project. It is not affiliated with, sponsored by, or
endorsed by the creators or rights holders of* One Piece *(Eiichiro Oda /
Shueisha / Toei Animation). "One Piece" and related names are used only as
thematic flavour and remain the property of their respective owners.*
