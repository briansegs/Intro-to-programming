import requests
r = requests.get(('https://www.metaweather.com/api/location/2459115'))
d = r.json()





# 6 items in list


#for i in d['consolidated_weather']:
#    print(i['applicable_date'])

def c_to_f(num):
    return num * 9 / 5 + 32

day = d['consolidated_weather'][0]['applicable_date']
max_t = c_to_f(d['consolidated_weather'][0]['max_temp'])
min_t = c_to_f(d['consolidated_weather'][0]['min_temp'])
the_t = c_to_f(d['consolidated_weather'][0]['the_temp'])
weather_state = d['consolidated_weather'][0]['weather_state_name']

print(f"The date for today is {day}.")
print(f"It looks like {weather_state} outside.")
print(f"The temperature is {the_t} with a high of {max_t} and a low of {min_t}.")

user_input = input("hi")
print(user_input)

