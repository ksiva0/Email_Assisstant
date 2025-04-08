import requests
import os

def search_web(query: str):
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    cx = os.getenv("GOOGLE_SEARCH_ENGINE_ID")  # Your Google Custom Search Engine ID
    endpoint = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
    }

    response = requests.get(endpoint, params=params)
    response.raise_for_status()  # raise error for bad status

    results = response.json()

    # Optional: Extract top 3 search result links and titles
    search_results = []
    for item in results.get("items", [])[:3]:
        search_results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet"),
        })

    return search_results
