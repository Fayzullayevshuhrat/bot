import asyncio
import json
import logging
import sys
from email import message
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


from config import TOKEN



dp = Dispatcher()





@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Nice try!")

@dp.message(F.text.isdigit())
async  def get_user_data(message:Message):
    with open("users.json", "r") as file:
        users = json.load(file)
    await message.answer(json.dumps(users[message.text]))


@dp.message()
async def shuhrat(message:Message):
    await message.answer(message.text)
    if "assalomu aleykum" in message.text:
        await message.answer("Va alaykum assalom!")
    else:
        await message.answer(message.text)





async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())