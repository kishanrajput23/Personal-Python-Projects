# Downloading Image 🖼️

## What is this?
A small tool that downloads an image from a provided URL using `requests` and saves it to disk.

**Main script:** `Download_Image.py`

### Example snippet
```python
import requests
url = input('Image URL: ')
r = requests.get(url)
open('image.jpg','wb').write(r.content)
```

### How to run
1. Install deps: `pip install requests`
2. Run: `python Download_Image.py` and enter the image URL when prompted.

## Summary
Useful for practicing HTTP requests, handling binary content and file I/O.

