"""Browser skills for Nova."""

import webbrowser
from urllib.parse import quote_plus

# Frequently used websites
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://github.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "twitter": "https://twitter.com",
    "amazon": "https://amazon.in",
    "flipkart": "https://flipkart.com",
    "netflix": "https://netflix.com",
    "spotify": "https://open.spotify.com"
}


def open_website(site):
    site = site.lower().strip()

    if site in WEBSITES:
        webbrowser.open(WEBSITES[site])
        return f"Opening {site}"

    if "." not in site:
        site += ".com"

    url = f"https://{site}"

    webbrowser.open(url)

    return f"Opening {site}"


def google_search(query):

    url = f"https://www.google.com/search?q={quote_plus(query)}"

    webbrowser.open(url)

    return f"Searching Google for {query}"


def youtube_search(query):

    url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"

    webbrowser.open(url)

    return f"Searching YouTube for {query}"