


import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def c_to_f(num):
    return num * 9 / 5 + 32

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def display_weather(weather):
    d = weather
    day = d['consolidated_weather'][0]['applicable_date']
    max_t = round(c_to_f(d['consolidated_weather'][0]['max_temp']))
    min_t = round(c_to_f(d['consolidated_weather'][0]['min_temp']))
    the_t = round(c_to_f(d['consolidated_weather'][0]['the_temp']))
    weather_state = d['consolidated_weather'][0]['weather_state_name']

    print(f"Weather for {weather['title']} {day}:")
    print(f"It looks like {weather_state} outside.")
    print(f"The temperature is {the_t} degrees with a high of {max_t} degrees and a low of {min_t} degrees.")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

def weather_dialog():
    where = ''
    while not where:
        where = input("Where in the world are you? ")
    locations = fetch_location(where)
    if len(locations) == 0:
        print("I don't know where that is.")
    elif len(locations) > 1:
        disambiguate_locations(locations)
    else:
        woeid = locations[0]['woeid']
        display_weather(fetch_weather(woeid))


if __name__ == '__main__':
    while True:
        weather_dialog()

