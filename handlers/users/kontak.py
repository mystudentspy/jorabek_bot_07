from aiogram import Router, types, F, filters
rt = Router()
@rt.message()
async def kontak(msg: types.Message):
   if msg.contact:
      c = msg.contact
      n = "barcha malumotlar:\n"
      n += f"{c.first_name} {c.last_name}\n"
      n += f"{c.phone_number}"
      await msg.answer(n)
      if msg.contact.user_id == msg.from_user.id:
         await msg.answer("bu rostdan sizniki")
      else:
         await msg.answer("bu boshqa insonni nomer")
