import streamlit as st
import pandas as pd
import requests

URL = "https://min-api.cryptocompare.com/data/top/percent?limit=10&tsym=USD"

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()
print(data["Data"])
all_data = data["Data"]