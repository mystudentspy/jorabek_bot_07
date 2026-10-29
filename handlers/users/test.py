from aiogram import Router, types
rt = Router()
@rt.message()
async def test(msg: types.Message):
    if msg.text:
        await msg.answer(str(msg.text))
