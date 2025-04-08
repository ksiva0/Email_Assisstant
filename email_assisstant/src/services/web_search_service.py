import requests
import streamlit as st

def maybe_search_web(context):
    query = context.get("details", {}).get("query")
    headers = {"Ocp-Apim-Subscription-Key": st.secrets["search"]["bing_api_key"]}
    params = {"q": query, "count": 3}
    response = requests.get("https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params)
    results = response.json().get("webPages", {}).get("value", [])
    return [r["snippet"] for r in results]
