import os
from serpapi import GoogleSearch

def get_country_code(location: str) -> str:
    if not location:
        return "US"
    loc_lower = location.lower()
    if "india" in loc_lower:
        return "IN"
    elif "us" in loc_lower or "united states" in loc_lower:
        return "US"
    elif "uk" in loc_lower or "united kingdom" in loc_lower:
        return "GB"
    elif "canada" in loc_lower:
        return "CA"
    elif "australia" in loc_lower:
        return "AU"
    else:
        return "US"

def search_products(query, location):
    gl_code = get_country_code(location)
    params = {
        "q": query,
        "tbm": "shop",
        "location": location,
        "hl": "en",
        "gl": gl_code,
        "api_key": os.environ.get("SERP_API_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("shopping_results", [])
