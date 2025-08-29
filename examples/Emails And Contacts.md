# Emails And Contacts Scraper With Python

Allows finding email addresses, social links, and phones from domains via [MapDataScraper API](https://app.mapdatascraper.com/api-docs#tag/Emails-and-Contacts).

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
# Search contacts from website:
results = client.emails_and_contacts(['mapdatascraper.com'])
```
