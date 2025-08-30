# calculate data using API

import requests

countryname= input("Enter your country: ")
url = f"https://disease.sh/v3/covid-19/countries/{countryname}"
response = requests.get(url)
data = response.json()

cases = data['cases']
deaths = data['deaths']
recovered = data['recovered']

print(f"COVID Starts from {countryname}")
print(f"Cases: {cases}")
print(f"Deaths: {deaths}")
print(f"Recovered: {recovered}")