import streamlit as st
from utils import get_token_prices


# Streamlit UI
st.title("Crypto Price Alert")


def display_table():
    # st.markdown(f"## {title}")
    header_cols = st.columns([1, 2, 3, 2, 2])
    with header_cols[0]:
        st.markdown("**Logo**")
    with header_cols[1]:
        st.markdown("**Symbol**")
    with header_cols[2]:
        st.markdown("**Full Name**")
    with header_cols[3]:
        st.markdown("**Price**")
    with header_cols[4]:
        st.markdown("**Percent Change**")

    result = get_token_prices()
    # print(result)
   