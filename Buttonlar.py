from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🥋 Ro'yxatdan o'tish")],
        [KeyboardButton("📋 Ro'yxatdan o'tganlar")],
        [KeyboardButton("📈 Yutuqlarni kuzatish")],
    ],
    resize_keyboard=True
)
