import googlemaps
import sys
from geopy.geocoders import Nominatim
import pprint


data = [{'Address': '40 R. de La Gauchetière O, Montréal, QC H2Z 1C1, Canada',
  'Hours': ['Monday: 11:00\u202fAM\u2009–\u200910:00\u202fPM',
            'Tuesday: 11:00\u202fAM\u2009–\u200910:00\u202fPM',
            'Wednesday: 11:00\u202fAM\u2009–\u200910:00\u202fPM',
            'Thursday: 11:00\u202fAM\u2009–\u200910:00\u202fPM',
            'Friday: 11:00\u202fAM\u2009–\u200910:30\u202fPM',
            'Saturday: 11:00\u202fAM\u2009–\u200910:30\u202fPM',
            'Sunday: 11:00\u202fAM\u2009–\u200910:30\u202fPM'],
  'Name': 'CoCo Fresh Tea & Juice Chinatown 都可珍珠奶茶',
  'Phone number': '(438) 771-6688',
  'Place ID': 'ChIJ5Z0OC1QbyUwRTklE42U_GSo',
  'Price level': 'No data',
  'Rating': 4,
  'Website': None},
 {'Address': '90 R. de La Gauchetière O, Montréal, QC H2Z 1C1, Canada',
  'Hours': ['Monday: 11:00\u202fAM\u2009–\u20099:30\u202fPM',
            'Tuesday: 11:00\u202fAM\u2009–\u20099:30\u202fPM',
            'Wednesday: 11:00\u202fAM\u2009–\u20099:30\u202fPM',
            'Thursday: 11:00\u202fAM\u2009–\u20099:30\u202fPM',
            'Friday: 11:00\u202fAM\u2009–\u200910:00\u202fPM',
            'Saturday: 11:00\u202fAM\u2009–\u200910:00\u202fPM',
            'Sunday: 11:00\u202fAM\u2009–\u20099:30\u202fPM'],
  'Name': 'Yi Fang Taiwan Fruit Tea Chinatown Montreal',
  'Phone number': '(514) 866-6565',
  'Place ID': 'ChIJKaa-tZ8byUwRGrUg4btwr4k',
  'Price level': 'No data',
  'Rating': 4.5,
  'Website': 'http://www.yifangquebec.com/'},
 {'Address': '71A R. de La Gauchetière O, Montréal, QC H2Z 1C2, Canada',
  'Hours': ['Monday: 11:30\u202fAM\u2009–\u200910:00\u202fPM',
            'Tuesday: 11:30\u202fAM\u2009–\u200910:00\u202fPM',
            'Wednesday: 11:30\u202fAM\u2009–\u200910:00\u202fPM',
            'Thursday: 11:30\u202fAM\u2009–\u200910:00\u202fPM',
            'Friday: 11:30\u202fAM\u2009–\u200910:30\u202fPM',
            'Saturday: 11:30\u202fAM\u2009–\u200910:30\u202fPM',
            'Sunday: 11:30\u202fAM\u2009–\u200910:00\u202fPM'],
  'Name': 'L2 Lounge',
  'Phone number': '(514) 878-0572',
  'Place ID': 'ChIJV-rdslEayUwRRcBCvcRp_-8',
  'Price level': 1,
  'Rating': 4.3,
  'Website': 'http://www.l2bubbletea.com/'},
 {'Address': '393 Rue Saint-Jacques #149, Montréal, QC H2Y 1N9, Canada',
  'Hours': ['Monday: 11:00\u202fAM\u2009–\u20098:00\u202fPM',
            'Tuesday: 11:00\u202fAM\u2009–\u20098:00\u202fPM',
            'Wednesday: 11:00\u202fAM\u2009–\u20098:00\u202fPM',
            'Thursday: 11:00\u202fAM\u2009–\u20099:00\u202fPM',
            'Friday: 11:00\u202fAM\u2009–\u20099:00\u202fPM',
            'Saturday: 11:00\u202fAM\u2009–\u20099:00\u202fPM',
            'Sunday: 11:00\u202fAM\u2009–\u20098:00\u202fPM'],
  'Name': 'Bubble Tea Shop',
  'Phone number': '(514) 288-4222',
  'Place ID': 'ChIJG1Njs2sbyUwRlglb_KzPvyo',
  'Price level': 'No data',
  'Rating': 0,
  'Website': 'https://bubbleteashop.com/?utm_source=G&utm_medium=LPM&utm_campaign=MTY'}]

def get_lat_long(postal_code):
    # Returns (latitude, longitude) based off postal code
    geolocator = Nominatim(user_agent="Hello my name is")
    location = geolocator.geocode(postal_code)
    if location is not None:
        return location.latitude, location.longitude
    else:
        return None


def get_places(search_query="bubble tea", location=(45.5019, -74.57), min_price=None, max_price=None):
    gmaps = googlemaps.Client(key='AIzaSyBZgZqccvdAkvMpA7BP-onQIGKaQwt54DM')
    results = gmaps.places(query=search_query, location=location, min_price=min_price, max_price=max_price)
    places_list = []
    for result in results["results"]:
        formatted_address = result.get("formatted_address", "No data")
        name = result.get("name", "No data")
        place_id = result.get("place_id", "No data")
        rating = result.get("rating", "No data")
        price_level = result.get("price_level", "No data")
        types = result.get("types", "No data")
        details = gmaps.place(place_id).get('result')
        hours = details.get('current_opening_hours', "No data")
        if hours != "No data":
            hours = hours.get('weekday_text', "No data")
        phone_number = details.get('formatted_phone_number')
        url = details.get('website')
        places_list.append({
            "Name": name,
            "Address": formatted_address,
            "Place ID": place_id,
            "Rating": rating,
            "Price level": price_level,
            "Hours": hours,
            "Phone number": phone_number,
            "Website": url
        })

    return places_list


coordinates = get_lat_long("H3B 4G5")
places = get_places("bubble tea", coordinates)
pprint.pprint(places)
