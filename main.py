import logging
from aiogram import types
from config import dp, bot, ADMIN_ID
from Buttonlar import main_menu

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        await bot.send_message(
            ADMIN_ID,
            f"👤 Foydalanuvchi botni ishga tushirdi:\n"
            f"ID: {message.from_user.id}\n"
            f"Username: @{message.from_user.username}\n"
            f"Full Name: {message.from_user.full_name}"
        )
    except Exception as e:
        print(f"[ERROR] Admin message failed: {e}")

    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}!\n"
        "🏆 Kickboxing bo'yicha ro'yxatdan o'tish botiga xush kelibsiz!",
        reply_markup=main_menu
    )

@dp.message_handler(lambda msg: msg.text == "🥋 Ro'yxatdan o'tish")
async def register_user(message: types.Message):
    await message.answer("📝 Ismingizni yozing... (Demo versiya, ishlanmoqda)")

@dp.message_handler(lambda msg: msg.text == "📋 Ro'yxatdan o'tganlar")
async def list_users(message: types.Message):
    await message.answer("📄 Ro'yxatdan o'tganlar ro'yxati (Demo versiya).")

@dp.message_handler(lambda msg: msg.text == "📈 Yutuqlarni kuzatish")
async def track_progress(message: types.Message):
    await message.answer("📊 Yutuqlarni kuzatish (Demo versiya).")
import asyncio

if __name__ == "__main__":
    print("Bot is starting...")
    asyncio.run(main())
