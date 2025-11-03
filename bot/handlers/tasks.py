from aiogram import types
from bot.loader import dp
from bot.utils.questions import generate_task
from bot.utils.user_data import PENDING_TASKS

@dp.message(lambda m: m.text and "задача" in m.text.lower())
async def send_task(message: types.Message):
    question, answer = generate_task()

    # Сохраняем правильный ответ в память
    PENDING_TASKS[message.from_user.id] = answer.strip()

    await message.answer(f"Реши:\n\n<b>{question}</b>", parse_mode="HTML")
