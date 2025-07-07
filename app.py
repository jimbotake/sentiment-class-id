import streamlit as st
import joblib

# Load model yang sudah dilatih
model = joblib.load('model/sentiment_classifier.pkl')

# Judul aplikasi
st.title("Klasifikasi Sentimen Tweet (Bahasa Indonesia)")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks tweet di sini:")

# Tombol prediksi
if st.button("Prediksi Sentimen"):
    if user_input.strip() == "":
        st.warning("Teks tidak boleh kosong!")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"Prediksi Sentimen: **{prediction}**")
