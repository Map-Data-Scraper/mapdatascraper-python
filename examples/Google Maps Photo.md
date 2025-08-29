# Google Maps Photos With Python

Returns Google Maps photos from places when using search queries (e.g., restaurants, Manhattan, NY, USA) or from a single place when using IDs or names (e.g., NoMad Restaurant, NY, USA, 0x886916e8bc273979:0x5141fcb11460b226, ChIJu7bMNFV-54gR-lrHScvPRX4).
In case no photos were found by your search criteria, your search request will consume the usage of one photo.[MapDataScraper API](https://app.mapdatascraper.cloud/api-docs#tag/Google/paths/~1maps~1photos-v3/get).

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
# Get information about the places photos:
results = client.google_maps_photos(['The NoMad Restaurant, NY, USA'])
```
