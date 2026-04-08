#!/usr/bin/env python3
"""YouTube Research Script using yt-dlp.

Searches YouTube for videos on any topic and returns structured metadata.
"""

import argparse
import json
import sys
import subprocess
import re
from datetime import datetime, timedelta


def parse_duration(duration):
    """Convert seconds to human-readable duration."""
    if not duration:
        return "Unknown"
    try:
        duration = int(duration)
        hours, remainder = divmod(duration, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"
    except (ValueError, TypeError):
        return "Unknown"


def format_views(views):
    """Format view count for human readability."""
    if not views:
        return "Unknown"
    try:
        views = int(views)
        if views >= 1_000_000:
            return f"{views / 1_000_000:.1f}M"
        elif views >= 1_000:
            return f"{views / 1_000:.1f}K"
        return str(views)
    except (ValueError, TypeError):
        return "Unknown"


def format_date(date_str):
    """Format YYYYMMDD date to readable format."""
    if not date_str:
        return "Unknown"
    try:
        dt = datetime.strptime(str(date_str), "%Y%m%d")
        return dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return str(date_str)


def get_date_filter(filter_type):
    """Get dateafter parameter for yt-dlp based on filter type."""
    if filter_type == "latest" or filter_type == "week":
        return (datetime.now() - timedelta(days=7)).strftime("%Y%m%d")
    elif filter_type == "month":
        return (datetime.now() - timedelta(days=30)).strftime("%Y%m%d")
    return None


def search_youtube(query, count=25, filter_type="all", sort="relevance"):
    """Search YouTube using yt-dlp and return video metadata."""
    search_query = f"ytsearch{count}:{query}"

    cmd = [
        sys.executable, "-m", "yt_dlp",
        search_query,
        "--dump-json",
        "--no-download",
        "--no-warnings",
        "--flat-playlist",
    ]

    sort_map = {
        "relevance": "",
        "date": "date",
        "view_count": "view_count",
    }

    date_filter = get_date_filter(filter_type)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
        )

        if result.returncode != 0 and not result.stdout.strip():
            error_msg = result.stderr.strip() if result.stderr else "Unknown error"
            if "429" in error_msg or "rate" in error_msg.lower():
                print(json.dumps({"error": "Rate limited by YouTube. Try again in a few minutes.", "results": []}))
            else:
                print(json.dumps({"error": f"yt-dlp error: {error_msg}", "results": []}))
            return []

        videos = []
        for line in result.stdout.strip().split("\n"):
            if not line.strip():
                continue
            try:
                data = json.loads(line)

                # Apply date filter if needed
                if date_filter and data.get("upload_date"):
                    if str(data["upload_date"]) < date_filter:
                        continue

                video = {
                    "title": data.get("title", "Unknown"),
                    "channel": data.get("channel", data.get("uploader", "Unknown")),
                    "views": data.get("view_count"),
                    "duration": data.get("duration"),
                    "duration_string": parse_duration(data.get("duration")),
                    "upload_date": format_date(data.get("upload_date")),
                    "url": data.get("url", data.get("webpage_url", f"https://www.youtube.com/watch?v={data.get('id', '')}")),
                    "description_snippet": (data.get("description", "") or "")[:200],
                }
                videos.append(video)
            except json.JSONDecodeError:
                continue

        # Sort results
        if sort == "view_count" and videos:
            videos.sort(key=lambda v: v.get("views") or 0, reverse=True)
        elif sort == "date" and videos:
            videos.sort(key=lambda v: v.get("upload_date", ""), reverse=True)

        return videos

    except subprocess.TimeoutExpired:
        print(json.dumps({"error": "Search timed out. Try fewer results or a simpler query.", "results": []}), file=sys.stderr)
        return []
    except FileNotFoundError:
        print(json.dumps({"error": "yt-dlp not found. Install with: pip install yt-dlp", "results": []}), file=sys.stderr)
        return []
    except Exception as e:
        print(json.dumps({"error": f"Unexpected error: {str(e)}", "results": []}), file=sys.stderr)
        return []


def print_summary(videos, query):
    """Print human-readable summary of results."""
    print(f"\n{'='*70}")
    print(f"  YouTube Research: \"{query}\"")
    print(f"  Found {len(videos)} videos")
    print(f"{'='*70}\n")

    for i, v in enumerate(videos, 1):
        print(f"  {i}. {v['title']}")
        print(f"     Channel: {v['channel']}")
        print(f"     Views: {format_views(v.get('views'))} | Duration: {v['duration_string']} | Date: {v['upload_date']}")
        print(f"     URL: {v['url']}")
        if v.get('description_snippet'):
            snippet = v['description_snippet'][:100]
            print(f"     {snippet}...")
        print()

    print(f"{'='*70}")


def main():
    parser = argparse.ArgumentParser(description="Search YouTube for videos on any topic")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--count", type=int, default=25, help="Number of results (default: 25)")
    parser.add_argument("--filter", choices=["all", "latest", "week", "month"], default="all",
                        help="Time filter (default: all)")
    parser.add_argument("--sort", choices=["relevance", "date", "view_count"], default="relevance",
                        help="Sort order (default: relevance)")
    parser.add_argument("--output", choices=["json", "summary"], default="json",
                        help="Output format (default: json)")

    args = parser.parse_args()

    videos = search_youtube(
        query=args.query,
        count=args.count,
        filter_type=args.filter,
        sort=args.sort,
    )

    if args.output == "summary":
        print_summary(videos, args.query)
    else:
        output = {
            "query": args.query,
            "count": len(videos),
            "filter": args.filter,
            "sort": args.sort,
            "results": videos,
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
