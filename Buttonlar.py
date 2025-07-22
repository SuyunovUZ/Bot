from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="👥 Register Athlete", callback_data="register")
    builder.button(text="📋 List Athletes", callback_data="list")
    builder.button(text="📈 Progress", callback_data="progress")
    builder.button(text="📢 Broadcast", callback_data="broadcast")
    builder.adjust(2)
    return builder.as_markup()
