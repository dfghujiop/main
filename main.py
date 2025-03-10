import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен из переменных окружения (лучше, чем хранить в коде)
TOKEN = "7991412640:AAGgSJNF4ry_reu62mJvvKxeWAcD5b2YAaQ@


# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура с кнопками "Да" и "Нет"
age_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Да", callback_data="age_yes")],
        [InlineKeyboardButton(text="❌ Нет", callback_data="age_no")]
    ]
)

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Вам есть 18?", reply_markup=age_keyboard)

@dp.callback_query(F.data == "age_yes")
async def age_confirmed(callback: types.CallbackQuery):
    text = ("Сначала подпишитесь на наших спонсоров\n"
            "t.me/StarsovEarnBot?start=5ia9jc40o\n\n"
            "Инструкция:\n"
            "1. Зайти по ссылке и нажать СТАРТ\n"
            "2. Выполнить задание\n"
            "3. Подтвердить задание\n"
            "4. Отправить скриншот\n"
            "5. Ждать")
    await callback.message.edit_text(text)  # Изменяет предыдущее сообщение
    await callback.answer()  # Закрывает уведомление

@dp.callback_query(F.data == "age_no")
async def age_denied(callback: types.CallbackQuery):
    await callback.message.edit_text("Вы не можете участвовать.")
    await callback.answer()  

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    asyncio.run(main())
