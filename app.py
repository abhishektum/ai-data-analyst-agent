import streamlit as st
import pandas as pd
from pandasai.llm import GoogleGemini
from pandasai import Agent # Ye line bhi check kar lena upar hai ya nahi

st.set_page_config(page_title="Data Guru", layout="wide")
st.header("Satik AI Data Analyst 🤖")

file = st.file_uploader("CSV upload karo", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head(5)) 

    # --- YE HAI BADLAV ---
    llm = GoogleGemini(api_token="AIzaSyA24Xkz0H9z71X_7KDOfcsMCWnXpZrv80I") 
    agent = Agent(df, config={"llm": llm}) 
    # ---------------------

    query = st.text_input("Data ke baare mein kuch bhi pucho:")
    if query:
        with st.spinner("AI soch raha hai..."):
            answer = agent.chat(query)
            st.success(answer)
