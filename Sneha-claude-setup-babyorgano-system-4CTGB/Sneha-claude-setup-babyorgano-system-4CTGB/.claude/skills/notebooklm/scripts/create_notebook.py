#!/usr/bin/env python3
"""Create a new NotebookLM notebook."""

import argparse
import asyncio
import json
import sys

from notebooklm import NotebookLMClient


async def main(title: str):
    try:
        async with await NotebookLMClient.from_storage() as client:
            nb = await client.notebooks.create(title)
            print(json.dumps({"notebook_id": nb.id, "title": title}))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a NotebookLM notebook.")
    parser.add_argument("--title", required=True, help="Notebook title")
    args = parser.parse_args()
    asyncio.run(main(args.title))
