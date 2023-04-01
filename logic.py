import googlemaps
import sys


from geopy.geocoders import Nominatim


def get_lat_long(postal_code):
    geolocator = Nominatim(user_agent="Hello my name is")  # Initialize geolocator with user agent
    location = geolocator.geocode(postal_code)   # Get location object from geolocator
    if location is not None:                     # Check if location was found
        return (location.latitude, location.longitude)  # Return tuple of latitude and longitude
    else:
        return None   # Return None if location was not found


gmaps = googlemaps.Client(key='AIzaSyBZgZqccvdAkvMpA7BP-onQIGKaQwt54DM')

search_query = "karaoke"
location = get_lat_long("H3B 4G5")
print(location)

radius = 40000
max_price = 100
min_price = 10
results = gmaps.places(query=search_query, location=location)


for result in results["results"]:
    formatted_address = result.get("formatted_address", "No data")
    business_status = result.get("business_status", "No data")
    name = result.get("name", "No data")
    place_id = result.get("place_id", "No data")
    rating = result.get("rating", "No data")
    price_level = result.get("price_level", "No data")
    types = result.get("types", "No data")
    icon_link = result.get("icon", "No data")
    print(f"Adress: {formatted_address}")
    print(f"Name: {name}")
    print(f"Place ID: {place_id}")
    print(f"Rating: {rating}")
    print(f"Price level: {price_level}")
    print(f"Icon link: {icon_link}")
    print("==========================================")