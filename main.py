import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from config.settings import BOT_TOKEN
from handlers.users.test import rt as test
from handlers.users.start import rt as start
from handlers.users.help import rt as help
from handlers.users.rasm import rt as rasm
from handlers.users.me import rt as me
from handlers.users.chat_id import rt as chat_id
from handlers.users.date import rt as soat
from handlers.users.photo import rt as photo
from handlers.users.voice import rt as ovoz
from handlers.users.stiker import rt as stiker
from handlers.users.dice import rt as dice
from handlers.users.location import rt as manzil
from handlers.users.gif import rt as gif
from handlers.users.text import rt as text
from handlers.users.contak import rt as nomer
from handlers.users.kontak import rt as kontak
from handlers.users.hamma_kod import rt as kodlar
dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(start)
    dp.include_router(help)
    dp.include_router(rasm)
    dp.include_router(me)
    dp.include_router(soat)
    dp.include_router(chat_id)
    dp.include_router(photo)
    dp.include_router(ovoz)
    dp.include_router(stiker)
    dp.include_router(dice)
    dp.include_router(manzil)
    dp.include_router(gif)
    # dp.include_router(text)
    dp.include_router(nomer)
    # dp.include_router(kodlar)
    dp.include_router(kontak)





    dp.include_router(test)



    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga yo'q")
    except TelegramUnauthorizedError:
        print("token xato!")
