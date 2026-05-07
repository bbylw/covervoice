#!/usr/bin/env python3
"""Generate an MP3 file from text using edge-tts.

Usage:
    python tts.py --text "你好" --voice zh-CN-YunjianNeural --out output.mp3
    python tts.py --text-file input.txt --voice en-US-AriaNeural --rate "+10%" --out out.mp3
"""
import argparse
import asyncio
import sys
from pathlib import Path

import edge_tts


async def synthesize(text: str, voice: str, rate: str, volume: str, out: Path) -> None:
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, volume=volume)
    await communicate.save(str(out))


def main() -> int:
    p = argparse.ArgumentParser(description="Edge TTS -> MP3")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="Text to synthesize")
    src.add_argument("--text-file", help="Path to a UTF-8 text file")
    p.add_argument("--voice", default="zh-CN-YunjianNeural")
    p.add_argument("--rate", default="+0%", help="+-N%, range -50% to +50%")
    p.add_argument("--volume", default="+0%", help="+-N%, range -50% to +50%")
    p.add_argument("--out", default="output.mp3", help="Output MP3 path")
    args = p.parse_args()

    if args.text_file:
        text = Path(args.text_file).read_text(encoding="utf-8")
    else:
        text = args.text
    if not text.strip():
        print("ERROR: text is empty", file=sys.stderr)
        return 2

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    asyncio.run(synthesize(text, args.voice, args.rate, args.volume, out))

    if not out.exists() or out.stat().st_size == 0:
        print(f"ERROR: output not generated at {out}", file=sys.stderr)
        return 1

    print(f"OK {out} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
