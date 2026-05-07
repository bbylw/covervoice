#!/usr/bin/env python3
"""Combine a cover image and an audio file into a 1080P MP4 video.

Uses FFmpeg to create a video where the static cover image is displayed
for the full duration of the audio track. Output is 1080x1920 (9:16).

Requirements:
    FFmpeg (with bundled ffprobe) must be installed and on PATH.
        Windows: winget install Gyan.FFmpeg
        macOS:   brew install ffmpeg
        Linux:   sudo apt install ffmpeg
    No Python packages are required (only the standard library).

Usage:
    python cover_to_video.py --image cover.png --audio voice.mp3 --out video.mp4
    python cover_to_video.py --image cover.png --audio voice.mp3 --out video.mp4 --fade-in 1.5 --fade-out 2.0
"""
import argparse
import subprocess
import sys
from pathlib import Path


def get_audio_duration(audio_path: Path) -> float:
    """Get audio duration in seconds using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed: {result.stderr}")
    return float(result.stdout.strip())


def build_ffmpeg_cmd(image: Path, audio: Path, out: Path, duration: float,
                     fade_in: float, fade_out: float) -> list:
    """Build FFmpeg command for image + audio -> MP4."""
    filters = []

    # Build video filter chain
    vf = f"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,fps=30"

    # Add fade effects if requested
    fade_parts = []
    if fade_in > 0:
        fade_in = min(fade_in, duration / 2)
        fade_parts.append(f"fade=t=in:st=0:d={fade_in}")
    if fade_out > 0:
        fade_out = min(fade_out, duration / 2)
        fade_start = max(0, duration - fade_out)
        fade_parts.append(f"fade=t=out:st={fade_start}:d={fade_out}")

    if fade_parts:
        vf += "," + ",".join(fade_parts)

    filters.append(vf)

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(image),
        "-i", str(audio),
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-vf", filters[0],
        "-shortest",
        "-t", str(duration),
        str(out)
    ]
    return cmd


def main() -> int:
    p = argparse.ArgumentParser(description="Cover image + audio -> 9:16 MP4 video")
    p.add_argument("--image", required=True, help="Path to cover image (PNG/JPG)")
    p.add_argument("--audio", required=True, help="Path to audio file (MP3/WAV)")
    p.add_argument("--out", default="output.mp4", help="Output MP4 path")
    p.add_argument("--fade-in", type=float, default=0, help="Fade in duration in seconds")
    p.add_argument("--fade-out", type=float, default=0, help="Fade out duration in seconds")
    args = p.parse_args()

    image = Path(args.image).resolve()
    audio = Path(args.audio).resolve()
    out = Path(args.out).resolve()

    if not image.exists():
        print(f"ERROR: image not found: {image}", file=sys.stderr)
        return 1
    if not audio.exists():
        print(f"ERROR: audio not found: {audio}", file=sys.stderr)
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)

    # Check FFmpeg + ffprobe availability (both are needed)
    for tool in ("ffmpeg", "ffprobe"):
        try:
            subprocess.run([tool, "-version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"ERROR: {tool} not found in PATH. Please install FFmpeg first.", file=sys.stderr)
            print("  Windows: winget install Gyan.FFmpeg", file=sys.stderr)
            print("  macOS:   brew install ffmpeg", file=sys.stderr)
            print("  Linux:   sudo apt install ffmpeg", file=sys.stderr)
            print("  (Official FFmpeg builds bundle ffprobe; if it is missing, reinstall a complete build.)", file=sys.stderr)
            return 1

    try:
        duration = get_audio_duration(audio)
    except Exception as e:
        print(f"ERROR: failed to get audio duration: {e}", file=sys.stderr)
        return 1

    print(f"Audio duration: {duration:.2f}s")
    print(f"Output: {out}")

    cmd = build_ffmpeg_cmd(image, audio, out, duration, args.fade_in, args.fade_out)
    print(f"Running: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: FFmpeg failed:\n{result.stderr}", file=sys.stderr)
        return 1

    if not out.exists() or out.stat().st_size == 0:
        print(f"ERROR: output not generated at {out}", file=sys.stderr)
        return 1

    print(f"OK {out} ({out.stat().st_size} bytes, {duration:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
