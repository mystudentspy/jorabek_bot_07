from aiogram import Router, types, F
rt = Router()
@rt.message(F.animation)
async def gif(msg: types.Message):
   await msg.answer("bu gif")


