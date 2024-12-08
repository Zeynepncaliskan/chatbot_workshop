import streamlit as st
import model_file

st.header("🤖 Mühendishane Chatbot")

# Sistem promptunu tanımla
system_prompt = "Sen Sezai Karakoç gibi cevap veren bir chatbotsun"

# Başlangıç mesajı
with st.chat_message(name="assistant"):
    st.write("Merhaba, Size nasıl yardımcı olabilirim?")

# Mesaj geçmişini tutmak için bir liste
messages = []

# Önceki mesajları ekrana yazdırır
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcının girdiği soru
soru = st.chat_input("Haydi sor sor...")

# Kullanıcı soru girdiyse
if soru:
    # Kullanıcının mesajını ekrana yazdır
    with st.chat_message("user"):
        st.markdown(soru)

    # Kullanıcının mesajını geçmişe ekle
    messages.append({"role": "user", "content": soru})

    # Mesaj geçmişini birleştir
    chat_history = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in messages]
    )

    # Modelden cevabı al
    response = model_file.give_response(chat_history, soru, system_prompt=system_prompt)

    # Cevabı ekrana yazdır
    with st.chat_message("assistant"):
        st.markdown(response)

    # Cevabı geçmişe ekle
    messages.append({"role": "assistant", "content": response})
    