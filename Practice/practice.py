import pandas as pd
import streamlit as st

st.set_page_config(
     page_title="Job Title list",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded"
 )

df = pd.read_excel('Pay Range Master 051722.xlsx', sheet_name='Master_List')

df['Grade'] = df['Grade'].astype(str)
df['AIP %'] = df['AIP %'].astype(str)
df['Job Code'] = df['Job Code'].astype(int)

titles = ['']

for title in df['Job Title'].drop_duplicates():
    titles.append(title)

title_choice = st.sidebar.selectbox("Select a title:", titles)
if title_choice != '':
    df = df[df['Job Title'] == title_choice]
st.dataframe(df.style.format(subset=['Annual Min', 'Annual Mid','Annual Max'], formatter="{:,.0f}"))