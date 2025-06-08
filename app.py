import streamlit as st
import joblib
import re
import emoji
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download resource jika belum ada
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab', quiet=True)

# Load model, encoder, vectorizer
model = joblib.load('model.pkl')
encoder = joblib.load('encoder.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Custom dictionary slang ke baku
custom_dict = {
    'mantap': ['mantep'],
    'bagus': ['good', 'top'],
    'tidak': ['ga', 'gak'],
    'oke': ['ok'],
    'mudah': ['easy'],
    'besar': ['gede'],
    'kukuh': ['kokoh'],
    'senang': ['happy'],
    'saran': ['rekomen', 'recommended'],
    'pas': ['sesuai'],
    'sepadan': ['worth it'],
    'terlambat': ['telat'],
    'kotor': ['jorok'],
    'menunda': ['delay'],
    'melentur': ['melenyot']
}

irrelevant_words = ['yang', 'barang', 'nya', 'botol', 'air', 'ini', 'itu']
stop_words = set(stopwords.words('indonesian'))

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')

def clean_text(text):
    text = text.lower()
    text = remove_emoji(text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    
    for key, replacements in custom_dict.items():
        for word in replacements:
            text = re.sub(r'\b' + re.escape(word) + r'\b', key, text)
    
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and t not in irrelevant_words]
    tokens = list(dict.fromkeys(tokens))
    return ' '.join(tokens)

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis", layout="centered")
st.title("🔍 Analisis Sentimen Kalimat")
st.write("Masukkan kalimat untuk memprediksi sentimen (Positif, Negatif, atau Netral).")

input_text = st.text_area("Masukkan Kalimat", "")

if st.button("Prediksi"):
    if input_text.strip() == "":
        st.warning("Silakan masukkan kalimat terlebih dahulu.")
    else:
        cleaned = clean_text(input_text)
        tfidf = vectorizer.transform([cleaned])
        prediction = model.predict(tfidf)
        label = encoder.inverse_transform(prediction)[0]

        st.markdown(f"### 📝 Hasil Prediksi: **{label}**")
        st.markdown("**Teks Setelah Preprocessing:**")
        st.code(cleaned)
