import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import *
from aiogram.utils import executor

from config import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

#без фильтра
@dp.message_handler(commands='tag2')
async def _(msg: Message):
    wss = msg.get_args().split(',')
    for el in wss:
        dsd = el.replace(' ', '+')
        qq = open('txt.txt', 'a+')
        qq.write(f'https://www.youtube.com/results?search_query={dsd}')
        qq.write('\n')
    await msg.answer_document(open('txt.txt', 'rb'))
    qq = open('txt.txt', 'a+')
    qq.close()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'txt.txt')
    os.remove(path)

#с фильтром за последний час
@dp.message_handler(commands='tag1')
async def _(msg: Message):
    wss = msg.get_args().split(',')
    for el in wss:
        dsd = el.replace(' ', '+')
        qq = open('txt.txt', 'a+')
        qq.write(f'https://www.youtube.com/results?search_query={dsd}&sp=EgIIAQ%253D%253D')
        qq.write('\n')
    await msg.answer_document(open('txt.txt', 'rb'))
    qq = open('txt.txt', 'a+')
    qq.close()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'txt.txt')
    os.remove(path)


if __name__ == '__main__':
    executor.start_polling(dp)
