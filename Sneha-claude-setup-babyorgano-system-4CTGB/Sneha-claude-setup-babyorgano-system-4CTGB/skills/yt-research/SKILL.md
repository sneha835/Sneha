# YouTube Research Skill

## Trigger Phrases
- "search YouTube for [topic]"
- "find YouTube videos about [topic]"
- "YouTube research [topic]"
- "what's on YouTube about [topic]"

## What It Does
Searches YouTube for videos on any topic using yt-dlp and returns structured metadata including titles, channels, views, duration, upload dates, and URLs.

## How to Run

```bash
source .venv/bin/activate

# Basic search (25 results, JSON)
python scripts/yt_research.py --query "TOPIC" --count 25

# Human-readable summary
python scripts/yt_research.py --query "TOPIC" --count 10 --output summary

# Filter by time
python scripts/yt_research.py --query "TOPIC" --filter week --output summary
python scripts/yt_research.py --query "TOPIC" --filter month --output summary

# Sort by views or date
python scripts/yt_research.py --query "TOPIC" --sort view_count --output summary
python scripts/yt_research.py --query "TOPIC" --sort date --output summary
```

## Parameters
- `--query` (required): Search topic
- `--count`: Number of results (default: 25)
- `--filter`: Time filter — all, latest, week, month (default: all)
- `--sort`: Sort order — relevance, date, view_count (default: relevance)
- `--output`: Output format — json, summary (default: json)

## Output Fields
Each video result includes:
- `title` — Video title
- `channel` — Channel name
- `views` — View count
- `duration_string` — Human-readable duration
- `upload_date` — Upload date (YYYY-MM-DD)
- `url` — YouTube URL
- `description_snippet` — First 200 chars of description

## Notes
- If no topic is provided, **ask the user what topic they want to research**
- JSON output can be piped to other scripts or sent to NotebookLM
- After results, offer: "Want me to send these to NotebookLM for analysis?"
