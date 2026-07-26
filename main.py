import os
import asyncio
from telegram import Bot
from google import genai

# 1. جلب المفاتيح من بيئة العمل
TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def analyze_and_send():
    if not GEMINI_API_KEY:
        raise ValueError("خطأ: لم يتم العثور على GEMINI_API_KEY في GitHub Secrets!")

    # 2. تهيئة عميل Gemini
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    sample_apartment = """
    شقة للإيجار حي النعيم بجدة، 4 غرف وصالة و2 حمام، العمارة مجددة بالكامل، 
    السعر 32,000 ريال سنوياً دفعتين، قريبة من الخدمات والمسجد.
    """
    
    prompt = f"""
    أنت خبير عقاري في مدينة جدة. قم بتحليل إعلان الشقة التالي باختصار شديد (3 نقاط فقط):
    1. ملخص سريع للعرض (الحي، عدد الغرف، السعر).
    2. تقييم السعر بالنسبة للموقع.
    3. أهم ميزة في العرض.
    
    الإعلان:
    {sample_apartment}
    """
    
    # 3. استخدام النموذج المعتمد والمتاح رسمياً
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=prompt,
    )
    
    telegram_message = f"🤖 **تحليل رادار جدة الذكي (Gemini):**\n\n{response.text}"
    
    # 4. إرسال الرسالة إلى التليجرام
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=telegram_message)

if __name__ == "__main__":
    asyncio.run(analyze_and_send())
