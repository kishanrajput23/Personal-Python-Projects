# Udemy Web Scraping 🧾

## What is this?
A small scraper that demonstrates how to collect course information from Udemy (or similar course listing pages) for learning and analysis purposes. It shows how to use `requests` and `BeautifulSoup` (or Selenium when JavaScript rendering is required).

## How it works
- The script fetches the HTML of a course listing page and parses it to extract course titles, instructors, prices, ratings, and other metadata.
- If the site uses dynamic loading, Selenium can be used to render the page before scraping.

**Main script:** `Udemy.py`

### Requirements
- Python 3.x
- `requests`, `beautifulsoup4` (`pip install requests beautifulsoup4`)
- (Optional) `selenium` and a browser driver if needed for dynamic pages

### How to run
1. Install dependencies: `pip install requests beautifulsoup4`
2. Run: `python Udemy.py`
3. The script outputs scraped data to the console or a CSV file (`udemy.csv`) when configured.

## Summary
This project demonstrates basic web scraping techniques, the importance of respecting `robots.txt`, rate-limiting, and legal/ethical considerations when scraping. Use it as a starting point to build a structured dataset for analysis, and always scrape responsibly.

