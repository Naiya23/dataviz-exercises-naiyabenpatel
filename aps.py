import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

st.title("📊 Global Superstore Dashboard")

df = pd.read_csv("Global_Superstore2.csv", encoding="latin1")

st.dataframe(df.head())
