import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
import mysql.connector

# Fungsi koneksi ke database MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_predict_dm'
    )

# Fungsi untuk menyimpan data gejala ke tabel gejala
def save_gejala(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, outcome, id_user):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO gejala (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, outcome, id_user)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, outcome, id_user)
    cursor.execute(query, values)
    conn.commit()
    
    # Ambil id_gejala yang baru saja disimpan
    id_gejala = cursor.lastrowid
    cursor.close()
    conn.close()
    
    return id_gejala

# Fungsi untuk menyimpan riwayat ke tabel riwayat
def save_riwayat(id_gejala, id_user):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO riwayat (id_gejala, id_user)
    VALUES (%s, %s)
    """
    values = (id_gejala, id_user)
    cursor.execute(query, values)
    conn.commit()

    # Mengambil ID riwayat yang baru saja dibuat
    id_riwayat = cursor.lastrowid

    cursor.close()
    conn.close()

    # Mengembalikan id_gejala dan id_user (atau nilai yang dibutuhkan)
    return id_gejala, id_user


# Aplikasi utama untuk prediksi
def prediksi_app():
    st.title("Prediksi Penyakit Diabetes Melitus Menggunakan Logistic Regression dan Support Vector Machine (SVM)")
    st.write("")

    # Cek apakah pengguna sudah login
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        # Dapatkan id_user dari session_state
        id_user = st.session_state.get('id_user')

        # Load dataset
        df = pd.read_csv('diabetes.csv')
        zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
        for column in zero_not_accepted:
            df[column] = df[column].replace(0, np.nan)
            mean = int(df[column].mean(skipna=True))
            df[column] = df[column].replace(np.nan, mean)

        # Split dataset
        X = df.iloc[:, 0:8].values
        y = df.iloc[:, 8].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Model selection
        model_choice = st.selectbox("Pilih Model", ["Logistic Regression", "Support Vector Machine"])

        # Input features for prediction
        st.subheader("Masukkan Gejala")
        pregnancies = st.number_input("Pregnancies")
        glucose = st.number_input("Glucose")
        blood_pressure = st.number_input("Blood Pressure")
        skin_thickness = st.number_input("Skin Thickness")
        insulin = st.number_input("Insulin")
        bmi = st.number_input("BMI")
        diabetes_pedigree = st.number_input("Diabetes Pedigree Function")
        age = st.number_input("Age")

        if st.button("Prediksi"):
            if model_choice == "Logistic Regression":
                # Logistic Regression with Grid Search
                param_grid = {
                    'C': [0.01, 0.1, 1,10,100],
                    'fit_intercept': [True, False],
                    'solver': ['liblinear', 'newton-cg', 'lbfgs', 'sag', 'saga']
                }
                grid = GridSearchCV(LogisticRegression(max_iter=500), param_grid, cv=5, scoring='accuracy')
                grid.fit(X_train, y_train)
                best_model = grid.best_estimator_ 

            elif model_choice == "Support Vector Machine":
                # Support Vector Machine with Grid Search
                param_grid = {
                    'C': [0.01, 0.1, 1, 10,100],
                    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
                    'gamma': ['scale', 'auto']
                }
                grid = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
                grid.fit(X_train, y_train)
                best_model = grid.best_estimator_

            # Prediction
            inputs = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
            result = best_model.predict([inputs])
            outcome = 0 if result[0] == 0 else 1
            diagnosis = "Pasien tidak terdiagnosis menderita Diabetes Melitus." if outcome == 0 else "Pasien terdiagnosis menderita Diabetes Melitus"
            st.success(f"Hasil prediksi: {diagnosis}")

            # Simpan gejala ke database
            id_gejala = save_gejala(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, outcome, id_user)

            # Simpan riwayat ke database
            id_gejala, id_user = save_riwayat(id_gejala, id_user)

            st.info("Gejala yang dimasukkan beserta hasil prediksi berhasil disimpan ke dalam database, dan pengguna dapat mengaksesnya melalui menu Riwayat.")

            # Model evaluation
            y_pred = best_model.predict(X_test)
            cm = confusion_matrix(y_test, y_pred)

            # Display confusion matrix
            st.subheader("Confusion Matrix")
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Tidak Diabetes', 'Diabetes'], yticklabels=['Tidak Diabetes', 'Diabetes'])
            plt.ylabel('True Label')
            plt.xlabel('Predicted Label')
            st.pyplot(fig)

            # Display classification report
            st.subheader("Classification Report")
            report = classification_report(y_test, y_pred, target_names=['Tidak Diabetes', 'Diabetes'])
            st.text(report)
    else:
        st.error("Silakan login terlebih dahulu.")
