from aiogram import types
from bot.loader import dp
from bot.utils.questions import generate_task
from pathlib import Path
import json

FAQ_PATH = Path("bot/data/faq.json")

@dp.message(lambda m: m.text == "📚 Новая задача")
async def menu_task(message: types.Message):
    question, answer = generate_task()
    await message.answer(f"Реши:\n\n<b>{question}</b>", parse_mode="HTML")

@dp.message(lambda m: m.text == "❓ Вопрос по обучению")
async def menu_faq(message: types.Message):
    if FAQ_PATH.exists():
        with open(FAQ_PATH, encoding="utf-8") as f:
            faq_data = json.load(f)
    else:
        faq_data = {}

    if not faq_data:
        await message.answer("❌ FAQ пока пустой.")
        return

    text = "<b>Часто задаваемые вопросы:</b>\n\n"
    for q, a in faq_data.items():
        text += f"❓ <b>{q}</b>\n🟢 {a}\n\n"
    await message.answer(text.strip(), parse_mode="HTML")

@dp.message(lambda m: m.text == "📈 Статистика")
async def menu_stats(message: types.Message):
    await message.answer("📊 Статистика будет позже. Сейчас пока заглушка.")

@dp.message(lambda m: m.text.lower() in {"да", "ещё", "хочу ещё", "давай ещё", "давай", "ещё одну"})
async def send_another_task(message: types.Message):
    from bot.utils.questions import generate_task
    from bot.utils.user_data import PENDING_TASKS

    question, answer = generate_task()
    PENDING_TASKS[message.from_user.id] = answer.strip()

    await message.answer(f"Окей, вот новая задача:\n\n<b>{question}</b>", parse_mode="HTML")

