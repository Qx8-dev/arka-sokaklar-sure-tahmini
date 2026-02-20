import streamlit as st
import joblib
import numpy as np

model = joblib.load("arkasokaklarmodel.pkl")

st.title("Arka Sokaklar Bölüm Süresi Tahmin Uygulaması")

feature1 = st.number_input("Bölümün numarası", min_value=1, step=1)

if st.button("Tahmin Yap"):
    data = np.array([[feature1]])
    prediction = model.predict(data)

    # Tahmini saniyeye yuvarla
    total_seconds = int(round(prediction.item()))

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    st.write(f"Tahmin: {hours} saat {minutes} dakika {seconds} saniye")