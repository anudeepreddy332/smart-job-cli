from os import getenv
import requests
import time
import random
from dotenv import load_dotenv
load_dotenv()

time.sleep(random.uniform(1, 3))

def build_url(keyword, location):
    return {
        "engine": "google",
        "q": f"{keyword} jobs in {location}",
        "hl": "en",
        "api_key": getenv("SERP_API"),
        "num": 10
    }

def fetch_jobs(params, total_results=50):
    print("[INFO] Sending request to SerpAPI...")
    all_jobs = []
    start = 0

    while len(all_jobs) < total_results:
        params["start"] = start
        try:
            response = requests.get("https://serpapi.com/search", params=params, timeout=10)
            response.raise_for_status()

            results = response.json()
            organic_results = results.get("organic_results", [])

            if not organic_results:
                break

            for result in organic_results:
                title = result.get("title","")
                link = result.get("link","")
                snippet = result.get("snippet","")
                company, location ="", ""
                if " · " in snippet:
                    parts = snippet.split(" · ")
                    if len(parts) >=2:
                        company = parts[0].strip()
                        location = parts[1].strip()

                all_jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "url": link,
                })
            start += 10
            time.sleep(random.uniform(1,2))

        except requests.RequestException as e:
            print(f"[ERROR] Request failed: {e}")
            break

    return all_jobs[:total_results]