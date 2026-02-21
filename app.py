import streamlit as st
import pandas as pd
from pandasai import Agent # Naya aur fast tareeka

st.set_page_config(page_title="Data Guru", layout="wide")
st.header("Satik AI Data Analyst 🤖")

file = st.file_uploader("CSV upload karo", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head(5)) # Data dikhayega

    # Agent setup (Isme LLM ka dimaag hota hai)
    # Hint: Free API ke liye Google 'Gemini API Key' le lo, 
    # wo abhi kaafi free quota de rahe hain.
    agent = Agent(df) 

    query = st.text_input("Data ke baare mein kuch bhi pucho:")
    if query:
        with st.spinner("AI soch raha hai..."):
            answer = agent.chat(query)
            st.success(answer)