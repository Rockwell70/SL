import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_excel('EE_Data.xlsx', usecols='P,K')
summary = pd.pivot_table(df, index='MSA', values='Annual Salary', aggfunc=np.mean)
st.dataframe(summary)