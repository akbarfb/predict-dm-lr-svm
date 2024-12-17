import streamlit as st
from app.login_register import login_register_app
from app.prediksi import prediksi_app
import app.riwayat  # Import file riwayat.py

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'username' not in st.session_state:  # Pastikan key 'username' ada
        st.session_state['username'] = None

    if 'nama' not in st.session_state:
        st.session_state['nama'] = None

    if st.session_state['logged_in']:
        # Jika sudah login, tampilkan menu utama
        id_user = st.session_state['id_user']
        username = st.session_state['username']
        nama = st.session_state['nama']  

        menu = ["🏠 Home", "🔍 Prediksi", "📜 Riwayat"]  # Menu tanpa Logout
        choice = st.sidebar.selectbox("Pilih Menu", menu)

        # Menambahkan tombol logout di bawah sidebar setelah menu
        st.sidebar.markdown("###")
        if st.sidebar.button("🚪 Logout"):
            st.session_state['logged_in'] = False  # Set status login menjadi False
            st.session_state['id_user'] = None  # Hapus data pengguna
            st.session_state['username'] = None  # Hapus nama pengguna
            st.rerun() 

        # Menampilkan informasi pengguna yang sedang login
        st.sidebar.markdown(f"### User : {nama}") 
        st.sidebar.markdown(f"ID Pengguna : {id_user}")

        if choice == "🏠 Home":
            # Menambahkan gambar latar belakang sesuai tema kesehatan
            st.markdown(
                """
                <style>
                .stApp {
                    position: relative;
                    background-image: url('https://down-yuantu.pngtree.com/back_our/20230412/bg/7b36bffbac31f.png?e=1734388660&st=NzJhMmJkYWVhOGY2ZWQyMDliZTA2YzFiYzZiYjdmNGY&n=%E2%80%94Pngtree%E2%80%94medical+service+black+background_2445898.png');
                    background-size: cover;
                    background-position: center;
                    height: 100vh;
                    color: white;
                }
                .stApp::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0, 0, 0, 0.5);  /* Gelapkan latar belakang dengan opacity */
                    z-index: -1;
                }
                .title {
                    font-size: 3rem;
                    font-weight: bold;
                    background: linear-gradient(45deg, #ffb300, #2c3e50);
                    -webkit-background-clip: text;
                    color: transparent;
                    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
                    animation: fadeIn 2s ease-in-out;
                }
                .content-text {
                    font-size: 1.2rem;
                    line-height: 1.6;
                    font-weight: 300;
                    color: white;
                    text-align: justify;
                    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4);
                }
                .highlight {
                    color: #ffcc00;
                    font-weight: bold;
                }
                @keyframes fadeIn {
                    0% {
                        opacity: 0;
                        transform: translateY(20px);
                    }
                    100% {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                </style>
                """, unsafe_allow_html=True
            )

            # Menampilkan teks dengan animasi dan highlight
            st.markdown("<h1 class='title'>Selamat Datang di Sistem Prediksi Diabetes Melitus</h1>", unsafe_allow_html=True)
            st.markdown(
                "<p class='content-text'>Ini adalah halaman utama aplikasi Anda. Sistem ini dirancang untuk membantu Anda dalam mendeteksi risiko <span class='highlight'>Diabetes Melitus</span> secara dini. Dengan menggunakan teknologi prediksi berbasis data gejala seperti jumlah kehamilan, kadar gula darah, tekanan darah, ketebalan kulit, kadar insulin, BMI, riwayat diabetes keluarga, dan usia, kami menyediakan hasil prediksi yang akurat dan bermanfaat. Cek kondisi Anda sekarang untuk langkah pencegahan yang lebih baik!. Pilih pada menu sidebar Prediksi untuk melakukan prediksi penyakit Diabetes Melitus atau menu sidebar Riwayat untuk melihat riwayat prediksi yang telah anda inputkan.</p>", unsafe_allow_html=True)
        
        elif choice == "🔍 Prediksi":
            st.title("Halaman Prediksi")
            prediksi_app()
        
        elif choice == "📜 Riwayat":
            st.title("Riwayat Prediksi Penyakit Diabetes")
            app.riwayat.show_riwayat(st.session_state['id_user'])
    else:
        # Jika belum login, arahkan ke halaman login/register
        login_register_app()

if __name__ == "__main__":
    main()
