# Sistem Prediksi Penyakit Diabetes Melitus

## Deskripsi Proyek  
Sistem ini bertujuan untuk **memprediksi risiko diabetes melitus** berdasarkan gejala yang diinputkan oleh pengguna. Dibangun menggunakan **Streamlit framework**, aplikasi ini menyediakan antarmuka yang interaktif dan mudah digunakan. Proyek ini memiliki **fitur login dan registrasi**, serta terintegrasi langsung dengan database untuk menyimpan riwayat prediksi.

---

## Fitur Utama  
1. **Login dan Registrasi**  
   - Pengguna dapat membuat akun baru atau masuk ke akun yang sudah ada.  
   - Informasi akun tersimpan di database untuk memastikan keamanan data.  

2. **Menu Prediksi**  
   - Pengguna dapat memasukkan data gejala seperti:  
     - **Pregnancies**  
     - **Glucose**  
     - **Blood Pressure**  
     - **Skin Thickness**  
     - **Insulin**  
     - **BMI**  
     - **Diabetes Pedigree**  
     - **Age**  
   - Data yang dimasukkan akan diproses menggunakan **metode prediksi Logistic Regression dan SVM**.  
   - Hasil prediksi ditampilkan secara real-time.  

3. **Menu Riwayat**  
   - Menampilkan riwayat prediksi yang pernah dilakukan oleh pengguna.  
   - Riwayat tersimpan langsung di database dan dapat diakses kapan saja.  

4. **Terhubung ke Database**  
   - Seluruh data seperti akun pengguna dan riwayat prediksi disimpan ke dalam database untuk memastikan integritas dan keberlanjutan data.

---

## Teknologi yang Digunakan  
- **Streamlit**: Framework untuk membangun antarmuka pengguna berbasis Python.  
- **Python**: Bahasa pemrograman utama yang digunakan.  
- **Database**: MySQL (sesuai implementasi).  
- **Logistic Regression & SVM**: Metode prediksi untuk analisis data gejala.  

---

## Struktur Proyek  
```
PREDICT-DM/
├───── app
├───── login_register.py     # Modul login dan registrasi
├───── prediksi.py           # Modul prediksi diabetes
├───── riwayat.py            # Modul menampilkan riwayat prediksi
├── main.py                  # File utama untuk menjalankan Streamlit
├── diabetes.csv             # Dataset
└──
```

---

## Cara Penggunaan  
1. **Login atau Registrasi** terlebih dahulu menggunakan akun Anda.  
2. Pilih **Menu Prediksi** dan masukkan data gejala yang diminta.  
3. Klik tombol **Prediksi** untuk melihat hasil analisis.  
4. Buka **Menu Riwayat** untuk melihat data gejala dan hasil prediksi sebelumnya.  
