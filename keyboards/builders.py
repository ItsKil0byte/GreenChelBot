from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.subloader import get_json

def shop_generator():
    items = get_json("products.json")

    builder = InlineKeyboardBuilder()
    [builder.button(text=item[0], url=item[1]) for item in items]

    return builder.as_markup()
