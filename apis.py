from amadeus import Flights
from key import amadeus_key
from key import instagram_key
from key import iata_key
import requests
from flask import * 
import ast
import json

# ============================  Functions ===========================================


def convertToIata(city):
	pass



def convertToCity(iata):
	url = "https://iatacodes.org/api/v6/airports?api_key=" + iata_key + "&code=" + iata
	city = json.loads(requests.get(url).content)["response"][0]['name']
	return city 

def cityToCountry(city):
	pass

# =============================== Scripts ==========================================

flights = Flights(amadeus_key)
origin = 'BKK'
departure_date = None
price = None
duration = None
direct = None
aggregation_mode = None

resp = flights.inspiration_search(
    origin=origin,
    departure_date=departure_date,
    max_price=price,
    duration=duration,
    direct=direct,
    aggregation_mode=aggregation_mode)



destinations = []

prices = []
for x in range(len(resp['results'])):
	destinations.append(resp['results'][x]['destination'])
	prices.append(resp['results'][x]['price'])


	
