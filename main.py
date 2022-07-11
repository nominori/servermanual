from aiogram import Bot, Dispatcher, executor, types  # Імпорт потрібних модулів

TOKEN = ''  # Токен вашого бота який ви отримали від BotFather
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    text = f"Ти написав: {message.text}"
    await message.reply(text=text)

# Для прикладу ось метод який відправляє користувачу його ж повідомлення


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # А це дозволить боту працювати без зупинки
