import streamlit as st
import pandas as pd
import sys
import os

# Backend klasörünü sisteme tanıtıyoruz (modülleri bulması için)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.ai_engine import get_ai_recommendation

# Sayfa Ayarları
st.set_page_config(page_title="RotaNet - AI Lojistik", layout="wide")

# Başlık Kısmı
st.title("🚚 RotaNet: Adil Lojistik Planlama")
st.write("Operasyonel planlamada yapay zeka destekli tarafsızlık.")

# Sidebar (Veri Girişleri)
with st.sidebar:
    st.header("⚙️ Konfigürasyon")
    api_key = st.text_input("Gemini API Key", type="password")
    uploaded_file = st.file_uploader("Sefer Verilerini Yükle (Excel/CSV)", type=["xlsx", "csv"])
    num_vehicles = st.number_input("Aktif Araç Sayısı", min_value=1, value=1)
# --- Kısım 2: Veri İşleme ---
data = None
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        st.subheader("📋 Yüklenen Sefer Verileri")
        st.dataframe(data.head()) # İlk 5 satırı göster
    except Exception as e:
        st.error(f"Dosya okuma hatası: {e}")
# --- Kısım 3: AI Optimizasyonu ---
if st.button("🚀 Optimizasyonu Başlat"):
    if data is not None and api_key:
        with st.spinner("AI analiz ediyor, adalet puanları hesaplanıyor..."):
            try:
                # Backend'den AI sonucunu çağırıyoruz
                result = get_ai_recommendation(api_key, data)
                
                st.subheader("🤖 AI Karar Destek Raporu")
                st.markdown(result) # AI'dan gelen cevabı markdown formatında yazdır
            except Exception as e:
                st.error(f"Analiz sırasında bir hata oluştu: {e}")
    else:
        st.warning("Lütfen önce bir dosya yükleyin ve API anahtarınızı girin.")
