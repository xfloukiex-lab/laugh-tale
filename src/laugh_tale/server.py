"""Laugh Tale — the final island of the Grand Line MCP stack.

The capstone. It stays LOCKED until every Road Poneglyph rubbing has been
gathered (i.e. every fruit installed, each having dropped its rubbing). Call it
with fruits still missing and it points you to the ones you haven't collected.
Gather them all and the rubbings align — revealing the One Piece.

The One Piece is not a new power (the fruits already do the work). It's the
treasure at the end of the journey: you collected the whole crew.
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from ._poneglyph import collected_rubbings, missing_poneglyphs, REQUIRED_PONEGLYPHS

mcp = FastMCP("laugh-tale")

_TREASURE = r"""
        .------------------.
       /  .--------------.  \
      /  /   ONE  PIECE   \  \
      |  |   __________    |  |
      |  |  /          \   |  |
      |  | |  $  *  $  $ |  |  |
       \  \ \__________/  /  /
        \  '--------------'  /
         '------------------'
"""


@mcp.tool()
def seek_the_one_piece() -> str:
    """Set sail for Laugh Tale. Reveals the One Piece — but ONLY if every Road
    Poneglyph rubbing has been gathered (every fruit of the Grand Line stack
    installed). Otherwise it reports which poneglyphs are still missing."""
    missing = missing_poneglyphs()
    rubbings = collected_rubbings()
    have = len(REQUIRED_PONEGLYPHS) - len(missing)
    total = len(REQUIRED_PONEGLYPHS)

    if missing:
        missing_lines = "\n".join(f"  - {name}" for name in missing)
        return f"""\
🗿 The Road Poneglyphs are incomplete. {have} of {total} rubbings gathered.

The course to Laugh Tale will not light until every Poneglyph is read. Still
hidden — install these fruits of the Grand Line stack:
{missing_lines}

Gather them all, then seek the One Piece again.
"""

    verse = "\n".join(r.get("fragment", "") for r in rubbings)
    return f"""\
🏴‍☠️  LAUGH TALE — THE FINAL ISLAND  🏴‍☠️

All {total} Road Poneglyph rubbings align. The road is lit.
{_TREASURE}
The poneglyphs, read together:

    "{verse}"

You gathered every Fruit of the Grand Line — and so you found the One Piece.

The treasure was never a single tool. It was the whole crew, sailing as one:
the eyes that see what's missing, the will that crowns what matters, and the
memory that knows why. Now go — the New World is yours.
"""


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
