#!/usr/bin/env python3
"""DPAP Social Media Research Script.

Multi-platform research: YouTube, Reddit, Google News, Instagram, Quora.
Designed for BabyOrgano product research across Indian platforms.
"""

import argparse
import json
import subprocess
import sys
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import quote_plus


# ── Sentiment keywords ──────────────────────────────────────────────────────

POSITIVE_KEYWORDS = [
    "love", "amazing", "great", "excellent", "best", "recommend", "effective",
    "works", "helped", "good", "fantastic", "wonderful", "perfect", "safe",
    "trusted", "natural", "organic", "ayurvedic", "beneficial", "healthy",
    "improved", "better", "favourite", "favorite", "must-have", "life-saver",
]

NEGATIVE_KEYWORDS = [
    "bad", "worst", "terrible", "harmful", "dangerous", "fake", "scam",
    "waste", "useless", "side effect", "allergy", "allergic", "rash",
    "complaint", "problem", "issue", "avoid", "don't buy", "not safe",
    "chemical", "toxic", "misleading", "fraud", "recall", "ban", "unsafe",
]

COMPLAINT_KEYWORDS = [
    "complaint", "problem", "issue", "side effect", "harmful", "allergy",
    "fake", "scam", "waste", "not working", "dangerous", "worst", "recall",
    "ban", "unsafe", "risk", "warning",
]


# ── YouTube Research (via yt-dlp) ────────────────────────────────────────────

def research_youtube(product, yt_count=15):
    """Run multiple YouTube searches and deduplicate results."""
    queries = [
        product,
        f"{product} review india",
        f"{product} benefits side effects",
        f"best {product} india",
        f"{product} ayurvedic",
    ]

    all_videos = {}
    complaint_videos = []

    for query in queries:
        search_query = f"ytsearch{yt_count}:{query}"
        cmd = [
            sys.executable, "-m", "yt_dlp",
            search_query,
            "--dump-json",
            "--no-download",
            "--no-warnings",
            "--flat-playlist",
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            for line in result.stdout.strip().split("\n"):
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    vid_id = data.get("id", "")
                    if vid_id in all_videos:
                        continue

                    title = data.get("title", "")
                    video = {
                        "title": title,
                        "channel": data.get("channel", data.get("uploader", "Unknown")),
                        "views": data.get("view_count", 0),
                        "duration": data.get("duration", 0),
                        "upload_date": data.get("upload_date", ""),
                        "url": data.get("url", data.get("webpage_url", f"https://www.youtube.com/watch?v={vid_id}")),
                        "description_snippet": (data.get("description", "") or "")[:200],
                    }
                    all_videos[vid_id] = video

                    # Flag complaint/problem videos
                    title_lower = title.lower()
                    desc_lower = (data.get("description", "") or "").lower()
                    if any(kw in title_lower or kw in desc_lower for kw in COMPLAINT_KEYWORDS):
                        complaint_videos.append(video)

                except json.JSONDecodeError:
                    continue
        except (subprocess.TimeoutExpired, Exception):
            continue

    # Sort by views, take top 15
    sorted_videos = sorted(all_videos.values(), key=lambda v: v.get("views") or 0, reverse=True)[:15]

    return {
        "platform": "youtube",
        "total_found": len(all_videos),
        "top_videos": sorted_videos,
        "complaint_videos": complaint_videos,
        "queries_run": queries,
    }


# ── Reddit Research (public JSON API) ────────────────────────────────────────

def research_reddit(product):
    """Search Reddit using public JSON API (no login needed)."""
    import requests

    headers = {"User-Agent": "BabyOrgano-Research/1.0"}
    subreddits = ["", "india", "IndianParents", "Ayurveda", "supplements"]
    all_posts = {}
    positive_count = 0
    negative_count = 0

    for sub in subreddits:
        if sub:
            url = f"https://www.reddit.com/r/{sub}/search.json?q={quote_plus(product)}&sort=top&t=year&limit=25&restrict_sr=on"
        else:
            url = f"https://www.reddit.com/search.json?q={quote_plus(product)}&sort=top&t=year&limit=25"

        try:
            resp = requests.get(url, headers=headers, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                for child in data.get("data", {}).get("children", []):
                    post = child.get("data", {})
                    post_id = post.get("id", "")
                    if post_id in all_posts:
                        continue

                    title = post.get("title", "")
                    selftext = post.get("selftext", "")
                    combined = (title + " " + selftext).lower()

                    # Sentiment analysis
                    pos = sum(1 for kw in POSITIVE_KEYWORDS if kw in combined)
                    neg = sum(1 for kw in NEGATIVE_KEYWORDS if kw in combined)
                    positive_count += pos
                    negative_count += neg

                    all_posts[post_id] = {
                        "title": title,
                        "subreddit": post.get("subreddit", "unknown"),
                        "score": post.get("score", 0),
                        "num_comments": post.get("num_comments", 0),
                        "url": f"https://reddit.com{post.get('permalink', '')}",
                        "created": datetime.fromtimestamp(post.get("created_utc", 0)).strftime("%Y-%m-%d") if post.get("created_utc") else "Unknown",
                        "sentiment_positive": pos,
                        "sentiment_negative": neg,
                    }
            elif resp.status_code == 429:
                continue  # Rate limited, skip
        except Exception:
            continue

    sorted_posts = sorted(all_posts.values(), key=lambda p: p.get("score", 0), reverse=True)

    total_signals = positive_count + negative_count
    sentiment_summary = "neutral"
    if total_signals > 0:
        pos_ratio = positive_count / total_signals
        if pos_ratio > 0.6:
            sentiment_summary = "positive"
        elif pos_ratio < 0.4:
            sentiment_summary = "negative"

    return {
        "platform": "reddit",
        "total_posts": len(all_posts),
        "posts": sorted_posts[:25],
        "sentiment": {
            "positive_signals": positive_count,
            "negative_signals": negative_count,
            "overall": sentiment_summary,
        },
        "subreddits_searched": subreddits,
    }


# ── Google News Research (RSS) ──────────────────────────────────────────────

def research_google_news(product):
    """Search Google News via RSS feed (no login needed)."""
    import requests

    url = f"https://news.google.com/rss/search?q={quote_plus(product)}&hl=en-IN&gl=IN&ceid=IN:en"
    headers = {"User-Agent": "BabyOrgano-Research/1.0"}

    FLAG_KEYWORDS = ["recall", "ban", "unsafe", "risk", "warning", "fssai", "fake"]
    articles = []
    flagged_articles = []

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code == 200:
            # Parse RSS XML
            try:
                root = ET.fromstring(resp.text)
                channel = root.find("channel")
                if channel is not None:
                    for item in channel.findall("item")[:20]:
                        title = item.findtext("title", "")
                        link = item.findtext("link", "")
                        pub_date = item.findtext("pubDate", "")
                        source = item.findtext("source", "")

                        article = {
                            "title": title,
                            "source": source,
                            "date": pub_date,
                            "url": link,
                        }

                        # Check for flags
                        title_lower = title.lower()
                        flags = [kw for kw in FLAG_KEYWORDS if kw in title_lower]
                        if flags:
                            article["flags"] = flags
                            flagged_articles.append(article)

                        articles.append(article)
            except ET.ParseError:
                # Fallback: regex parsing
                titles = re.findall(r"<title><!\[CDATA\[(.*?)\]\]></title>", resp.text)
                links = re.findall(r"<link>(https?://[^<]+)</link>", resp.text)
                for i, title in enumerate(titles[:10]):
                    link = links[i] if i < len(links) else ""
                    article = {"title": title, "source": "", "date": "", "url": link}
                    title_lower = title.lower()
                    flags = [kw for kw in FLAG_KEYWORDS if kw in title_lower]
                    if flags:
                        article["flags"] = flags
                        flagged_articles.append(article)
                    articles.append(article)
    except Exception:
        pass

    return {
        "platform": "google_news",
        "total_articles": len(articles),
        "articles": articles[:10],
        "flagged_articles": flagged_articles,
        "flagged_count": len(flagged_articles),
    }


# ── Instagram Research (Playwright) ─────────────────────────────────────────

def research_instagram(product):
    """Check Instagram hashtag popularity using Playwright."""
    product_tag = re.sub(r'[^a-zA-Z0-9]', '', product.lower())
    hashtags = [
        product_tag, "kidshealth", "indianmom", "ayurveda",
        "naturalremedies", "kidsnutrition", "immunitybooster", "healthykids",
    ]

    results = []

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {
            "platform": "instagram",
            "status": "skipped",
            "reason": "Playwright not available",
            "hashtags": [],
        }

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            for tag in hashtags:
                try:
                    page.goto(f"https://www.instagram.com/explore/tags/{tag}/", timeout=15000)
                    page.wait_for_timeout(3000)
                    content = page.content()

                    # Try to extract post count
                    post_count = 0
                    count_match = re.search(r'([\d,]+)\s*posts?', content, re.IGNORECASE)
                    if count_match:
                        post_count = int(count_match.group(1).replace(",", ""))

                    # Determine popularity level
                    if post_count >= 1_000_000:
                        popularity = "very_high"
                    elif post_count >= 100_000:
                        popularity = "high"
                    elif post_count >= 10_000:
                        popularity = "medium"
                    elif post_count > 0:
                        popularity = "low"
                    else:
                        popularity = "unknown"

                    results.append({
                        "hashtag": f"#{tag}",
                        "post_count": post_count,
                        "popularity": popularity,
                    })
                except Exception:
                    results.append({
                        "hashtag": f"#{tag}",
                        "post_count": 0,
                        "popularity": "error",
                    })

            browser.close()
    except Exception as e:
        return {
            "platform": "instagram",
            "status": "error",
            "reason": str(e),
            "hashtags": results,
        }

    return {
        "platform": "instagram",
        "status": "completed",
        "hashtags": results,
    }


# ── Quora Research (Playwright) ──────────────────────────────────────────────

def research_quora(product):
    """Search Quora for questions about the product."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {
            "platform": "quora",
            "status": "skipped",
            "reason": "Playwright not available",
            "questions": [],
        }

    questions = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            url = f"https://www.quora.com/search?q={quote_plus(product + ' india')}&type=question"
            page.goto(url, timeout=20000)
            page.wait_for_timeout(5000)

            content = page.content()
            # Extract question titles from page
            q_matches = re.findall(r'<span[^>]*class="[^"]*q-text[^"]*"[^>]*>(.*?)</span>', content)
            if not q_matches:
                # Fallback: look for any question-like text
                q_matches = re.findall(r'(?:What|How|Why|Which|Is|Are|Can|Does|Do|Should|Where|When)[^<?"]{10,120}\??', content)

            for q in q_matches[:10]:
                q_clean = re.sub(r'<[^>]+>', '', q).strip()
                if len(q_clean) > 10:
                    questions.append({"title": q_clean})

            browser.close()
    except Exception as e:
        return {
            "platform": "quora",
            "status": "error",
            "reason": str(e),
            "questions": questions,
        }

    return {
        "platform": "quora",
        "status": "completed",
        "total_questions": len(questions),
        "questions": questions,
    }


# ── Report Generation ────────────────────────────────────────────────────────

def print_report(results, product):
    """Print human-readable research report."""
    print(f"\n{'='*70}")
    print(f"  SOCIAL MEDIA RESEARCH REPORT: \"{product}\"")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}\n")

    for platform_data in results:
        platform = platform_data.get("platform", "unknown")

        if platform == "youtube":
            print(f"  ── YOUTUBE {'─'*56}")
            print(f"  Total videos found: {platform_data.get('total_found', 0)}")
            print(f"  Complaint videos: {len(platform_data.get('complaint_videos', []))}")
            print()
            for i, v in enumerate(platform_data.get("top_videos", [])[:10], 1):
                views = v.get("views", 0)
                views_str = f"{views/1000:.1f}K" if views and views >= 1000 else str(views or 0)
                print(f"    {i}. {v['title']}")
                print(f"       Channel: {v['channel']} | Views: {views_str}")
                print(f"       URL: {v['url']}")
            print()

        elif platform == "reddit":
            print(f"  ── REDDIT {'─'*57}")
            sentiment = platform_data.get("sentiment", {})
            print(f"  Total posts: {platform_data.get('total_posts', 0)}")
            print(f"  Sentiment: {sentiment.get('overall', 'neutral')} "
                  f"(+{sentiment.get('positive_signals', 0)} / -{sentiment.get('negative_signals', 0)})")
            print()
            for i, p in enumerate(platform_data.get("posts", [])[:10], 1):
                print(f"    {i}. [{p.get('subreddit', '')}] {p['title']}")
                print(f"       Score: {p.get('score', 0)} | Comments: {p.get('num_comments', 0)}")
            print()

        elif platform == "google_news":
            print(f"  ── GOOGLE NEWS {'─'*52}")
            print(f"  Total articles: {platform_data.get('total_articles', 0)}")
            print(f"  Flagged articles: {platform_data.get('flagged_count', 0)}")
            print()
            for i, a in enumerate(platform_data.get("articles", [])[:10], 1):
                flags = f" ⚠ FLAGGED: {', '.join(a['flags'])}" if a.get("flags") else ""
                print(f"    {i}. {a['title']}{flags}")
                if a.get("source"):
                    print(f"       Source: {a['source']}")
            print()

        elif platform == "instagram":
            print(f"  ── INSTAGRAM {'─'*54}")
            status = platform_data.get("status", "unknown")
            if status == "skipped":
                print(f"  Status: Skipped ({platform_data.get('reason', '')})")
            else:
                for h in platform_data.get("hashtags", []):
                    count = h.get("post_count", 0)
                    count_str = f"{count:,}" if count else "N/A"
                    print(f"    {h['hashtag']}: {count_str} posts ({h.get('popularity', 'unknown')})")
            print()

        elif platform == "quora":
            print(f"  ── QUORA {'─'*58}")
            status = platform_data.get("status", "unknown")
            if status == "skipped":
                print(f"  Status: Skipped ({platform_data.get('reason', '')})")
            else:
                for i, q in enumerate(platform_data.get("questions", [])[:10], 1):
                    print(f"    {i}. {q['title']}")
            print()

    print(f"{'='*70}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="DPAP Social Media Research")
    parser.add_argument("--product", required=True, help="Product name to research")
    parser.add_argument("--platforms", default="youtube,reddit,google,instagram,quora",
                        help="Comma-separated platforms (default: all)")
    parser.add_argument("--yt-count", type=int, default=15, help="YouTube results per query (default: 15)")
    parser.add_argument("--output", choices=["json", "report"], default="json",
                        help="Output format (default: json)")

    args = parser.parse_args()
    platforms = [p.strip().lower() for p in args.platforms.split(",")]

    results = []

    if "youtube" in platforms:
        results.append(research_youtube(args.product, args.yt_count))

    if "reddit" in platforms:
        results.append(research_reddit(args.product))

    if "google" in platforms:
        results.append(research_google_news(args.product))

    if "instagram" in platforms:
        results.append(research_instagram(args.product))

    if "quora" in platforms:
        results.append(research_quora(args.product))

    if args.output == "report":
        print_report(results, args.product)
    else:
        output = {
            "product": args.product,
            "platforms": platforms,
            "generated": datetime.now().isoformat(),
            "results": results,
        }
        print(json.dumps(output, indent=2, default=str))


if __name__ == "__main__":
    main()
