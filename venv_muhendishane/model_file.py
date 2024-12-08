import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env dosyasını yükler ve içerisindeki değişkenleri sisteme ekler.
load_dotenv(dotenv_path="C:\\Users\\Zeynep Nurten\\OneDrive\\Desktop\\projeler\\muhendishane_chatbot\\venv_muhendishane\\deneme.env")

# API anahtarını ortam değişkenlerinden al
api_key = os.getenv("GOOGLE_API_KEY")

if api_key is None:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

# API anahtarını kullanarak model yapılandırmasını yapın
import google.generativeai as genai
genai.configure(api_key=api_key)

# Kullanacağımız Generative AI modelini tanımlıyoruz
model = genai.GenerativeModel('gemini-1.5-flash')


def give_response(chat_history, soru, system_prompt):
    # Sistem promptunu ekliyoruz
    full_prompt = f"{system_prompt}\n\n{chat_history}\nuser: {soru}\nassistant:"

    # Hazırlanan prompt'u modele gönderir ve modelin oluşturduğu içeriği döndürür
    response = model.generate_content(full_prompt)

    return response.text  # Modelden gelen yanıtın sadece metin kısmını döndürür
