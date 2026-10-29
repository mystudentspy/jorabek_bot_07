from aiogram import Router, types, F
rt = Router()
@rt.message(F.voice)
async def ovoz(msg: types.Message):
   await msg.answer("bu ovoz")


