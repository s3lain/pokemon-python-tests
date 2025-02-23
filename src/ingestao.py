# Databricks notebook source
import requests
import json
import datetime

url = "https://pokeapi.co/api/v2/pokemon?limit=1400"

response = requests.get(url)
data = response.json()
data_save = data["results"]

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

path = f"/Volumes/raw/pokemon/pokemon_raw/pokemons_list/{now}.json"


# len(data_save)
with open(path, "w") as open_file:    
    json.dump(data_save, open_file)

# COMMAND ----------

dbutils.fs.ls("/Volumes/raw/pokemon/pokemon_raw/pokemons_list/")
