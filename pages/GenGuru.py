import streamlit as st
import requests

st.set_page_config(
    page_title="GenGuru",
    page_icon="👋",
)

st.sidebar.success("GenGuru")

# Judul aplikasi
st.title("GenGuru")
st.markdown("Aplikasi pembuat perencanaan pembelajaran berbasis AI!")

# Input dari pengguna


options = {
    "Tujuan": "Tuliskan tujuan pembelajaran beserta indikator pencapaian ",
    "Aktivitas": "Tuliskan aktivitas pembelajaran dengan lengkap ",
    "Soal": "Tuliskan 5 soal esai bertipe higher order thinking skill atau deep learning. "
}
selected_display = st.selectbox("Pilih komponen:", list(options.keys()))
selected_task = options[selected_display]

user_topic = st.text_input("Masukkan topik materi:", "")

# Konstruksi prompt berdasarkan input pengguna
prompt = (
    f"Topik Materi: {user_topic} "
    f"INSTRUKSI: {selected_task}. "
    "Tuliskan dengan bahasa yang jelas. "
)

# Tombol untuk memicu pemanggilan API
if st.button("Buat"):
    if user_topic.strip() == "":
        st.error("Silakan masukkan data terlebih dahulu.")
    else:
        # Tampilkan pesan loading
        with st.spinner("Memuat..."):
            try:
                # Pemanggilan API
                response = requests.post(
                    "https://rumahguru.org/api/index.php",
                    headers={"Content-Type": "application/json"},
                    json={"prompt": prompt, "api": "sk-097866776777575t67cc"}
                )

                # Periksa status respons
                if not response.ok:
                    st.error(f"Error: {response.status_code} - {response.reason}")
                else:
                    data = response.json()
                    if "text" in data and data["text"]:
                        # Menampilkan hasil cerita
                        st.markdown(data["text"], unsafe_allow_html=True)
                    else:
                        st.warning("Tidak ada respons teks yang tersedia.")
            except Exception as e:
                st.error(f"Error fetching data: {str(e)}")

# Footer aplikasi
st.markdown("---")
st.markdown("© 2025 AI Institute")