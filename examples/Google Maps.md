# Google Maps Scraper With Python

The library provides real-time access to the places from Google Maps via [MapDataScraper API](https://app.mapdatascraper.com/api-docs#tag/Google-Maps).
It allows easy scraping of [businesses information](https://mapdatascraper.com/google-maps-scraper/#dictionary) from Google Maps.

![screencast](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2M3OWRhZTI1NzBhNjZlNGY4NmVlOTIzNTQ3MGZhOTQyYTIzNjY0MyZjdD1n/70a8jRmg5xuTjl3yuF/giphy.gif)

## Installation

Python 3+
```bash
pip install mapdatascraper
```

[Link to the Python package page](https://pypi.org/project/mapdatascraper/)

## Initialization
```python
from mapdatascraper import ApiClient

client = ApiClient(api_key='SECRET_API_KEY')
```
[Link to the profile page to create the API key](https://app.mapdatascraper.com/profile)

## Usage

```python
# Search for businesses in specific locations:
results = client.google_maps_search(['restaurants brooklyn usa'], limit=20, language='en', region='us')

# Get data of the specific place by id
results = client.google_maps_search(['ChIJrc9T9fpYwokRdvjYRHT8nI4'], language='en')

# Scrap Places by Two Queries
results = client.google_maps_search(
    ['restaurants brooklyn usa', 'bars brooklyn usa'],
    limit=50, # limit of palces per each query
    language='en',
    region='US',
)

for query_places in results:
    for place in query_places:
        print('query:', place['query'])
        print('name:', place['name'])
        print('phone:', place['phone'])
        print('website:', place['site'])

# Scrap Places by Place Ids
results = client.google_maps_search(
    ["ChIJ8ccnM7dbwokRy-pTMsdgvS4", "ChIJN5X_gWdZwokRck9rk2guJ1M", "ChIJxWLy8DlawokR1jvfXUPSTUE"],
    limit=1, # limit of palces per each query
)

for query_places in results:
    for place in query_places:
        print('name:', place['name'])
        print('place_id:', place['place_id'])
```
