# convert USD to INR by using API 

import requests
name = input("Enter your name: ")
USD = float(input("Enter amount in USD: "))

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()
rate = data["rates"]["INR"]
INR = USD * rate
print(f"Hello {name}, ${USD} is equal to ₹{INR:.2f} INR.")
