#Model for the Pokedex
#This file is meant to web scrape pokedex data from https://www.pokemon.com/us/pokedex/
# Pokemon's Picture | Index # | Description

import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.pokemon.com/us/pokedex/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.get_text())

# 800 - Necrozma, datatype string
pokeIDandName = soup.get_text()

#TODO 
#Loop thru pokeIDandName and remove all extra stuff
#Isolate index number and name