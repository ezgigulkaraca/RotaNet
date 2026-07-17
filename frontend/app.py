import streamlit as st
import pandas as pd
import sys
import os

# Sistemin backend klasörünü bulabilmesi için yolu ayarlıyoruz
from ai_engine import get_ai_recommendation

# Şimdi hata almadan içeri aktarabiliriz
from backend.ai_engine import get_ai_recommendation

# Sayfa Yapılandırması
st.set_page_config(page_title="RotaNet - Akıllı Lojistik", layout="wide")

st.title("🚚 RotaNet: Adil Lojistik Planlama")

# Sidebar - Yapılandırma
with st.sidebar:
    st.header("⚙️ Konfigürasyon")
    api_key = st.text_input("Gemini API Key", type="password")
    uploaded_file = st.file_uploader("Sefer Verilerini Yükle (Excel/CSV)", type=["xlsx", "csv"])
    num_vehicles = st.number_input("Aktif Araç Sayısı", min_value=1, value=1)

# Veri Okuma Mantığı
data = None
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        st.subheader("📋 Yüklenen Sefer Verileri")
        st.dataframe(data.head())
    except Exception as e:
        st.error(f"Dosya okuma hatası: {e}")

# AI Optimizasyonunu Çalıştırma
if st.button("🚀 Optimizasyonu Başlat"):
    if data is not None and api_key:
        with st.spinner("AI analiz ediyor, adalet puanları hesaplanıyor..."):
            try:
                result = get_ai_recommendation(api_key, data)
                st.subheader("🤖 AI Karar Destek Raporu")
                st.markdown(result)
            except Exception as e:
                st.error(f"Analiz sırasında bir hata oluştu: {e}")
    else:
        st.warning("Lütfen önce bir dosya yükleyin ve API anahtarınızı girin.")
