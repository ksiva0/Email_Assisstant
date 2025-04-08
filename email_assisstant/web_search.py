import requests  
import config  

def perform_web_search(query):  
    api_key = config.WEB_SEARCH_API_KEY  
    search_url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx=YOUR_CSE_ID&q={query}"  
    response = requests.get(search_url)  

    if response.status_code == 200:  
        return response.json().get("items", [])  
    else:  
        print(f"Error during web search: {response.status_code}")  
        return []  
