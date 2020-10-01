import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

a = requests.get(API_ROOT + API_LOCATION + "new york").json()

b = requests.get(API_ROOT + API_WEATHER + str(2459115)).json()

display_weather(b)
for i in range(6):
 
    
    day = d['consolidated_weather'][i]['applicable_date']
    max_t = round(c_to_f(d['consolidated_weather'][i]['max_temp']))
    min_t = round(c_to_f(d['consolidated_weather'][i]['min_temp']))
    the_t = round(c_to_f(d['consolidated_weather'][i]['the_temp']))
    weather_state = d['consolidated_weather'][i]['weather_state_name']



    print(f"For day {i + 1}")
    print(f"It looks like {weather_state} outside.")
    print(f"The temperature is {the_t} degrees with a high of {max_t} degrees and a low of {min_t} degrees.")
