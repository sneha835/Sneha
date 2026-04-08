#!/usr/bin/env python3
"""Add YouTube URLs as sources to a NotebookLM notebook."""

import argparse
import asyncio
import json
import sys

from notebooklm import NotebookLMClient

DELAY_BETWEEN_SOURCES = 1.5  # seconds, to avoid rate limits


async def main(notebook_id: str, urls: list[str]):
    added = []
    failed = []

    try:
        async with await NotebookLMClient.from_storage() as client:
            for i, url in enumerate(urls):
                try:
                    await client.sources.add_youtube(notebook_id, url)
                    added.append(url)
                    print(f"[{i + 1}/{len(urls)}] Added: {url}", file=sys.stderr)
                except Exception as e:
                    failed.append({"url": url, "error": str(e)})
                    print(f"[{i + 1}/{len(urls)}] Failed: {url} - {e}", file=sys.stderr)

                if i < len(urls) - 1:
                    await asyncio.sleep(DELAY_BETWEEN_SOURCES)

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

    result = {
        "notebook_id": notebook_id,
        "total": len(urls),
        "added": len(added),
        "failed_count": len(failed),
        "failed": failed,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add YouTube sources to a notebook.")
    parser.add_argument("--notebook-id", required=True, help="Notebook ID")
    parser.add_argument("--urls", nargs="+", required=True, help="YouTube video URLs")
    args = parser.parse_args()
    asyncio.run(main(args.notebook_id, args.urls))
