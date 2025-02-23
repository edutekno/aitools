import streamlit as st
import requests

# Judul aplikasi
st.title("GenFood")
st.markdown("Aplikasi generator resep otomatis. Cukup ketik nama makanan, ide resep, bahan makanan atau jadwal, dan AI akan menghasilkan resepnya secara instan!")

# Input dari pengguna
question = "PROMPT: "+ st.text_input("Masukkan nama makanan, ide resep, atau bahan:", "")+ " INSTRUKSI: Anda akan membuatkan resep masakan (atau minuman) dengan nama makanan/minuman, bahan atau kriteria kriteria. "+"(Jika bahan dan kriteria belum jelas, buatkan resep yang terbaik yang anda tahu.). langsung jawab diawali dengan nama resep tanpa intro. kemudian tuliskan resep lengkap dengan detail."+" Di akhir berikan tips dan penjelasan singkat makanan ini (misal tentang kebaikan/manfaatnya, tradisi/sejarahnya dll)."
# Tombol untuk memicu pemanggilan API
if st.button("Buat Resep"):
    if question.strip() == "":
        st.error("Silakan masukkan input terlebih dahulu.")
    else:
        # Tampilkan pesan loading
        with st.spinner("Memuat resep..."):
            try:
                # Pemanggilan API
                response = requests.post(
                    "https://rumahguru.org/api/index.php",
                    headers={"Content-Type": "application/json"},
                    json={"prompt": question, "api": "sk-097866776777575t67cc"}
                )

                # Periksa status respons
                if not response.ok:
                    st.error(f"Error: {response.status_code} - {response.reason}")
                else:
                    data = response.json()
                    if "text" in data and data["text"]:
                        # Menampilkan hasil resep
                        st.markdown(data["text"], unsafe_allow_html=True)
                    else:
                        st.warning("Tidak ada respons teks yang tersedia.")
            except Exception as e:
                st.error(f"Error fetching data: {str(e)}")

# Footer aplikasi
st.markdown("---")
st.markdown("© 2025 AI Institute")