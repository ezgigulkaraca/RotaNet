import streamlit as st
import google.generativeai as genai

# API KEY
API_KEY = "AIzaSyAXA7edsGE5ggJrQo5wT2CO2pe2BSbEoKc"

genai.configure(api_key=API_KEY)

# MODEL (senin denemek istediğin)
model = genai.GenerativeModel("models/gemini-1.5-flash-002")

st.title("Gemini Test")

if st.button("Test Et"):
    try:
        response = model.generate_content("Merhaba, kısa bir analiz yaz")
        st.success(response.text)

    except Exception as e:
        st.error(str(e))
