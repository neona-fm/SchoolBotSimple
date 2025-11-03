from aiogram import types
from bot.loader import dp
from bot.utils.user_data import PENDING_TASKS

@dp.message(lambda m: m.text and m.text.strip().isdigit())
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    user_input = message.text.strip()

    if user_id not in PENDING_TASKS:
        await message.answer("🤔 Я не задавал тебе задачу. Нажми '📚 Новая задача'.")
        return

    correct_answer = PENDING_TASKS.pop(user_id)  # Удаляем после ответа

    if user_input == correct_answer:
        await message.answer("✅ Правильно! Хочешь ещё одну?")
    else:
        await message.answer(f"❌ Неправильно. Правильный ответ был: <b>{correct_answer}</b>", parse_mode="HTML")
