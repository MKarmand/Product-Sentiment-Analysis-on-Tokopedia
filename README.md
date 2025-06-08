# Analisis Sentimen Produk LocknLock di Tokopedia

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan produk **LocknLock** di Tokopedia. Proses ini melibatkan tahap pembersihan data, pelabelan berbasis leksikon, ekstraksi fitur, penyeimbangan data, pelatihan model menggunakan algoritma **Multilayer Perceptron (MLP)**, serta evaluasi model.

🔗 **[Klik di sini untuk membuka aplikasi Streamlit](https://share.streamlit.io/username/nama-aplikasi/main/app.py)**

## 📁 Struktur Proyek

### 🔹 1. Pra-pemrosesan Data
- Mengganti kata tidak baku (slang) dengan kata baku.
- Menghapus kata yang tidak relevan.
- Mengubah semua huruf menjadi huruf kecil.
- Menghapus angka dan tanda baca.
- Menghapus data duplikat.

### 🔹 2. Pelabelan Sentimen
Pelabelan dilakukan berdasarkan skor leksikal:
- **Positif > Negatif** → Sentimen **Positif**
- **Positif < Negatif** → Sentimen **Negatif**
- **Positif = Negatif** → Sentimen **Netral**

### 🔹 3. Visualisasi
- Visualisasi word cloud untuk setiap kelas sentimen.

### 🔹 4. Ekstraksi Fitur
- Memisahkan fitur (X) dan label (y).
- Menggunakan **SMOTE** untuk menyeimbangkan distribusi kelas.

### 🔹 5. Pemodelan
- Melatih model klasifikasi menggunakan **Multilayer Perceptron (MLP)**.
- Menggunakan data pelatihan dan validasi.

### 🔹 6. Evaluasi
- Evaluasi performa model menggunakan metrik akurasi, precision, recall, dan f1-score.

## 🛠️ Teknologi dan Library
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- WordCloud
- imbalanced-learn (SMOTE)
- Streamlit

## 🚀 Cara Menjalankan

Aplikasi ini dapat dijalankan langsung secara online melalui Streamlit:


> Gantilah URL di atas dengan tautan aplikasi Streamlit Anda yang sebenarnya.

## 📌 Catatan
- Kamus leksikon untuk pelabelan sentimen harus tersedia sebelum proses labeling.
- Daftar kata slang dan stopword sebaiknya disesuaikan dengan karakteristik data dari Tokopedia.
