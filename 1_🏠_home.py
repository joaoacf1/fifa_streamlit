import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/FIFA23_official_data.csv", index_col=0)

    def extract_year(value):
        if pd.isna(value):
            return value
        if isinstance(value, (int, float)):
            return int(value)
        value = str(value)
        parts = value.split()
        year = parts[-1]
        return int(year)

    df_data["Contract Valid Until"] = df_data["Contract Valid Until"].apply(extract_year)
    df_data = df_data.dropna(subset=["Contract Valid Until"])
    df_data = df_data[df_data["Contract Valid Until"] >= 2023] #Use to return from the current year: datetime.today().year
    df_data = df_data[df_data["Value"] != '£0']
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA23 OFFICIAL DATASET ⚽')

st.sidebar.markdown('Developed by https://github.com/joaoacf1')

btn = st.button('Access the data in Kaggle')

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?resource=download')

st.markdown('''
            Unlock detailed player statistics from the FIFA23 Official Dataset!
            This platform allows you to visualize key attributes such as player ratings, potential, age, and club details.
            Go deeper with additional insights like player value, weight, height, and more.
            Whether you're analyzing player performance or comparing across teams and nationalities,
            this dataset provides a rich source of football data for your analysis. Start exploring now!  
            ''')
