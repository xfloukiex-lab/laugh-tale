<!-- mcp-name: io.github.xfloukiex-lab/laugh-tale -->
# 🏴‍☠️ Laugh Tale — the One Piece

> **Fan-inspired homage. Not affiliated with, sponsored by, or endorsed by the
> creators or rights holders of *One Piece* (Eiichiro Oda / Shueisha / Toei
> Animation).** All code and artwork here are original; no official assets, logos,
> or artwork are used. "One Piece" and related marks belong to their owners.

<img src="icon.png" width="120" align="right">

A [Model Context Protocol](https://modelcontextprotocol.io) server. The **capstone**. It stays locked until every Road Poneglyph rubbing is gathered — i.e. until all three fruits are installed and each has dropped its rubbing. Collect them all and `seek_the_one_piece` reveals **the One Piece**.

**Tool:** `seek_the_one_piece`

The reveal is an easter-egg — the three fruits are the real treasure. Works via a shared on-disk folder (`~/.grandline/poneglyphs/`), so the fruits can live in completely separate repos and still count.

## Install

Requires Python ≥ 3.10.

```bash
pip install laugh-tale
```

Then add to your MCP client config (e.g. Claude Desktop, or `claude mcp add`):

```json
{ "mcpServers": { "laugh-tale": { "command": "laugh-tale" } } }
```

## Develop

```bash
git clone https://github.com/xfloukiex-lab/laugh-tale
cd laugh-tale
python -m venv .venv && . .venv/Scripts/activate   # or .venv/bin/activate
pip install -e ".[dev]"
python tests/test_laugh_tale.py
```

## 🏴‍☠️ Part of the Grand Line stack — collect them all

Each tool drops a *poneglyph rubbing* into `~/.grandline/poneglyphs/`. Install all of them and **Laugh Tale** reveals the One Piece.

- 🗿 [`road-poneglyph`](https://github.com/xfloukiex-lab/road-poneglyph) — Road Poneglyph
- ⚔️ [`conquerors-haki`](https://github.com/xfloukiex-lab/conquerors-haki) — Conqueror's Haki
- ⏳ [`toki-toki`](https://github.com/xfloukiex-lab/toki-toki) — Toki Toki no Mi
- 🏴‍☠️ [`laugh-tale`](https://github.com/xfloukiex-lab/laugh-tale) — Laugh Tale — the One Piece ← you are here

## License

Apache-2.0. Icon: original art (see source `icon.svg`); generated locally, no
official assets.
