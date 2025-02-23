import os
import streamlit as st
from groq import Groq

# Initialize Groq client
def initialize_groq_client():
    #api_key = os.environ.get("GROQ_API_KEY")
    api_key="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"
    if api_key is None:
        st.error("GROQ_API_KEY tidak ditemukan. Pastikan API key sudah dikonfigurasi.")
        return None
    return Groq(api_key=api_key)

# Function to get chat completion
def get_chat_completion(client, prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Main function
def main():
    st.title("Groq AI Chat Completion Demo")
    st.write("Aplikasi sederhana untuk menanyakan pertanyaan ke model bahasa Groq.")
    
    prompt = st.text_input("Masukkan pertanyaan Anda:", placeholder="Ex: Explain the importance of fast language models")
    
    if st.button("Kirim Pertanyaan"):
        client = initialize_groq_client()
        if client:
            response = get_chat_completion(client, prompt)
            if response:
                st.write("Jawaban:")
                st.markdown(f"{response}")

if __name__ == "__main__":
    main()
