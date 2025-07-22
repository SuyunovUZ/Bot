from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from buttons import main_menu
from config import TOKEN, ADMIN_ID
import asyncio
import logging

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

# Start command
@dp.message(commands=["start"])
async def start_handler(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("<b>Welcome, Coach!</b> 👊", reply_markup=main_menu())
    else:
        await message.answer("<b>Welcome to Khayriddinov Kickboxing Club 🥊</b>", reply_markup=main_menu())

# Default
@dp.message()
async def fallback(message: Message):
    await message.answer("Please use the menu buttons.")

async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
