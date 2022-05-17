import os

import numpy as np
import pandas as pd
import streamlit as st

pd.options.display.float_format = "{:0,.2f}".format

st.set_page_config(
     page_title="Job Title list",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded"
 )

df = pd.read_excel('Pay Range Master 051722.xlsb', sheet_name='Master_List', converters={"Grade":str,
                                                                                         "AIP %":str,
                                                                                         'Job Code':int})
df['Hourly Min'] = round(df['Hourly Min'],2)
df['Hourly Mid'] = round(df['Hourly Mid'],2)
df['Hourly Max'] = round(df['Hourly Max'],2)

df['Annual Min'] = round(df['Annual Min'],0)
df['Annual Mid'] = round(df['Annual Mid'],0)
df['Annual Max'] = round(df['Annual Max'],0)


titles = ['']

for title in df['Job Title'].drop_duplicates():
    titles.append(title)

title_choice = st.sidebar.selectbox("Select a title:", titles)
if title_choice != '':
    df = df[df['Job Title'] == title_choice]
st.dataframe(df.style.format(subset=['Annual Min', 'Annual Mid','Annual Max'], formatter="{:,.0f}"))