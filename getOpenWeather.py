# Feteching weather information from openweathermap.org
# print weather for a particular location

import sys,requests,json

APP_ID = "YOUR API KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

'''if len(sys.argv) < 2:

    print('Usage : getOpenWeathet.py city_name,2-letter-country-code')

    sys.exit()

location = ''.join(sys.argv[1:])'''

location_ = "Dhaka,Bangladesh"

# download the json data from openweathermap.org's API

url = BASE_URL + "q=" + location_ + "&appid=" + APP_ID

response = requests.get(url)

if response.status_code == 200:

    #print(response.text) # this is the raw json text 

    # getting data in json format

    data = response.json()

    print(data)

    # getting the main block

    main = data['main']

    temp = main['temp']

    humidity = main['humidity']

    #weather report

    report = data['weather']

    coord = data['coord']
    
    # coordinate
    lon = coord['lon']
    lat = coord['lat']

    description = report[0]['description']

    print('-'*20 + location_ + '-'*20)
    print(f'Temperature - {temp}')
    print(f'Humidity - {humidity}')
    print(f'weather report = {description}')
    print(f'Lon = {lon} , Lat = {lat}')

