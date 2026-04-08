#!/usr/bin/env python3
"""DPAP Research Pipeline for BabyOrgano.

Data-driven Product Acceptance Protocol — 6-step product validation.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from urllib.parse import quote_plus

# ── Brand Configuration ──────────────────────────────────────────────────────

BRAND = {
    "name": "BabyOrgano",
    "category": "Ayurvedic Kids Health & Wellness, India",
    "competitors": [
        "MamaEarth Kids", "Himalaya Baby", "Dabur Honitus",
        "Baidyanath Kids", "The Moms Co", "SattvikBaby",
        "Carbamide Forte Kids", "Wellbeing Nutrition Kids",
        "Pediasure", "Zandu Baby",
    ],
    "price_range": "Rs 300-900",
    "formats": ["Drops", "Gummies", "Syrup", "Chewable tablets", "Powder"],
    "benchmarks": {
        "min_avg_rating": 3.8,
        "min_buying_intent_pct": 50,
        "trend_direction": ["stable", "increasing"],
    },
    "signoff_team": [
        {"name": "Dr. Urvi", "role": "R&D"},
        {"name": "Sneha", "role": "Marketing"},
        {"name": "Ripul Sharma", "role": "Founder"},
        {"name": "Riddhi Sharma", "role": "Founder"},
        {"name": "Ghazal", "role": "CS"},
    ],
}

INGREDIENT_MAP = {
    "immunity": ["Tulsi", "Giloy", "Amla", "Ashwagandha", "Neem", "Turmeric"],
    "growth": ["Ashwagandha", "Shatavari", "Bala", "Amalaki", "Brahmi"],
    "digestion": ["Triphala", "Ajwain", "Fennel", "Ginger", "Haritaki"],
    "brain": ["Brahmi", "Shankhpushpi", "Ashwagandha", "Vacha"],
    "sleep": ["Ashwagandha", "Brahmi", "Jatamansi", "Tagara"],
    "nutrition": ["Amla", "Shatavari", "Moringa", "Ashwagandha", "Amalaki"],
}

CATEGORY_KEYWORDS = {
    "immunity": ["immunity", "immune", "cold", "cough", "flu", "fever", "infection"],
    "growth": ["growth", "height", "weight", "grow", "tall", "strength"],
    "digestion": ["digestion", "digest", "stomach", "gut", "constipation", "appetite"],
    "brain": ["brain", "memory", "focus", "concentration", "cognitive", "smart"],
    "sleep": ["sleep", "calm", "relax", "night", "insomnia", "restless"],
    "nutrition": ["nutrition", "vitamin", "mineral", "supplement", "multivitamin", "nourish"],
}

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9",
}
# ── STEP 1: Google Trends ─────────────────────────────────────────────────────

def step_trends(product):
    """Analyze Google Trends data for the product."""
    result = {"step": "trends", "status": "pending", "passed": False, "data": {}}

    try:
        from pytrends.request import TrendReq
    except ImportError:
        result["status"] = "error"
        result["error"] = "pytrends not installed. Run: pip install pytrends"
        return result

    last_word = product.strip().split()[-1]
    keywords = [
        product,
        f"ayurvedic {last_word} for kids",
        f"{BRAND['competitors'][0]} kids",
    ]
    # pytrends max 5 keywords
    keywords = keywords[:5]

    try:
        pytrends = TrendReq(hl="en-IN", tz=330)

        # 12-month interest
        pytrends.build_payload(keywords[:3], cat=0, timeframe="today 12-m", geo="IN")
        iot = pytrends.interest_over_time()

        twelve_month = {}
        if not iot.empty and product in iot.columns:
            values = iot[product].tolist()
            avg_interest = sum(values) / len(values) if values else 0
            # Seasonal spikes
            spikes = []
            for i, val in enumerate(values):
                if val > avg_interest * 1.3:
                    spikes.append({"index": i, "value": int(val)})
            # Direction: compare last 3 months to overall
            last_3 = values[-12:] if len(values) >= 12 else values[-3:]
            last_3_avg = sum(last_3) / len(last_3) if last_3 else 0
            if last_3_avg > avg_interest * 1.1:
                direction = "increasing"
            elif last_3_avg < avg_interest * 0.9:
                direction = "declining"
            else:
                direction = "stable"
            twelve_month = {
                "avg_interest": round(avg_interest, 1),
                "max_interest": max(values) if values else 0,
                "direction": direction,
                "seasonal_spikes": len(spikes),
                "spike_details": spikes[:5],
            }

        # 5-year trend
        five_year = {}
        try:
            pytrends.build_payload([product], cat=0, timeframe="today 5-y", geo="IN")
            iot5 = pytrends.interest_over_time()
            if not iot5.empty and product in iot5.columns:
                vals5 = iot5[product].tolist()
                five_year = {
                    "avg_interest": round(sum(vals5) / len(vals5), 1) if vals5 else 0,
                    "current_vs_peak": round(vals5[-1] / max(vals5) * 100, 1) if vals5 and max(vals5) > 0 else 0,
                }
        except Exception:
            five_year = {"error": "Could not fetch 5-year data"}

        # Regional interest
        regions = {}
        try:
            pytrends.build_payload([product], cat=0, timeframe="today 12-m", geo="IN")
            ibr = pytrends.interest_by_region(resolution="REGION", inc_low_vol=True)
            if not ibr.empty:
                top = ibr[product].sort_values(ascending=False).head(5)
                regions = {k: int(v) for k, v in top.items()}
        except Exception:
            regions = {"error": "Could not fetch regional data"}

        direction = twelve_month.get("direction", "unknown")
        avg = twelve_month.get("avg_interest", 0)
        passed = direction in ["stable", "increasing"] and avg >= 10

        result["data"] = {
            "keywords": keywords,
            "twelve_month": twelve_month,
            "five_year": five_year,
            "top_regions": regions,
        }
        result["status"] = "completed"
        result["passed"] = passed
        result["summary"] = f"Direction: {direction}, Avg interest: {avg}"

    except Exception as e:
        result["status"] = "error"
        result["error"] = f"Google Trends error (likely rate limited): {str(e)}"

    return result
# ── STEP 2: Amazon India ──────────────────────────────────────────────────────

def step_amazon(product):
    """Scrape Amazon India search results for the product."""
    result = {"step": "amazon", "status": "pending", "passed": False, "data": {}}

    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        result["status"] = "error"
        result["error"] = "requests/beautifulsoup4 not installed"
        return result

    ayurvedic_keywords = ["ayur", "herbal", "natural", "organic", "tulsi", "ashwa"]
    url = f"https://www.amazon.in/s?k={quote_plus(product)}&i=hpc"

    try:
        resp = requests.get(url, headers=HTTP_HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")

        cards = soup.select('[data-component-type="s-search-result"]')
        listings = []
        ratings = []
        ayurvedic_count = 0

        for card in cards[:30]:
            title_el = card.select_one("h2 a span") or card.select_one("h2 span")
            title = title_el.get_text(strip=True) if title_el else ""

            rating_el = card.select_one("span.a-icon-alt")
            rating_text = rating_el.get_text(strip=True) if rating_el else ""
            rating = 0.0
            if rating_text:
                m = re.search(r'(\d+\.?\d*)', rating_text)
                if m:
                    rating = float(m.group(1))

            review_el = card.select_one('span[aria-label*="rating"]')
            reviews = 0
            if review_el:
                m = re.search(r'(\d[\d,]*)', review_el.get_text())
                if m:
                    reviews = int(m.group(1).replace(",", ""))

            price_el = card.select_one("span.a-price .a-offscreen")
            price = price_el.get_text(strip=True) if price_el else ""

            link_el = card.select_one("h2 a")
            link = "https://www.amazon.in" + link_el["href"] if link_el and link_el.get("href") else ""

            is_ayurvedic = any(kw in title.lower() for kw in ayurvedic_keywords)
            if is_ayurvedic:
                ayurvedic_count += 1

            if title:
                listing = {
                    "title": title[:100],
                    "rating": rating,
                    "reviews": reviews,
                    "price": price,
                    "url": link[:150],
                    "is_ayurvedic": is_ayurvedic,
                }
                listings.append(listing)
                if rating > 0:
                    ratings.append(rating)

        avg_rating = round(sum(ratings) / len(ratings), 2) if ratings else 0
        total = len(listings)

        # Gap analysis
        gaps = []
        if avg_rating < 4.2:
            gaps.append("Quality gap — BabyOrgano can differentiate on formulation")
        if total < 15:
            gaps.append("Under-served market — first mover Ayurvedic advantage")
        if ayurvedic_count < 3:
            gaps.append("Clear Ayurvedic white space on Amazon")

        passed = avg_rating >= BRAND["benchmarks"]["min_avg_rating"]

        result["data"] = {
            "total_listings": total,
            "avg_rating": avg_rating,
            "ayurvedic_listings": ayurvedic_count,
            "top_listings": listings[:10],
            "gap_analysis": gaps,
        }
        result["status"] = "completed"
        result["passed"] = passed
        result["summary"] = f"{total} listings, avg rating {avg_rating}, {ayurvedic_count} Ayurvedic, {len(gaps)} gaps found"

    except Exception as e:
        result["status"] = "error"
        result["error"] = f"Amazon scraping error: {str(e)}"

    return result
# ── STEP 3: E-commerce & Marketplace Presence ─────────────────────────────────

def step_ecommerce(product):
    """Check Flipkart and other marketplace presence."""
    result = {"step": "ecommerce", "status": "pending", "passed": False, "data": {}}

    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        result["status"] = "error"
        result["error"] = "requests/beautifulsoup4 not installed"
        return result

    # Flipkart
    flipkart_data = {"listings": [], "total": 0}
    try:
        fk_url = f"https://www.flipkart.com/search?q={quote_plus(product)}"
        resp = requests.get(fk_url, headers=HTTP_HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")
        cards = soup.select("div._1AtVbE") or soup.select("div[data-id]")
        for card in cards[:15]:
            title_el = card.select_one("div._4rR01T") or card.select_one("a.s1Q9rs") or card.select_one("a[title]")
            title = title_el.get_text(strip=True) if title_el else ""
            rating_el = card.select_one("div._3LWZlK")
            rating = rating_el.get_text(strip=True) if rating_el else ""
            price_el = card.select_one("div._30jeq3") or card.select_one("div._25b18c div:first-child")
            price = price_el.get_text(strip=True) if price_el else ""
            if title:
                flipkart_data["listings"].append({"title": title[:100], "rating": rating, "price": price})
        flipkart_data["total"] = len(flipkart_data["listings"])
    except Exception as e:
        flipkart_data["error"] = str(e)

    # Marketplace presence checks
    marketplaces = {
        "Nykaa": f"https://www.nykaa.com/search/result/?q={quote_plus(product)}",
        "FirstCry": f"https://www.firstcry.com/search?q={quote_plus(product)}",
        "Apollo Pharmacy": f"https://www.apollopharmacy.in/search-medicines/{quote_plus(product)}",
        "1mg": f"https://www.1mg.com/search/all?name={quote_plus(product)}",
        "PharmEasy": f"https://pharmeasy.in/search/all?name={quote_plus(product)}",
    }

    quick_commerce = {
        "Blinkit": f"https://blinkit.com/s/?q={quote_plus(product)}",
        "Zepto": f"https://www.zeptonow.com/search?query={quote_plus(product)}",
        "Swiggy Instamart": f"https://www.swiggy.com/instamart/search?query={quote_plus(product)}",
    }

    presence = {}
    for name, url in {**marketplaces, **quick_commerce}.items():
        try:
            resp = requests.get(url, headers=HTTP_HEADERS, timeout=10, allow_redirects=True)
            has_results = resp.status_code == 200 and len(resp.text) > 5000
            presence[name] = {"url": url, "available": has_results}
        except Exception:
            presence[name] = {"url": url, "available": False, "error": "Connection failed"}

    available_count = sum(1 for v in presence.values() if v.get("available"))
    passed = flipkart_data["total"] > 0 or available_count >= 2

    result["data"] = {
        "flipkart": flipkart_data,
        "marketplace_presence": presence,
        "available_on": available_count,
        "total_checked": len(presence),
    }
    result["status"] = "completed"
    result["passed"] = passed
    result["summary"] = f"Flipkart: {flipkart_data['total']} listings, {available_count}/{len(presence)} marketplaces available"

    return result
# ── STEP 4: Kids & Ayurvedic Wellness Assessment ──────────────────────────────

def detect_category(product):
    """Detect product category from keywords."""
    product_lower = product.lower()
    scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in product_lower)
        if score > 0:
            scores[cat] = score
    if scores:
        return max(scores, key=scores.get)
    return "immunity"  # default


def step_kids_assessment(product):
    """Kids & Ayurvedic wellness assessment (logic-based, no scraping)."""
    result = {"step": "kids", "status": "pending", "passed": False, "data": {}}

    category = detect_category(product)
    ingredients = INGREDIENT_MAP.get(category, INGREDIENT_MAP["immunity"])

    age_groups = {
        "0-2 years (Toddlers)": "Drops or liquid formulations preferred. Parental supervision essential.",
        "2-5 years (Preschool)": "Syrup or flavored drops. Taste is critical for compliance.",
        "5-12 years (School age)": "Gummies, chewable tablets, or flavored powder. Fun factor matters.",
    }

    parental_concerns = {
        "immunity": ["Frequent infections", "Seasonal illness", "Antibiotic dependency", "School absences"],
        "growth": ["Below-average height/weight", "Poor appetite", "Delayed milestones", "Nutritional gaps"],
        "digestion": ["Constipation", "Poor appetite", "Stomach pain", "Food sensitivities"],
        "brain": ["Poor concentration", "Academic performance", "Screen time effects", "Memory issues"],
        "sleep": ["Difficulty falling asleep", "Night waking", "Screen time before bed", "Restlessness"],
        "nutrition": ["Picky eating", "Nutritional deficiencies", "Low energy", "Iron/vitamin gaps"],
    }

    purchase_triggers = [
        "Doctor/pediatrician recommendation",
        "Other parent recommendation",
        "Visible symptoms in child",
        "Seasonal change (monsoon/winter)",
        "Social media influence",
        "School health advisory",
    ]

    problem_statement = {
        "immunity": f"Indian parents struggle with frequent childhood illnesses, seeking safe Ayurvedic alternatives to synthetic immunity boosters for children aged 0-12.",
        "growth": f"Parents are concerned about optimal growth and development, looking for natural Ayurvedic solutions to support height, weight, and overall physical development.",
        "digestion": f"Digestive issues in children are common and parents prefer gentle, Ayurvedic remedies over harsh chemical alternatives.",
        "brain": f"With increasing academic pressure and screen time, parents seek natural Ayurvedic brain health support for improved focus and memory.",
        "sleep": f"Sleep disruption in children affects the whole family. Parents want safe, natural Ayurvedic solutions for better sleep quality.",
        "nutrition": f"Picky eating and nutritional gaps worry parents who prefer Ayurvedic supplementation over synthetic multivitamins.",
    }

    positioning = (
        f"BabyOrgano {product} — Trusted Ayurvedic {category} support for children, "
        f"formulated with {', '.join(ingredients[:3])} and other time-tested ingredients. "
        f"FSSAI-approved, pediatrician-reviewed, and made specifically for Indian children "
        f"aged 0-12. Priced at {BRAND['price_range']} for accessible wellness."
    )

    result["data"] = {
        "detected_category": category,
        "recommended_ingredients": ingredients,
        "problem_statement": problem_statement.get(category, problem_statement["immunity"]),
        "target_age_groups": age_groups,
        "parental_concerns": parental_concerns.get(category, parental_concerns["immunity"]),
        "purchase_triggers": purchase_triggers,
        "babyorgano_positioning": positioning,
    }
    result["status"] = "completed"
    result["passed"] = True  # Always passes — it's an assessment
    result["summary"] = f"Category: {category}, Ingredients: {', '.join(ingredients[:3])}"

    return result


# ── STEP 5: Customer Survey ───────────────────────────────────────────────────

def step_survey(product):
    """Generate a 7-question customer survey for the product."""
    result = {"step": "survey", "status": "pending", "passed": False, "data": {}}

    category = detect_category(product)

    survey = {
        "title": f"BabyOrgano {product.title()} — Customer Research Survey",
        "owner": "Ghazal (CS)",
        "target_responses": 100,
        "buying_intent_benchmark": "50% positive on Q3",
        "questions": [
            {
                "q": 1,
                "text": f"How aware are you of current {category} products for children?",
                "options": ["Very aware", "Somewhat aware", "Not aware"],
                "type": "single_choice",
            },
            {
                "q": 2,
                "text": f"How severe is the {category} problem for your child?",
                "options": ["Critical — affects daily life", "Moderate — occasional concern", "Mild — rarely an issue", "Not an issue"],
                "type": "single_choice",
            },
            {
                "q": 3,
                "text": f"Would you buy a BabyOrgano {product} if available?",
                "options": ["Definitely yes", "Probably yes", "Maybe", "Unlikely", "Never"],
                "type": "single_choice",
                "benchmark": ">= 50% selecting Definitely or Probably",
                "is_key_metric": True,
            },
            {
                "q": 4,
                "text": "What price range is acceptable for a monthly supply?",
                "options": ["Under Rs 300", "Rs 300-500", "Rs 500-700", "Rs 700-900", "Above Rs 900"],
                "type": "single_choice",
            },
            {
                "q": 5,
                "text": "What product format do you prefer for your child?",
                "options": ["Drops", "Gummies", "Syrup", "Chewable tablets", "Powder"],
                "type": "single_choice",
            },
            {
                "q": 6,
                "text": "What would make you trust a new Ayurvedic kids brand?",
                "options": [
                    "Doctor/pediatrician recommendation",
                    "FSSAI/AYUSH certifications",
                    "Transparent ingredient list",
                    "Positive parent reviews",
                    "Established brand reputation",
                ],
                "type": "multi_choice",
            },
            {
                "q": 7,
                "text": "What is your main objection to trying a new product?",
                "options": ["Price too high", "Safety concerns", "Unsure about effectiveness", "Not easily available", "Already using something that works"],
                "type": "single_choice",
            },
        ],
        "call_script_notes": [
            "Introduce yourself: 'Hi, I'm calling from BabyOrgano. We're researching parents' needs for children's wellness.'",
            "Keep calls under 5 minutes",
            "Record verbatim responses to open-ended follow-ups",
            f"Target: parents of children 0-12 in metro + tier-2 Indian cities",
            "Offer: 'As a thank you, we'll send you a free sample when the product launches'",
        ],
    }

    result["data"] = survey
    result["status"] = "completed"
    result["passed"] = True  # Survey generation always passes
    result["summary"] = f"7-question survey generated, owner: Ghazal (CS), benchmark: 50% buying intent"

    return result
# ── STEP 6: Social Media Research ─────────────────────────────────────────────

def step_social(product, yt_count=10):
    """Run social media research via dpap_social_research.py subprocess."""
    result = {"step": "social", "status": "pending", "passed": False, "data": {}}

    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dpap_social_research.py")

    if os.path.exists(script_path):
        try:
            cmd = [
                sys.executable, script_path,
                "--product", product,
                "--platforms", "youtube,reddit,google",
                "--yt-count", str(yt_count),
                "--output", "json",
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if proc.returncode == 0 and proc.stdout.strip():
                social_data = json.loads(proc.stdout)
                result["data"] = social_data
                result["status"] = "completed"
                result["passed"] = True
                result["summary"] = f"Social research completed across {len(social_data.get('results', []))} platforms"
                return result
        except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception) as e:
            result["data"]["subprocess_error"] = str(e)

    # Fallback: yt-dlp only
    try:
        search_query = f"ytsearch{yt_count}:{product}"
        cmd = [sys.executable, "-m", "yt_dlp", search_query, "--dump-json", "--no-download", "--no-warnings", "--flat-playlist"]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        videos = []
        for line in proc.stdout.strip().split("\n"):
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                videos.append({
                    "title": data.get("title", ""),
                    "channel": data.get("channel", data.get("uploader", "")),
                    "views": data.get("view_count", 0),
                    "url": data.get("url", data.get("webpage_url", "")),
                })
            except json.JSONDecodeError:
                continue
        result["data"] = {"fallback": True, "youtube_videos": videos}
        result["status"] = "completed"
        result["passed"] = len(videos) > 0
        result["summary"] = f"YouTube fallback: {len(videos)} videos found"
    except Exception as e:
        result["status"] = "error"
        result["error"] = f"Social research failed: {str(e)}"

    return result


# ── Report Generation ─────────────────────────────────────────────────────────

def generate_recommendation(step_results):
    """Generate PROCEED/CONDITIONAL/REJECT recommendation."""
    passed = sum(1 for r in step_results if r.get("passed"))
    total = len(step_results)

    if passed >= 4:
        recommendation = "PROCEED"
        rationale = f"{passed}/{total} steps passed. Market signals are favorable for BabyOrgano entry."
    elif passed >= 2:
        recommendation = "CONDITIONAL"
        rationale = f"{passed}/{total} steps passed. Proceed with caution — address failing steps before launch."
    else:
        recommendation = "REJECT"
        rationale = f"Only {passed}/{total} steps passed. Market conditions are not favorable. Re-evaluate product concept."

    checklist = []
    pending_actions = []
    for r in step_results:
        step_name = r.get("step", "unknown")
        status = "PASS" if r.get("passed") else "FAIL"
        if r.get("status") == "error":
            status = "ERROR"
        checklist.append(f"[{status}] Step: {step_name} — {r.get('summary', 'No summary')}")
        if not r.get("passed"):
            pending_actions.append(f"Review and address: {step_name} ({r.get('summary', r.get('error', 'Failed'))})")

    if not pending_actions:
        pending_actions.append("All steps passed — proceed to sign-off")

    return {
        "recommendation": recommendation,
        "rationale": rationale,
        "passed": passed,
        "total": total,
        "checklist": checklist,
        "pending_actions": pending_actions,
        "signoff_required": [f"{p['name']} ({p['role']})" for p in BRAND["signoff_team"]],
    }


def print_report(product, step_results, recommendation):
    """Print formatted text report."""
    rec = recommendation
    print(f"\n{'='*70}")
    print(f"  DPAP RESEARCH REPORT: \"{product}\"")
    print(f"  Brand: {BRAND['name']} | Category: {BRAND['category']}")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}")

    # Recommendation first
    print(f"\n  {'*'*60}")
    marker = {"PROCEED": ">>", "CONDITIONAL": "!!", "REJECT": "XX"}
    print(f"  {marker.get(rec['recommendation'], '--')} RECOMMENDATION: {rec['recommendation']}")
    print(f"  {rec['rationale']}")
    print(f"  {'*'*60}\n")

    # Step results
    for r in step_results:
        step = r.get("step", "unknown").upper()
        status = r.get("status", "unknown")
        passed = "PASS" if r.get("passed") else "FAIL"
        if status == "error":
            passed = "ERROR"

        print(f"  ── STEP: {step} [{passed}] {'─' * (50 - len(step))}")
        print(f"  Status: {status}")
        if r.get("summary"):
            print(f"  Summary: {r['summary']}")
        if r.get("error"):
            print(f"  Error: {r['error']}")

        data = r.get("data", {})

        if r["step"] == "trends":
            tm = data.get("twelve_month", {})
            if tm:
                print(f"  Direction: {tm.get('direction', 'N/A')}")
                print(f"  Avg Interest: {tm.get('avg_interest', 'N/A')}")
                print(f"  Seasonal Spikes: {tm.get('seasonal_spikes', 0)}")
            regions = data.get("top_regions", {})
            if regions and not isinstance(regions, str):
                print(f"  Top Regions: {', '.join(f'{k}: {v}' for k, v in list(regions.items())[:5])}")

        elif r["step"] == "amazon":
            print(f"  Total Listings: {data.get('total_listings', 0)}")
            print(f"  Avg Rating: {data.get('avg_rating', 0)}")
            print(f"  Ayurvedic Listings: {data.get('ayurvedic_listings', 0)}")
            gaps = data.get("gap_analysis", [])
            if gaps:
                print(f"  Gap Analysis:")
                for g in gaps:
                    print(f"    - {g}")

        elif r["step"] == "ecommerce":
            fk = data.get("flipkart", {})
            print(f"  Flipkart Listings: {fk.get('total', 0)}")
            print(f"  Marketplaces Available: {data.get('available_on', 0)}/{data.get('total_checked', 0)}")

        elif r["step"] == "kids":
            print(f"  Category: {data.get('detected_category', 'N/A')}")
            print(f"  Ingredients: {', '.join(data.get('recommended_ingredients', []))}")
            print(f"  Positioning: {data.get('babyorgano_positioning', 'N/A')[:150]}...")

        elif r["step"] == "survey":
            survey = data
            print(f"  Survey: {survey.get('title', 'N/A')}")
            print(f"  Owner: {survey.get('owner', 'N/A')}")
            print(f"  Benchmark: {survey.get('buying_intent_benchmark', 'N/A')}")
            for q in survey.get("questions", []):
                key = " [KEY METRIC]" if q.get("is_key_metric") else ""
                print(f"    Q{q['q']}: {q['text']}{key}")
                print(f"        Options: {' / '.join(q['options'])}")

        elif r["step"] == "social":
            if data.get("fallback"):
                print(f"  (YouTube fallback mode)")
                vids = data.get("youtube_videos", [])
                for v in vids[:5]:
                    print(f"    - {v.get('title', '')} ({v.get('views', 0)} views)")
            else:
                for platform_data in data.get("results", []):
                    platform = platform_data.get("platform", "")
                    print(f"    Platform: {platform}")

        print()

    # Checklist
    print(f"  ── CHECKLIST {'─'*54}")
    for item in rec["checklist"]:
        print(f"    {item}")
    print()

    # Pending actions
    print(f"  ── PENDING ACTIONS {'─'*48}")
    for action in rec["pending_actions"]:
        print(f"    - {action}")
    print()

    # Sign-off
    print(f"  ── SIGN-OFF REQUIRED {'─'*46}")
    for person in rec["signoff_required"]:
        print(f"    [ ] {person}")
    print()
    print(f"{'='*70}\n")


# ── Main ──────────────────────────────────────────────────────────────────────

ALL_STEPS = ["trends", "amazon", "ecommerce", "kids", "survey", "social"]

STEP_FUNCTIONS = {
    "trends": step_trends,
    "amazon": step_amazon,
    "ecommerce": step_ecommerce,
    "kids": step_kids_assessment,
    "survey": step_survey,
}


def main():
    parser = argparse.ArgumentParser(description="DPAP Research Pipeline for BabyOrgano")
    parser.add_argument("--product", required=True, help="Product name to research")
    parser.add_argument("--steps", default="all", help="Steps to run: 'all' or comma-separated (trends,amazon,ecommerce,kids,survey,social)")
    parser.add_argument("--output", choices=["json", "report"], default="report", help="Output format")
    parser.add_argument("--yt-count", type=int, default=10, help="YouTube results count")

    args = parser.parse_args()

    if args.steps == "all":
        steps_to_run = ALL_STEPS
    else:
        steps_to_run = [s.strip() for s in args.steps.split(",")]

    step_results = []

    for step_name in steps_to_run:
        if step_name == "social":
            r = step_social(args.product, args.yt_count)
        elif step_name in STEP_FUNCTIONS:
            r = STEP_FUNCTIONS[step_name](args.product)
        else:
            r = {"step": step_name, "status": "error", "passed": False, "error": f"Unknown step: {step_name}"}
        step_results.append(r)

    rec = generate_recommendation(step_results)

    if args.output == "json":
        output = {
            "product": args.product,
            "brand": BRAND["name"],
            "generated": datetime.now().isoformat(),
            "recommendation": rec,
            "steps": step_results,
        }
        print(json.dumps(output, indent=2, default=str))
    else:
        print_report(args.product, step_results, rec)


if __name__ == "__main__":
    main()
