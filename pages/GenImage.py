import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

# Judul aplikasi
st.title("GenImage")

# Input token API
deepinfra_token = st.text_input("Masukkan DeepInfra Token", type="password")

# Input prompt
prompt = st.text_area("Masukkan Prompt", "A photo of ")

# Input ukuran gambar
size = st.selectbox("Pilih Ukuran Gambar", ["640x512", "512x512", "512x640"])

# Input model
model = st.selectbox("Pilih Model", ["black-forest-labs/FLUX-1-dev", "other-model-option"])

# Input jumlah gambar
# n_images = st.number_input("Jumlah Gambar", min_value=1, max_value=5, value=1)
n_images = 1
# Tombol generate
if st.button("Generate Image"):
    if not deepinfra_token:
        st.error("Silakan masukkan DeepInfra Token.")
    else:
        # Endpoint API
        url = "https://api.deepinfra.com/v1/openai/images/generations"

        # Headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {deepinfra_token}"
        }

        # Payload
        payload = {
            "prompt": prompt,
            "size": size,
            "model": model,
            "n": n_images
        }

        # Menampilkan loading spinner
        with st.spinner("Menghasilkan gambar... Harap tunggu..."):
            try:
                # Mengirim permintaan ke API
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()  # Memastikan tidak ada error HTTP
                data = response.json()

                # Menampilkan hasil
                for idx, image_data in enumerate(data.get("data", [])):
                    b64_image = image_data.get("b64_json")
                    if b64_image:
                        # Mendekode Base64 menjadi gambar
                        image_data = base64.b64decode(b64_image)
                        img = Image.open(BytesIO(image_data))
                        st.write(f"Gambar {idx + 1}:")
                        st.image(img, caption=f"Gambar {idx + 1}", use_container_width=True)
                    else:
                        st.warning(f"Tidak ada data Base64 untuk gambar {idx + 1}.")
            except requests.exceptions.RequestException as e:
                st.error(f"Terjadi kesalahan saat mengakses API: {e}")
