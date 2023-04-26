

city = input('Введіть місто: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric'

data = requests.get(url).json()
temp = data['main']['temp']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
wind = data['wind']['speed']

print(f"Погода в місті: {city}\n"
    f"Температура: {temp}°C\n"
    f"Тиск: {pressure} Па\n"
    f"Вологість: {humidity} кг/м3\n"
    f"Швидкість вітру: {wind} м\с")