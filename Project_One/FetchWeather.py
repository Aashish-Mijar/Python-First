import requests
name=input("Enter your name. ")
city=input("Enter your city. ")
api_key="a6e27a837f713827baa5e9138cab3f9e"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
data=response.json()
# print(data)
temp=data['main']['temp']
description = data['weather'][0]['description']
print(f"Hello {name}! 🌞 It’s currently {temp}°C with {description} in {city}.")