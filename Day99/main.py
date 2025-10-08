import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# from iso3166 import countries
from datetime import datetime, timedelta


pd.options.display.float_format = '{:,.2f}'.format

st.title("Mission Launches")

uploaded_file = "mission_launches.csv"