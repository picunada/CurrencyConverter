import requests
# import math
# import json

user_agent = 'Mozilla/5.0'

currency_name = input().lower()
""" Getting the json from site """
url = f'http://www.floatrates.com/daily/{currency_name}.json'

response = requests.get(url, headers={'User-Agent': user_agent})
output = response.json()
exchange_rates = {}


d = {'key1': {'key2': 1}}
while True:
    currency_receive = input().lower()
    if currency_receive == "":
        break
    amount = int(input())
    if "usd" in output:
        exchange_rates["usd"] = output["usd"]["rate"]
    if "eur" in output:
        exchange_rates["eur"] = output["eur"]["rate"]

    print("Checking the cache...")

    if f"{currency_receive}" in exchange_rates:
        print("Oh! It is in the cache!")

        exchange_rate = round(output[f"{currency_receive}"]["rate"], 4)
        amount_given = amount * exchange_rate
        print(f"You received {round(amount_given, 2)} {currency_receive.upper()}")
    else:
        print("Sorry, but it is not in the cache!")
        exchange_rates[f"{currency_receive}"] = output[f"{currency_receive}"]["rate"]
        exchange_rate = round(exchange_rates[f"{currency_receive}"], 4)
        amount_given = amount * exchange_rate
        print(f"You received {round(amount_given, 2)} {currency_receive.upper()}")


