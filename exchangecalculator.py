import requests
import json

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/a?format=json")

if response.ok == True :
    data = response.json()[0]
    # print(data)

    table = data["table"]
    no = data["no"]
    effectiveDate = data["effectiveDate"]

    # print("Exchange rates: ", table, no, effectiveDate)

    rates = data["rates"]

    nameList = ""

    for rate in rates :
        # print(rate["currency"], rate["code"], rate["mid"])
        # print(rate["code"])
        nameList = ("Kraj : " + str(rate["currency"]) + "Symbol : " + rate["code"])
        print(nameList)

        # for v in rate["code"] :
            # nameList = (nameList + str(v))
            # print(rate["code"])

        
