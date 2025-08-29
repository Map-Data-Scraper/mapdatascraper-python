MapDataScraper Python Library
=========================

The library provides convenient access to the `MapDataScraper
API <https://app.mapdatascraper.com/api-docs>`__ from applications written
in the Python language. Allows using `MapDataScraper’s
services <https://mapdatascraper.com/services/>`__ from your code.

`API Docs <https://app.mapdatascraper.com/api-docs>`__

Installation
------------

Python 3+

.. code:: bash

   pip install mapdatascraper

`Link to the python package
page <https://pypi.org/project/mapdatascraper/>`__

Initialization
--------------

.. code:: python

   from mapdatascraper import ApiClient

   client = ApiClient(api_key='SECRET_API_KEY')

`Link to the profile page to create the API
key <https://app.mapdatascraper.com/profile>`__

Scrape Google Search
--------------------

.. code:: python

   # Google Search
   results = client.google_search('bitcoin')


Scrape Google Maps (Places)
---------------------------

.. code:: python

   # Search for businesses in specific locations:
   results = client.google_maps_search('restaurants brooklyn usa', limit=20, language='en')

   # Get data of the specific place by id
   results = client.google_maps_search('ChIJrc9T9fpYwokRdvjYRHT8nI4', language='en')

   # Search with many queries (batching)
   results = client.google_maps_search([
       'restaurants brooklyn usa',
       'bars brooklyn usa',
   ], language='en')

Scrape Google Maps Reviews
--------------------------

.. code:: python

   # Get reviews of the specific place by id
   results = client.google_maps_reviews('ChIJrc9T9fpYwokRdvjYRHT8nI4', reviews_limit=20, language='en')

   # Get reviews for places found by search query
   results = client.google_maps_reviews('Memphis Seoul brooklyn usa', reviews_limit=20, limit=500, language='en')

   # Get only new reviews during last 24 hours
   from datetime import datetime, timedelta
   yesterday_timestamp = int((datetime.now() - timedelta(1)).timestamp())

   results = client.google_maps_reviews(
       'ChIJrc9T9fpYwokRdvjYRHT8nI4', sort='newest', cutoff=yesterday_timestamp, reviews_limit=100, language='en')

Scrape Google Maps Photos
-------------------------

.. code:: python

   results = client.google_maps_photos(
       'Trump Tower, NY, USA', photosLimit=20, language='en')

Scrape Google Maps Directions
-----------------------------

.. code:: python

   results = client.google_maps_directions(['29.696596, 76.994928    30.7159662444353, 76.8053887016268', '29.696596, 76.994928    30.723065, 76.770169'])

Scrape Google Play Reviews
--------------------------

.. code:: python

   results = client.google_play_reviews(
       'com.facebook.katana', reviews_limit=20, language='en')

Emails And Contacts Scraper
---------------------------

.. code:: python

   results = client.emails_and_contacts(['mapdatascraper.com'])

`More
examples <https://github.com/mapdatascraper/mapdatascraper-python/tree/master/examples>`__

Responses examples
------------------

Google Maps Reviews response example:

.. code:: json

   {
     "name": "Memphis Seoul",
     "address": "569 Lincoln Pl, Brooklyn, NY 11238, \\u0421\\u043f\\u043e\\u043b\\u0443\\u0447\\u0435\\u043d\\u0456 \\u0428\\u0442\\u0430\\u0442\\u0438",
     "address_street": "569 Lincoln Pl",
     "address_borough": "\\u041a\\u0440\\u0430\\u0443\\u043d-\\u0413\\u0430\\u0439\\u0442\\u0441",
     "address_city": "Brooklyn",
     "time_zone": "America/New_York",
     "type": "\\u0420\\u0435\\u0441\\u0442\\u043e\\u0440\\u0430\\u043d",
     "types": "\\u0420\\u0435\\u0441\\u0442\\u043e\\u0440\\u0430\\u043d",
     "postal_code": "11238",
     "latitude": 40.6717258,
     "longitude": -73.9579098,
     "phone": "+1 347-349-2561",
     "rating": 3.9,
     "reviews": 32,
     "site": "http://www.getmemphisseoul.com/",
     "photos_count": 77,
     "google_id": "0x89c25bb5950fc305:0x330a88bf1482581d",
     "reviews_link": "https://www.google.com/search?q=Memphis+Seoul,+569+Lincoln+Pl,+Brooklyn,+NY+11238,+%D0%A1%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D1%96+%D0%A8%D1%82%D0%B0%D1%82%D0%B8&ludocid=3677902399965648925#lrd=0x89c25bb5950fc305:0x330a88bf1482581d,1",
     "reviews_id": "3677902399965648925",
     "photo": "https://lh5.googleusercontent.com/p/X_6-QqMphC_ctqs3bHSqFg",
     "working_hours": "\\u0432\\u0456\\u0432\\u0442\\u043e\\u0440\\u043e\\u043a: 16:00\\u201322:00 | \\u0441\\u0435\\u0440\\u0435\\u0434\\u0430: 16:00\\u201322:00 | \\u0447\\u0435\\u0442\\u0432\\u0435\\u0440: 16:00\\u201322:00 | \\u043f\\u02bc\\u044f\\u0442\\u043d\\u0438\\u0446\\u044f: 16:00\\u201322:00 | \\u0441\\u0443\\u0431\\u043e\\u0442\\u0430: 16:00\\u201322:00 | \\u043d\\u0435\\u0434\\u0456\\u043b\\u044f: 16:00\\u201322:00 | \\u043f\\u043e\\u043d\\u0435\\u0434\\u0456\\u043b\\u043e\\u043a: 16:00\\u201322:00",
     "reviews_per_score": "1: 6, 2: 0, 3: 4, 4: 3, 5: 19",
     "verified": true,
     "reserving_table_link": null,
     "booking_appointment_link": null,
     "owner_id": "100347822687163365487",
     "owner_link": "https://www.google.com/maps/contrib/100347822687163365487",
     "reviews_data": [
       {
         "google_id": "0x89c25bb5950fc305:0x330a88bf1482581d",
         "autor_link": "https://www.google.com/maps/contrib/112314095435657473333?hl=en-US",
         "autor_name": "Eliott Levy",
         "autor_id": "112314095435657473333",
         "review_text": "Very good local comfort fusion food ! \\nKimchi coleslaw !! Such an amazing idea !",
         "review_link": "https://www.google.com/maps/reviews/data=!4m5!14m4!1m3!1m2!1s112314095435657473333!2s0x0:0x330a88bf1482581d?hl=en-US",
         "review_rating": 5,
         "review_timestamp": 1560692128,
         "review_datetime_utc": "06/16/2019 13:35:28",
         "review_likes": null
       },
       {
         "google_id": "0x89c25bb5950fc305:0x330a88bf1482581d",
         "autor_link": "https://www.google.com/maps/contrib/106144075337788507031?hl=en-US",
         "autor_name": "fenwar1",
         "autor_id": "106144075337788507031",
         "review_text": "Great wings with several kinds of hot sauce. The mac and cheese ramen is excellent.\\nUPDATE:\\nReturned later to try the meatloaf slider, a thick meaty slice  topped with slaw and a fantastic sauce- delicious. \\nConsider me a regular.\\ud83d\\udc4d",
         "review_link": "https://www.google.com/maps/reviews/data=!4m5!14m4!1m3!1m2!1s106144075337788507031!2s0x0:0x330a88bf1482581d?hl=en-US",
         "review_rating": 5,
         "review_timestamp": 1571100055,
         "review_datetime_utc": "10/15/2019 00:40:55",
         "review_likes": null
       },
       ...
     ]
   }

Emails & Contacts Scraper response example:

.. code:: json

   [
       {
         "query": "mapdatascraper.com",
         "domain": "mapdatascraper.com",
         "emails": [
           {
             "value": "service@mapdatascraper.com",
             "sources": [
               {
                 "ref": "https://mapdatascraper.com/",
                 "extracted_on": "2021-09-27T07:45:30.386000",
                 "updated_on": "2021-11-18T12:59:15.602000"
               },
             ...
             ]
           },
           {
             "value": "support@mapdatascraper.com",
             "sources": [
               {
                 "ref": "https://mapdatascraper.com/privacy-policy/",
                 "extracted_on": "2021-11-18T12:51:39.716000",
                 "updated_on": "2021-11-18T12:51:39.716000"
               }
             ]
           }
         ],
         "phones": [
           {
             "value": "12812368208",
             "sources": [
               {
                 "ref": "https://mapdatascraper.com/",
                 "extracted_on": "2021-11-18T12:59:15.602000",
                 "updated_on": "2021-11-18T12:59:15.602000"
               },
               ...
             ]
           }
         ],
         "socials": {
           "facebook": "https://www.facebook.com/mapdatascraper/",
           "github": "https://github.com/mapdatascraper",
           "linkedin": "https://www.linkedin.com/company/mapdatascraper/",
           "twitter": "https://twitter.com/mapdatascraper",
           "whatsapp": "https://wa.me/12812368208",
           "youtube": "https://www.youtube.com/channel/UCDYOuXSEenLpt5tKNq-0l9Q"
         },
         "site_data": {
           "description": "Scrape Google Maps Places, Business Reviews, Photos, Play Market Reviews, and more. Get any public data from the internet by applying cutting-edge technologies.",
           "generator": "WordPress 5.8.2",
           "title": "MapDataScraper - get any public data from the internet"
         }
       }
     ]

Contributing
------------

Bug reports and pull requests are welcome on GitHub at
https://github.com/mapdatascraper/mapdatascraper-python.
