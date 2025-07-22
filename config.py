from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "8087444949:AAHfanBiKddIK08U3LVUUbl-e_8EPCBTZPs"
ADMIN_ID = 6044283939

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
