# Convert USP to NPR by using API

import requests
name = input("Enter your name: ")

USD = float(input("Enter amount in USD: "))
url= "https://api.exchangerrate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()
rate = data["rates"]["NPR"]

NPR = USD * rate
print(f"Hello {name}, ${USD} is equal to रू {NPR:.2f} NPR.")