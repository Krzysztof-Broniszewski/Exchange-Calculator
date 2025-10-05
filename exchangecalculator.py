import requests
import json

url = "https://api.nbp.pl/api/exchangerates/tables/a?format=json"
response = requests.get(url, timeout=10)

if response.ok:
    data = response.json()[0]

    table = data["table"]
    no = data["no"]
    effectiveDate = data["effectiveDate"]

    rates = data["rates"]

    nameList = []
    codes = []

    for rate in rates:
        # dodajemy (currency, code) do listy
        nameList.append((rate["currency"], rate["code"]))
        print((rate["currency"], rate["code"]))
        # zbieramy same kody
        codes.append(rate["code"])

    print("\nWszystkie kody:", codes)
else:
    print("Błąd HTTP:", response.status_code, response.text)
