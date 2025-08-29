# Email Address Verifier Scraper With Python

Allows to validate email addresses. Checks if emails are deliverable. [MapDataScraper API](https://app.mapdatascraper.cloud/api-docs#tag/Email-Related/paths/~1email-validator/get).

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
# Validate email addresses:
results = client.validate_emails(['support@mapdatascraper.com'])
```
