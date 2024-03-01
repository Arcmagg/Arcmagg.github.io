from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot =Bot('token')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    markup.add(types.KeyboardButton('Войти в VK', web_app=WebAppInfo(url='https://vk.com/headdesigner')))
    await message.answer('тут вы можете слушать музыку без подписки',reply_markup=markup)




executor.start_polling(dp)
