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
  