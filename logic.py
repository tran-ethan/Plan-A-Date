import os
import random
import googlemaps
from geopy.geocoders import Nominatim
import pprint


def get_lat_long(postal_code):
    # Returns (latitude, longitude) based off postal code
    geolocator = Nominatim(user_agent="Hello my name is")
    location = geolocator.geocode(postal_code)
    if location is not None:
        return location.latitude, location.longitude
    else:
        return None


def get_places(gender, age, day, time, interests, location=(45.5019, -74.57),
               min_price=None, max_price=None):
    print('function called!')
    if age < 13:
        types = ["amusement_park", "aquarium", "bakery", "bowling_alley", "campground", "movie_theater", "museum",
         "park", "pet_store", "playground", "school", "toy_store", "zoo"]
    else:
        types = None
    gmaps = googlemaps.Client(key=os.environ.get('KEY'))

    places_list = []

    # GENDER
    if gender == 'other':
        gender = random.choice(['male', 'female'])
    genders = {
        'male': ["sports", "games", "laser tag", "axe throwing", "escape room", "barbequeue", "minigolf", "bowling"],
        'female': ["food festival", "karaoke", "spa", "resort", "walk", "cooking", "movie", "picnic", "pottery", "museum"]
    }
    query = random.choice(genders[gender])
    print('first query ' + query)
    results = gmaps.places(query=query, location=location, min_price=min_price, max_price=max_price, type=types)
    for result in results["results"]:
        pprint.pprint(result)
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
            "Website": url,
            "Maps": f"https://www.google.com/maps/place/?q=place_id:{place_id}",
            "Types": types
        })

    # INTERESTS
    hobbies = {
        'sports': ['football', 'basketball', 'volleyball', 'tennis', 'golf', 'swimming', 'baseball', 'hockey', 'cricket','bowling', 'minigolf'],
        'music': [x + " music" for x in ["pop", "rock", "jazz", "classical", "hip hop", "country", "blues", "electronic", "folk"]],
        'shopping': ["groceries", "clothing", "electronics", "home goods", "books", "health and beauty", "toys", "sports equipment", "pet supplies", "gifts", "office supplies", "outdoor gear"],
        'food and drinks': ["pizza", "hamburger", "sushi", "salad", "coffee", "tea", "juice", "water", "bubble tea", "restaurant", "wine tasting"],
        'entertainment': ["cinema", "movies", "comedy show"],
        'books': ["library", "bookstore", "school"]
    }
    # First interests
    hobby = random.choice(interests)
    query = random.choice(hobbies[hobby])
    print('second query' + query)

    results2 = gmaps.places(query=query, location=location, min_price=min_price, max_price=max_price, type=types)
    for result in results2["results"]:
        pprint.pprint(result)
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
            "Website": url,
            "Maps": f"https://www.google.com/maps/place/?q=place_id:{place_id}",
            "Types": types
        })

    # Filter out places that don't have time availabilities

    # Shuffle places
    random.shuffle(places_list)

    return places_list
