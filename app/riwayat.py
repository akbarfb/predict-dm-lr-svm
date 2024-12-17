import streamlit as st
import pandas as pd
import mysql.connector

# Fungsi untuk menghubungkan ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",             
        database="db_predict_dm" 
    )
    return connection

# Fungsi untuk mengambil data riwayat dari database
def get_riwayat(id_user):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Ambil data dari tabel riwayat berdasarkan id_user
    query = """
    SELECT r.id_riwayat, r.created_at, g.*, u.nama AS user_name 
    FROM riwayat r
    JOIN gejala g ON r.id_gejala = g.id_gejala
    JOIN user u ON r.id_user = u.id_user
    WHERE r.id_user = %s
    ORDER BY r.created_at DESC
    """
    cursor.execute(query, (id_user,))  # Masukkan id_user sebagai parameter query
    rows = cursor.fetchall()
    connection.close()

    # Kembalikan data sebagai DataFrame
    return pd.DataFrame(rows) if rows else None

# Fungsi untuk menampilkan riwayat
def show_riwayat(id_user):
    # Ambil data riwayat berdasarkan id_user
    data = get_riwayat(id_user)

    # Tampilkan data dalam tabel atau pesan kosong
    if data is not None and not data.empty:
        # Ubah nilai pada kolom 'outcome'
        if 'outcome' in data.columns:
            data['outcome'] = data['outcome'].apply(lambda x: "Tidak Menderita Diabetes Melitus" if x == 0 else "Menderita Diabetes Melitus")
        
        # Format angka untuk kolom numerik
        numeric_columns = [
            'pregnancies', 'glucose', 'blood_pressure', 
            'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree', 'age'
        ]
        for col in numeric_columns:
            if col in data.columns:
                data[col] = data[col].apply(lambda x: f"{x:.0f}" if x == int(x) else f"{x:.2f}")
        
        # Tampilkan tabel dengan data yang sudah diubah
        st.table(data)
    else:
        st.info("Belum ada riwayat yang tersimpan.")


# Jalankan fungsi untuk menampilkan riwayat
if __name__ == "__main__":
    show_riwayat()
