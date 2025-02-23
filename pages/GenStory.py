import streamlit as st
import requests

st.set_page_config(
    page_title="GenStory",
    page_icon="👋",
)

st.sidebar.success("GenStory")

# Judul aplikasi
st.title("GenStory")
st.markdown("Aplikasi pembuat cerita otomatis dengan berbagai jenis. Cukup ketik ide Anda dan AI akan menghasilkan cerita yang menarik!")

# Input dari pengguna
genre_options = ["Fabel", "Dongeng", "Fiksi Ilmiah", "Misteri", "Plot Twist"]
selected_genre = st.selectbox("Pilih genre cerita:", genre_options)
user_idea = st.text_input("Masukkan ide cerita Anda:", "")

# Konstruksi prompt berdasarkan input pengguna
prompt = (
    f"PROMPT: {user_idea} "
    f"INSTRUKSI: Buatkan cerita dengan genre {selected_genre}. "
    "Ceritakan dengan detail, termasuk karakter, setting, konflik, dan resolusi. "
    "Jika ide belum jelas, buatkan cerita terbaik yang sesuai dengan genre ini. "
    "Langsung jawab dengan cerita lengkap tanpa intro."
)

# Tombol untuk memicu pemanggilan API
if st.button("Buat Cerita"):
    if user_idea.strip() == "":
        st.error("Silakan masukkan ide cerita terlebih dahulu.")
    else:
        # Tampilkan pesan loading
        with st.spinner("Memuat cerita..."):
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