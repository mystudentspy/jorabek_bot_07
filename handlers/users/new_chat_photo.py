from aiogram import Router, F
from aiogram.types import Message

rt = Router()

@rt.message(F.new_chat_photo)
async def photo(message: Message):
    await message.reply("Guruh profili uchun yangi rasm qoyildi!!")

