import requests

city = input('Enter a city: ')

units = 'metric'
unitsSymbols = {

'imperial': '˚F',

'metric': '˚C',

'kelvin': 'K'

}

try:
    response = requests.get(('http://api.openweathermap.org/data/2.5/weather?q=' + city + 
                            '&appid=476b94193414be09d482c9ee0af011e8&units='+units).json())
    
currentTemperature = response['main']['temp']
minTemperature = response['main']['temp_min']
humidity = response['main']['humidity']
maxTemperature = response['main']['temp_max']
feelsLikeTemperature = response['main']['feels_like']
description = response['weather'][0]['description']

print('In the city of ' + city.capitalize() + ':')  
print('the current temperature is ' + str(currentTemperature) + unitsSymbols[units] + ' but feels like ' + str(feelsLikeTemperature) + unitsSymbols[units])
print('the weather is ' + description)
print('the current humidity level is ' + str(humidity) + '%')

except :

print('city not found')
      