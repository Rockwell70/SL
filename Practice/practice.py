import os

import numpy as np
import pandas as pd
import streamlit as st

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"])

df = pd.read_excel('EE_Data.xlsx', usecols='P,K')
summary = pd.pivot_table(df, index='MSA', values='Annual Salary', aggfunc=np.mean)
st.dataframe(summary)