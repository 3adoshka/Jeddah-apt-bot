import os
import requests
import google.generativeai as genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

def run_bot():
    genai.configure(api_key=GEMINI_API_KEY)
    
    welcome_msg = (
        "🚀 **تم تفعيل رادار شقق جدة بنجاح!**\n\n"
        "السيرفر يعمل الآن وجاهز لمتابعة العروض واقتناص أفضل الفرص تلقائياً."
    )
    send_telegram(welcome_msg)
    print("تم إرسال رسالة التجربة إلى التليجرام بنجاح!")

if __name__ == "__main__":
    run_bot()
