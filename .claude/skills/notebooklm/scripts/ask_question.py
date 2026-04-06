#!/usr/bin/env python3
"""Ask a question / request analysis from a NotebookLM notebook."""

import argparse
import asyncio
import json
import sys

from notebooklm import NotebookLMClient


async def main(notebook_id: str, question: str):
    try:
        async with await NotebookLMClient.from_storage() as client:
            result = await client.chat.ask(notebook_id, question)
            print(json.dumps({"answer": result.answer}, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ask a question to a NotebookLM notebook.")
    parser.add_argument("--notebook-id", required=True, help="Notebook ID")
    parser.add_argument("--question", required=True, help="Question to ask")
    args = parser.parse_args()
    asyncio.run(main(args.notebook_id, args.question))
