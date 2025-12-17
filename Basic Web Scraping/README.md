# Basic Web Scraping 🕸️

## What is this?
A minimal project that shows how to fetch HTML pages and extract information using `requests` and `BeautifulSoup`.

## How it works
- Use `requests` to download page HTML.
- Parse the HTML with `BeautifulSoup` to find tags and extract text or attributes.

**Main script:** `basic web scraping.py`

### Example (snippet)
```python
import requests
from bs4 import BeautifulSoup

r = requests.get('https://example.com')
soup = BeautifulSoup(r.text, 'html.parser')
for h in soup.select('h2'):
    print(h.get_text())
```

### How to run
1. Install deps: `pip install requests beautifulsoup4`
2. Run: `python "basic web scraping.py"`

## Summary
Good starter project for learning HTTP requests, parsing HTML and handling network-related issues (timeouts, headers, robots). Always respect a site’s `robots.txt` and usage policies.

