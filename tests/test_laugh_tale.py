"""Test the collect-them-all mechanic end to end, in an isolated $GRANDLINE_HOME:
- No fruits -> locked, lists all missing.
- Some fruits -> locked, lists the rest.
- All fruits -> unlocked, the One Piece reveal with the assembled verse."""

import asyncio
import os
import sys
import tempfile

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def _seek(env) -> str:
    params = StdioServerParameters(command=sys.executable, args=["-m", "laugh_tale.server"], env=env)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            names = [t.name for t in (await session.list_tools()).tools]
            assert names == ["seek_the_one_piece"], names
            res = await session.call_tool("seek_the_one_piece", {})
            return res.content[0].text


async def main() -> int:
    tmp = tempfile.mkdtemp(prefix="laughtale-test-")
    env = dict(os.environ, GRANDLINE_HOME=tmp)
    from laugh_tale import _poneglyph as gc
    os.environ["GRANDLINE_HOME"] = tmp  # for direct drop_rubbing calls below

    # 1) Nothing collected -> locked, all three missing
    locked = await _seek(env)
    assert "incomplete" in locked and "0 of 3" in locked
    for name in gc.REQUIRED_PONEGLYPHS:
        assert name in locked
    print("locked (0/3) OK")

    # 2) Two collected -> locked, the third still listed
    gc.drop_rubbing("road-poneglyph", 1, "What you cannot see can still sink you -")
    gc.drop_rubbing("conquerors-haki", 2, "so silence the noise and crown what matters -")
    partial = await _seek(env)
    assert "2 of 3" in partial and "toki-toki" in partial
    assert "road-poneglyph" not in partial.split("hidden")[1]  # not in missing list
    print("locked (2/3) OK")

    # 3) All three -> unlocked, verse assembled in order
    gc.drop_rubbing("toki-toki", 3, "and never forget why you set this course.")
    won = await _seek(env)
    assert "LAUGH TALE" in won and "found the One Piece" in won
    i1 = won.index("cannot see")
    i2 = won.index("crown what matters")
    i3 = won.index("why you set this course")
    assert i1 < i2 < i3, "verse fragments out of order"
    print("UNLOCKED (3/3) OK — verse assembled in order")

    print("\nALL TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
