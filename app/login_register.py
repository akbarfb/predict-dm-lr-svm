import streamlit as st
import mysql.connector
import bcrypt

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_predict_dm'
    )

def register_user(nama, username, password, jk, usia):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO user (nama, username, password, jk, usia) 
        VALUES (%s, %s, %s, %s, %s)
        """, 
        (nama, username, hashed_password, jk, usia)
    )
    conn.commit()
    cursor.close()
    conn.close()

def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_user, username, password, nama FROM user WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:  # Periksa apakah result ada
        id_user, username, hashed_password, nama = result
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return id_user, username, nama  # Kembalikan id_user, username, dan nama
    return None, None, None  # Login gagal

def login_register_app():
    st.title('Login and Register')
    
    # Jika user sudah login, tampilkan pesan selamat datang
    if st.session_state.get('logged_in', False):
        username = st.session_state.get('username', 'Unknown')  # Ambil username dari session state
        st.success(f"Welcome back, {username}!")  # Menampilkan nama atau username
        if st.button('Logout'):
            st.session_state['logged_in'] = False
            st.session_state['id_user'] = None
            st.session_state['username'] = None  # Hapus username dari session state
            st.session_state['nama'] = None  # Hapus nama dari session state
            st.rerun()  # Reload halaman
        return

    menu = ['Login', 'Register']
    choice = st.sidebar.selectbox('Select an option', menu)

    if choice == 'Register':
        st.subheader('Create a New Account')
        nama = st.text_input('Nama Lengkap')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        jk = st.selectbox('Jenis Kelamin', ['Laki-laki', 'Perempuan'])
        usia = st.number_input('Usia', min_value=1, step=1)
        
        if st.button('Register'):
            if nama and username and password and jk and usia:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                if result:
                    st.error('Username already exists!')
                else:
                    register_user(nama, username, password, jk, usia)
                    st.success('Account created successfully! You can now login.')
            else:
                st.error('Please fill in all fields.')
    elif choice == 'Login':
        st.subheader('Login to Your Account')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            if username and password:
                id_user, username, nama = login_user(username, password)
                if id_user:  # Pastikan id_user ada
                    st.success('Login successful!')
                    st.session_state['logged_in'] = True  # Simpan status login
                    st.session_state['id_user'] = id_user  # Simpan ID user
                    st.session_state['username'] = username  # Simpan username
                    st.session_state['nama'] = nama  # Simpan nama
                    st.rerun()  # Reload untuk menampilkan halaman utama setelah login
                else:
                    st.error('Invalid username or password')
            else:
                st.error('Please fill in both fields.')

    elif choice == 'Login':
        st.subheader('Login to Your Account')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            if username and password:
                id_user = login_user(username, password)
                if id_user:  # Pastikan id_user ada
                    st.success('Login successful!')
                    st.session_state['logged_in'] = True  # Simpan status login
                    st.session_state['id_user'] = id_user  # Simpan ID user
                    st.rerun()
                else:
                    st.error('Invalid username or password')
            else:
                st.error('Please fill in both fields.')


   