import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import GoogleGemini

st.set_page_config(page_title="Satik AI Analyst", layout="wide")
st.header("Data Guru 🤖")

# API Key - Yahan apni Gemini wali key dhyan se paste kar
llm = GoogleGemini(api_token="AIzaSyA24Xkz0H9z71X_7KDOfcsMCWnXpZrv80I")

file = st.file_uploader("CSV upload karo", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.write("Data Preview:", df.head(3))

    query = st.text_input("Data ke baare mein kuch bhi pucho:")
    
    if query:
        with st.spinner("AI dimaag laga raha hai..."):
            try:
                # Agent ki jagah SmartDataframe use kar rahe hain
                df_smart = SmartDataframe(df, config={"llm": llm})
                answer = df_smart.chat(query)
                st.success(answer)
            except Exception as e:
                st.error(f"Ek choti gadbad ho gayi: {e}")
