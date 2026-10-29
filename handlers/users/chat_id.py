from aiogram import Router,filters,types
from pyexpat.errors import messages

rt = Router()
@rt.message(filters.Command("id_korish"))
async def chat_id(msg:types.Message):
    await msg.answer(f"sizning id raqamingiz:{msg.from_user.id}")




