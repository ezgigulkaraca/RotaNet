import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="RotaNet - Logistics Optimization", layout="wide")

# Logo ve Başlık
col1, col2 = st.columns([1, 4])
with col1:
    # Eğer assets klasöründe logo.png varsa açılacak
    # st.image("assets/logo.png", width=150)
    st.title("🚚")
with col2:
    st.title("RotaNet")
    st.caption("AI-Powered Logistics Decision Support Platform")

st.divider()

# Karşılama Mesajı
if "dataset" not in st.session_state:
    with st.expander("ℹ️ How to get started?", expanded=True):
        st.write("""
        1. **Download** the sample dataset from the sidebar.
        2. **Upload** your delivery data (CSV/Excel).
        3. **Set** the number of vehicles.
        4. **Click** 'Run Optimization' to see the magic!
        """)
import streamlit as st
import sys
import os

# --- DİNAMİK YOL DÜZELTMESİ ---
# Bu satırlar, 'backend' klasörünün bulunamaması sorununu kökten çözer.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.analytics import calculate_metrics
from backend.distance import create_distance_matrix
from backend.loader import load_dataset
from backend.optimizer import optimize_route

from frontend.charts import show_charts
from frontend.components import (
    error_message,
    info_message,
    success_message,
)
from frontend.dashboard import show_dashboard
from frontend.map_view import show_route_map

# Sayfa Ayarları
st.set_page_config(
    page_title="RotaNet",
    layout="wide"
)

st.title("RotaNet")
st.caption("AI-Powered Logistics Route Optimization Platform")

st.divider()

# Sidebar (Sol Menü)
with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Upload Delivery Dataset", type=["csv", "xlsx"])
    vehicle_count = st.number_input("Number of Vehicles", min_value=1, value=1, step=1)
    optimize = st.button("Run Optimization", use_container_width=True)

# Session state kontrolü
if "optimization_completed" not in st.session_state:
    st.session_state.optimization_completed = False

# Dosya yükleme kontrolü
if uploaded_file is None:
    info_message("Upload a CSV or Excel file to begin route optimization.")
    st.stop()

# Veri yükleme
try:
    df = load_dataset(uploaded_file)
except Exception as exception:
    error_message(str(exception))
    st.stop()

success_message("Dataset loaded successfully.")
st.subheader("Dataset Preview")
st.dataframe(df, use_container_width=True)
st.divider()

# Optimizasyon süreci
if optimize:
    try:
        with st.spinner("Optimizing route..."):
            distance_matrix = create_distance_matrix(df)
            route, total_distance = optimize_route(distance_matrix, vehicle_count)
            metrics = calculate_metrics(total_distance, route)

        st.session_state.optimization_completed = True
        st.session_state.route = route
        st.session_state.metrics = metrics
        st.session_state.dataset = df
        success_message("Optimization completed successfully!")
    except Exception as exception:
        error_message(f"Optimization error: {str(exception)}")

# Sonuçları göster
if st.session_state.optimization_completed:
    show_dashboard(st.session_state.metrics)
    show_charts(st.session_state.dataset, st.session_state.route)
    show_route_map(st.session_state.dataset, st.session_state.route)
# Sonuçları göster (Eğer optimizasyon yapıldıysa)
if st.session_state.optimization_completed:
    # 1. Dashboard ve Grafikleri göster
    show_dashboard(st.session_state.metrics)
    show_charts(st.session_state.dataset, st.session_state.route)
    
    # 2. Haritayı göster
    show_route_map(st.session_state.dataset, st.session_state.route)
    
    # 3. YENİ: AI Analizini en sona ekle
    st.divider()
    if st.button("Generate AI Logistics Report"):
        with st.spinner("AI analyzing route..."):
            # Bu fonksiyonu backend/ai_service.py içinden çağıracaksın
            insights = get_route_insights(st.session_state.metrics, st.session_state.route)
            st.success("AI Insight:")
            st.write(insights)
