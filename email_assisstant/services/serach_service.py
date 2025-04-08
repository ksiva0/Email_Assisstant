import requests
import os

def search_web(query: str):
    api_key = os.getenv("BING_API_KEY")
    endpoint = f"https://api.bing.microsoft.com/v7.0/search?q={query}"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    response = requests.get(endpoint, headers=headers)
    return response.json()
