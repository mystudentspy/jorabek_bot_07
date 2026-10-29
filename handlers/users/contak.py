from aiogram import Router, types, F
rt = Router()
@rt.message(F.contact)
async def nomer(msg: types.Message):
   await msg.answer("bu nomer")

