import requests
API = 'b57e76722caeaaacafc339d7c26da18d'
check = 1

while check == 1:
    city_input = input("Enter city name: ")

    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&APPID={API}")

    if weather_data.json()['cod'] == '404':
        print("Check spelling and try again!")
    else: check = 2

else:
    weather = weather_data.json()['weather'][0]['main']
    weather_temp = round(weather_data.json()['main']['temp'])

    print(f"it is {weather} in {city_input}")
    print(f"It is {weather_temp}°C in {city_input}")
