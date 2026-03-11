import streamlit as st
import pandas as pd

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Dashboard Analisis Siswa", layout="wide")
st.title("📊 Dashboard Analisis Kebutuhan Peserta Didik")
st.markdown("Dasbor ini menampilkan analisis aspek, gaya belajar, dan latar belakang siswa yang paling dominan di kelas.")
st.markdown("---")

# 1. Memuat Data
@st.cache_data
def load_data():
    # Pastikan nama file sesuai dengan yang ada di folder Anda
    df = pd.read_csv("Analisis Kebutuhan Peserta Didik.xlsx - Sheet1.csv")
    return df

df = load_data()

# Membagi layar menjadi 3 kolom agar rapi
col1, col2, col3 = st.columns(3)

# ---------------------------------------------------------
# GRAFIK 1: Aspek Dominan (AK, AA, AP)
# ---------------------------------------------------------
with col1:
    st.subheader("1. Aspek Dominan")
    st.caption("Membandingkan rata-rata Aspek Kognitif, Afektif, dll.")
    
    aspek_cols = ['Rata-Rata AK', 'Rata-Rata AA', 'Rata-Rata AP']
    # Menghitung rata-rata kelas untuk masing-masing aspek
    rata_aspek = df[aspek_cols].mean()
    
    # Menampilkan grafik batang bawaan Streamlit
    st.bar_chart(rata_aspek, color="#4A90E2")


# ---------------------------------------------------------
# GRAFIK 2: Gaya Belajar Dominan (GB)
# ---------------------------------------------------------
with col2:
    st.subheader("2. Gaya Belajar Dominan")
    st.caption("Membandingkan item Gaya Belajar (GB1, GB2, GB3)")
    
    gb_cols = ['GB1', 'GB2', 'GB3']
    rata_gb = df[gb_cols].mean()
    
    # Jika Anda ingin mengubah label GB1, GB2, GB3 menjadi Visual, Auditori, Kinestetik:
    # rata_gb.index = ['Visual', 'Auditori', 'Kinestetik']
    
    st.bar_chart(rata_gb, color="#50E3C2")


# ---------------------------------------------------------
# GRAFIK 3: Latar Belakang Dominan (LBB)
# ---------------------------------------------------------
with col3:
    st.subheader("3. Latar Belakang Dominan")
    st.caption("Membandingkan item Latar Belakang (LBB1, LBB2, LBB3)")
    
    lbb_cols = ['LBB1', 'LBB2', 'LBB3']
    rata_lbb = df[lbb_cols].mean()
    
    st.bar_chart(rata_lbb, color="#F5A623")

# Menambahkan tabel data mentah di bagian bawah jika dibutuhkan
st.markdown("---")
st.subheader("Tabel Data Responden")
st.dataframe(df)
