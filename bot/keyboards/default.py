from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="📚 Новая задача")],
        [KeyboardButton(text="❓ Вопрос по обучению")],
        [KeyboardButton(text="📈 Статистика")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
