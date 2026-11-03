# from aiogram import Router, types,filters
# rt = Router()
# @rt.message()
# async def chat(msg: types.Message):
#     if msg.new_chat_members:
#         ism = msg.new_chat_members[0].first_name
#         n = f"guruh {ism} xush kelibsiz!"
#         await msg.reply(n)
#         print(msg.from_user.first_name)




from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold

rt = Router()


@rt.message(F.new_chat_members)
async def welcome_new_members(msg: types.Message):

    group_name = msg.chat.title or "Guruh"

    for member in msg.new_chat_members:

        # Botlarni o'tkazib yuborish
        if member.is_bot:
            continue

        ism = member.full_name

        text = (
            f" Assalomu alaykum, {hbold(ism)}!\n\n"
            f" {hbold(group_name)} guruhiga "
            f"xush kelibsiz!\n\n"
            f" Sizga maroqli vaqt va "
            f"yaxshi suhbatlar tilaymiz!\n\n"
            f" Guruhimizga xush kelibsiz!"
        )

        await msg.answer(
            text,
            parse_mode=ParseMode.HTML
        )

        print(
            f"Yangi a'zo: {ism} | "
            f"ID: {member.id}"
        )

