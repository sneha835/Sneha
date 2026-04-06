#!/usr/bin/env python3
"""Generate an artifact (infographic, slide-deck, flashcards, etc.) from a NotebookLM notebook."""

import argparse
import asyncio
import json
import sys

from notebooklm import NotebookLMClient

VALID_TYPES = [
    "audio", "video", "slide-deck", "quiz", "flashcards",
    "report", "mind-map", "infographics", "data-table",
]


async def main(notebook_id: str, artifact_type: str, style: str | None):
    try:
        options = {}
        if style:
            options["style"] = style

        async with await NotebookLMClient.from_storage() as client:
            artifact = await client.artifacts.generate(notebook_id, artifact_type, options)
            print(json.dumps({
                "notebook_id": notebook_id,
                "type": artifact_type,
                "style": style,
                "artifact": str(artifact),
            }, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a NotebookLM artifact.")
    parser.add_argument("--notebook-id", required=True, help="Notebook ID")
    parser.add_argument("--type", required=True, choices=VALID_TYPES,
                        help="Artifact type to generate")
    parser.add_argument("--style", default=None,
                        help="Optional style/prompt for the artifact (e.g., 'handwritten / chalkboard')")
    args = parser.parse_args()
    asyncio.run(main(args.notebook_id, args.type, args.style))
