import google.generativeai as genai
import streamlit as st

def get_route_insights(metrics, route_summary):
    # Secrets'tan anahtarı al
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Bir lojistik uzmanısın. Şu optimizasyon verilerini yorumla:
    Mesafe: {metrics.get('total_distance')} km
    Rota: {route_summary}
    
    Bu rotayı daha verimli hale getirmek veya maliyeti düşürmek için 3 somut öneri ver.
    """
    
    response = model.generate_content(prompt)
    return response.text
