#!/usr/bin/env python3
"""Keyword Research Script — Google Trends India.

Finds top related keywords for any product/topic and returns
search interest data from Google Trends (geo: India).
"""

import argparse
import json
import sys
import time
from datetime import datetime


def get_keywords(topic, count=10, timeframe="today 12-m"):
    """Fetch top keywords and their interest data from Google Trends."""
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("ERROR: pytrends not installed. Run: pip install pytrends", file=sys.stderr)
        sys.exit(1)

    max_retries = 3
    pytrends = None

    for attempt in range(max_retries):
        try:
            pytrends = TrendReq(hl="en-IN", tz=330, retries=2, backoff_factor=1)
            break
        except Exception as e:
            if attempt < max_retries - 1:
                wait = (attempt + 1) * 5
                print(f"  Rate limited, retrying in {wait}s... ({attempt + 1}/{max_retries})", file=sys.stderr)
                time.sleep(wait)
            else:
                return {"error": f"Google Trends connection failed: {str(e)}", "keywords": []}

    seed_keywords = [topic]
    last_word = topic.strip().split()[-1]
    seed_keywords.extend([
        f"{topic} for kids",
        f"ayurvedic {last_word}",
        f"best {topic} india",
        f"{topic} for babies",
    ])
    seed_keywords = seed_keywords[:5]

    all_related = {}

    for i, seed in enumerate(seed_keywords):
        if i > 0:
            time.sleep(10)

        try:
            pytrends.build_payload([seed], cat=0, timeframe=timeframe, geo="IN")

            related = pytrends.related_queries()
            if seed in related:
                top_df = related[seed].get("top")
                if top_df is not None and not top_df.empty:
                    for _, row in top_df.iterrows():
                        kw = row.get("query", "")
                        val = int(row.get("value", 0))
                        if kw and kw not in all_related:
                            all_related[kw] = {"keyword": kw, "related_score": val, "source_seed": seed}

                rising_df = related[seed].get("rising")
                if rising_df is not None and not rising_df.empty:
                    for _, row in rising_df.iterrows():
                        kw = row.get("query", "")
                        val = str(row.get("value", "0"))
                        if kw and kw not in all_related:
                            all_related[kw] = {"keyword": kw, "related_score": 0, "rising": val, "source_seed": seed}

        except Exception:
            continue

    sorted_keywords = sorted(all_related.values(), key=lambda x: x.get("related_score", 0), reverse=True)
    top_keywords = sorted_keywords[:count]

    if not top_keywords:
        top_keywords = [{"keyword": seed, "related_score": 0, "source_seed": topic} for seed in seed_keywords]

    results = []
    for kw_data in top_keywords:
        kw = kw_data["keyword"]
        time.sleep(10)

        try:
            pytrends.build_payload([kw], cat=0, timeframe=timeframe, geo="IN")
            iot = pytrends.interest_over_time()

            avg_interest = 0
            max_interest = 0
            direction = "unknown"

            if not iot.empty and kw in iot.columns:
                values = iot[kw].tolist()
                avg_interest = round(sum(values) / len(values), 1) if values else 0
                max_interest = max(values) if values else 0

                last_3 = values[-12:] if len(values) >= 12 else values[-3:]
                last_3_avg = sum(last_3) / len(last_3) if last_3 else 0
                if last_3_avg > avg_interest * 1.1:
                    direction = "increasing"
                elif last_3_avg < avg_interest * 0.9:
                    direction = "declining"
                else:
                    direction = "stable"

            regions = {}
            try:
                ibr = pytrends.interest_by_region(resolution="REGION", inc_low_vol=True)
                if not ibr.empty and kw in ibr.columns:
                    top_reg = ibr[kw].sort_values(ascending=False).head(5)
                    regions = {k: int(v) for k, v in top_reg.items()}
            except Exception:
                pass

            results.append({
                "keyword": kw,
                "avg_interest": avg_interest,
                "max_interest": max_interest,
                "direction": direction,
                "top_regions": regions,
                "rising": kw_data.get("rising"),
                "source_seed": kw_data.get("source_seed"),
            })

        except Exception:
            results.append({
                "keyword": kw,
                "avg_interest": 0,
                "max_interest": 0,
                "direction": "unknown",
                "top_regions": {},
                "source_seed": kw_data.get("source_seed"),
                "error": "Could not fetch interest data",
            })

    results.sort(key=lambda x: x.get("avg_interest", 0), reverse=True)
    return {"topic": topic, "timeframe": timeframe, "keywords": results}


def print_report(data):
    """Print formatted keyword research report."""
    print(f"\n{'='*80}")
    print(f"  KEYWORD RESEARCH: \"{data['topic']}\"")
    print(f"  Timeframe: {data['timeframe']}")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*80}\n")

    if data.get("error"):
        print(f"  ERROR: {data['error']}\n")
        return

    keywords = data.get("keywords", [])
    if not keywords:
        print("  No keywords found.\n")
        return

    print(f"  {'#':<4} {'Keyword':<40} {'Avg':<8} {'Peak':<8} {'Direction':<12} {'Top Region'}")
    print(f"  {'─'*4} {'─'*40} {'─'*8} {'─'*8} {'─'*12} {'─'*20}")

    for i, kw in enumerate(keywords, 1):
        regions = kw.get("top_regions", {})
        top_region = list(regions.keys())[0] if regions else "N/A"
        rising_tag = " [RISING]" if kw.get("rising") else ""
        print(f"  {i:<4} {kw['keyword'][:38]:<40} {kw['avg_interest']:<8} {kw['max_interest']:<8} {kw['direction']:<12} {top_region}{rising_tag}")

    print(f"\n{'='*80}")

    print(f"\n  REGIONAL DETAILS:")
    for kw in keywords[:5]:
        regions = kw.get("top_regions", {})
        if regions:
            print(f"\n  \"{kw['keyword']}\":")
            for state, val in regions.items():
                print(f"    {state}: {val}")

    print(f"\n{'='*80}\n")


def main():
    parser = argparse.ArgumentParser(description="Keyword Research — Google Trends India")
    parser.add_argument("--topic", required=True, help="Product or topic to find keywords for")
    parser.add_argument("--count", type=int, default=10, help="Number of top keywords (default: 10)")
    parser.add_argument("--timeframe", default="today 12-m", help="Time range (default: today 12-m)")
    parser.add_argument("--output", choices=["json", "report"], default="report", help="Output format")

    args = parser.parse_args()

    data = get_keywords(args.topic, args.count, args.timeframe)

    if args.output == "json":
        print(json.dumps(data, indent=2, default=str))
    else:
        print_report(data)


if __name__ == "__main__":
    main()
