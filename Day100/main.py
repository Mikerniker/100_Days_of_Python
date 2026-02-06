import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# CONFIGURATION ============================================================================
st.set_page_config(
    page_title="Deaths By Police",
    page_icon="🚓",
    layout="wide",
)
pd.options.display.float_format = '{:,.2f}'.format

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# This might be helpful:
from collections import Counter


# CONFIGURATION ============================================================================
st.set_page_config(
    page_title="Deaths By Police",
    page_icon="🚓",
    layout="wide",
)
pd.options.display.float_format = '{:,.2f}'.format


# HEADER SECTION ============================================================================

st.markdown("<h1 style='text-align: center;'>Deaths by Police in the United States</h1>", unsafe_allow_html=True)

