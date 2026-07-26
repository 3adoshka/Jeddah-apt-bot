import os
import asyncio
from telegram import Bot
from google import genai

# جلب المفاتيح من متغيرات البيئة
TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def analyze_and_send():
    # 1. تهيئة عميل Gemini
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # نموذج إعلان شقة كمثال للفحص
    sample_apartment = """
    شقة للإيجار حي النعيم بجدة، 4 غرف وصالة و2 حمام، العمارة مجددة بالكامل، 
    السعر 32,000 ريال سنوياً دفعتين، قريبة من الخدمات والمسجد.
    """
    
    # 2. طلب التحليل والملخص من Gemini
    prompt = f"""
    أنت خبير عقاري في مدينة جدة. قم بتحليل إعلان الشقة التالي باختصار شديد (3 نقاط فقط):
    1. ملخص سريع للعرض (الحي، عدد الغرف، السعر).
    2. تقييم السعر بالنسبة للموقع (هل هو مناسب/لقطة/مرتفع).
    3. أهم ميزة في العرض.
    
    الإعلان:
    {sample_apartment}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    # 3. صياغة الرسالة النهائية للتليجرام
    telegram_message = f"🤖 **تحليل رادار جدة الذكي (بواسطة Gemini):**\n\n{response.text}"
    
    # 4. إرسال الرسالة للتليجرام
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=telegram_message, parse_mode='Markdown')

if name == "__main__":
    asyncio.run(analyze_and_send())
