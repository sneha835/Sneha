#!/usr/bin/env python3
"""Search YouTube for videos using yt-dlp and return structured metadata."""

import argparse
import json
import sys

from yt_dlp import YoutubeDL


def search_youtube(query: str, max_results: int = 10, sort: str = "relevance") -> list[dict]:
    """Search YouTube and return video metadata without downloading."""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False,
        "skip_download": True,
        "ignoreerrors": True,
    }

    if sort == "date":
        search_url = f"ytsearch_date{max_results}:{query}"
    else:
        search_url = f"ytsearch{max_results}:{query}"

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_url, download=False)

    results = []
    for entry in info.get("entries", []):
        if entry is None:
            continue
        results.append({
            "title": entry.get("title"),
            "url": entry.get("webpage_url"),
            "author": entry.get("uploader") or entry.get("channel"),
            "views": entry.get("view_count"),
            "duration": entry.get("duration_string") or _format_duration(entry.get("duration")),
            "upload_date": entry.get("upload_date"),
        })

    return results


def _format_duration(seconds):
    """Convert duration in seconds to a human-readable string."""
    if seconds is None:
        return None
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def main():
    parser = argparse.ArgumentParser(description="Search YouTube for videos.")
    parser.add_argument("--query", "-q", required=True, help="Search query")
    parser.add_argument("--max-results", "-n", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("--sort", choices=["relevance", "date"], default="relevance",
                        help="Sort order: relevance (default) or date (latest/trending)")
    args = parser.parse_args()

    try:
        results = search_youtube(args.query, args.max_results, args.sort)
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
