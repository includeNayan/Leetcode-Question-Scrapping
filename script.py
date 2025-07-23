import requests
import json
import re
from html import unescape

def fetch_question_detail(slug):
    url = "https://leetcode.com/graphql"
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        titleSlug
        content
        difficulty
        likes
        dislikes
        exampleTestcases
        topicTags {
          name
          slug
        }
      }
    }
    """
    r = requests.post(url, json={"query": query, "variables": {"titleSlug": slug}})
    r.raise_for_status()
    return r.json()["data"]["question"]

def strip_html_and_whitespace(text: str) -> str:
    # 1) remove HTML tags
    no_tags = re.sub(r"<[^>]+>", "", text)
    # 2) unescape HTML entities
    unesc = unescape(no_tags)
    # 3) remove all newlines, carriage returns, tabs → replace with single space
    cleaned = re.sub(r"[\r\n\t]+", " ", unesc)
    # 4) collapse multiple spaces into one
    return re.sub(r" {2,}", " ", cleaned).strip()

def clean_question_data(data: dict) -> dict:
    # Clean every string field in the dict (recursive for nested structures)
    def clean_value(v):
        if isinstance(v, str):
            return strip_html_and_whitespace(v)
        if isinstance(v, list):
            return [clean_value(item) for item in v]
        if isinstance(v, dict):
            return {k: clean_value(val) for k, val in v.items()}
        return v

    # First, transform the `content` HTML→plain text
    data["content"] = strip_html_and_whitespace(data.get("content", ""))

    # Now clean the exampleTestcases too
    data["exampleTestcases"] = strip_html_and_whitespace(
        data.get("exampleTestcases", "")
    )

    # Clean topicTags names/slugs, though they probably have no whitespace
    data["topicTags"] = [
        {
            "name": strip_html_and_whitespace(tag["name"]),
            "slug": strip_html_and_whitespace(tag["slug"]),
        }
        for tag in data.get("topicTags", [])
    ]

    # Finally clean any remaining top‑level strings
    for key in ["questionId", "title", "titleSlug", "difficulty"]:
        if key in data:
            data[key] = strip_html_and_whitespace(data[key])

    return data

if __name__ == "__main__":
    slugs = [
        "substring-with-concatenation-of-all-words"
    ]

    for slug in slugs:
        print(f"→ Fetching {slug} …")
        try:
            raw = fetch_question_detail(slug)
            clean = clean_question_data(raw)
            with open(f"{slug}.json", "w", encoding="utf-8") as f:
                json.dump(clean, f, ensure_ascii=False, indent=2)
            print(f"  ✔ Saved {slug}.json")
        except Exception as e:
            print(f"  ✘ Error on {slug}: {e}")
