import os

import numpy as np
import pandas as pd
import streamlit as st

# st.write(
#     "Has environment variables been set:",
#     os.environ["db_username"] == st.secrets["db_username"])

df = pd.read_excel('Pay Range Master 051722.xlsb', sheet_name='Master_List')
st.dataframe(df)