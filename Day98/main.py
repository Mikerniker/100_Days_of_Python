import streamlit as st
from utils import get_btc_details


result = get_btc_details()

# Streamlit UI

st.title("BITCOIN Price Alert")

st.image(result.get("logo"), width=100)
st.markdown(f"## BTC Price: $ {result.get('current_price'):.2f}")
st.markdown(f"## Price Change {result.get('price_change_24h')}%")