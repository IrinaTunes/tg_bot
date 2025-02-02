from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7367979722:AAFW1jA5ixxxXwhyQ1dfSW0dA9p1DztiTtU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бот')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот')

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе с ..... ')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)