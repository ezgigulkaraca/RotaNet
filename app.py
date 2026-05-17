import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import itertools
import random

from google import genai

# =========================
# SAYFA
# =========================
st.set_page_config(page_title="LogiMind AI", layout="wide")

st.title("LogiMind AI Rota Optimizasyonu")
st.write("Kullanıcı kendi Gemini API key’i ile sistemi test edebilir.")

# =========================
# API KEY GİRİŞİ
# =========================
st.sidebar.header("Gemini API Ayarları")

api_key = st.sidebar.text_input(
    "Gemini API Key Girin",
    type="password"
)

client = None

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        st.sidebar.success("API Key yüklendi ✔")
    except:
        st.sidebar.error("API Key geçersiz ❌")

# =========================
# PARAMETRELER
# =========================
arac_sayisi = st.sidebar.slider("Araç Sayısı", 1, 5, 2)
arac_kapasitesi = st.sidebar.slider("Araç Kapasitesi", 5, 50, 15)
trafik = st.sidebar.slider("Trafik Katsayısı", 1.0, 2.0, 1.0)

# =========================
# MÜŞTERİLER
# =========================
musteriler = {
    "A": (5, 10, 3), "B": (-3, 8, 5), "C": (12, 2, 4),
    "D": (8, -4, 2), "E": (-6, -5, 6), "F": (2, 15, 3),
    "G": (14, -1, 5), "H": (-2, -9, 2), "I": (7, 7, 4)
}

# =========================
# MESAFE
# =========================
def mesafe(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1]) * trafik

# =========================
# RANDOM KARŞILAŞTIRMA
# =========================
def random_mesafe(df):
    noktalar = df.iloc[1:].to_dict("records")
    random.shuffle(noktalar)

    yol = [(0, 0)] + [(n["x"], n["y"]) for n in noktalar] + [(0, 0)]

    return sum(
        mesafe(yol[i], yol[i+1])
        for i in range(len(yol)-1)
    )

# =========================
# GEMINI ANALİZ
# =========================
def gemini_yorumla(client, arac_sayisi, toplam_mesafe, tasarruf, trafik):
    if client is None:
        return "Gemini aktif değil (API key girilmedi)"

    try:
        prompt = f"""
Lojistik uzmanısın.

Araç: {arac_sayisi}
Mesafe: {toplam_mesafe:.2f}
Tasarruf: %{tasarruf:.1f}
Trafik: {trafik}

3 madde analiz yap:
- verimlilik
- operasyon önerisi
- karbon/maliyet etkisi
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini hata: {e}"

# =========================
# UI
# =========================
secili = st.multiselect(
    "Müşteriler",
    list(musteriler.keys()),
    default=["A", "B", "C"]
)

if len(secili) == 0:
    st.stop()

# =========================
# DATA
# =========================
data = [{"name": "Depo", "x": 0, "y": 0, "demand": 0}]

for m in secili:
    x, y, d = musteriler[m]
    data.append({"name": m, "x": x, "y": y, "demand": d})

df = pd.DataFrame(data)
st.dataframe(df)

# =========================
# OPTİMİZASYON
# =========================
if st.button("Optimize Et"):

    toplam_talep = df["demand"].sum()

    if toplam_talep > arac_sayisi * arac_kapasitesi:
        st.error("Kapasite yetersiz!")
        st.stop()

    rotalar = {i: [] for i in range(arac_sayisi)}
    yuk = {i: 0 for i in range(arac_sayisi)}

    for m in data[1:]:
        best = None

        for a in range(arac_sayisi):
            if yuk[a] + m["demand"] <= arac_kapasitesi:
                last = (0, 0) if len(rotalar[a]) == 0 else (rotalar[a][-1]["x"], rotalar[a][-1]["y"])
                d = mesafe(last, (m["x"], m["y"]))

                if best is None or d < best[1]:
                    best = (a, d)

        if best:
            a = best[0]
        else:
            a = min(yuk, key=yuk.get)

        rotalar[a].append(m)
        yuk[a] += m["demand"]

    fig = go.Figure()
    colors = ["red", "blue", "green", "purple", "orange"]

    toplam_mesafe = 0

    for a in range(arac_sayisi):
        if not rotalar[a]:
            continue

        best_route = None
        best_dist = float("inf")

        for perm in itertools.permutations(rotalar[a]):
            path = [(0, 0)] + [(p["x"], p["y"]) for p in perm] + [(0, 0)]

            dist = sum(
                mesafe(path[i], path[i+1])
                for i in range(len(path)-1)
            )

            if dist < best_dist:
                best_dist = dist
                best_route = perm

        toplam_mesafe += best_dist

        x = [0] + [p["x"] for p in best_route] + [0]
        y = [0] + [p["y"] for p in best_route] + [0]

        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="lines+markers",
            name=f"Araç {a+1}",
            line=dict(color=colors[a % len(colors)], width=3)
        ))

    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode="markers",
        name="Depo",
        marker=dict(size=15, color="black", symbol="square")
    ))

    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # METRİKLER
    # =========================
    r = random_mesafe(df)
    tasarruf = ((r - toplam_mesafe) / r) * 100 if r > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Random", f"{r:.2f}")
    col2.metric("Optimize", f"{toplam_mesafe:.2f}")
    col3.metric("Tasarruf", f"%{tasarruf:.1f}")

    # =========================
    # AI RAPOR
    # =========================
    st.subheader("AI Analiz")

    with st.spinner("Gemini çalışıyor..."):
        rapor = gemini_yorumla(client, arac_sayisi, toplam_mesafe, tasarruf, trafik)
        st.info(rapor)
