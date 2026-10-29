from aiogram import Router, types, F
rt = Router()
@rt.message(F.sticker)
async def stiker(msg: types.Message):
   await msg.answer("bu stiker")