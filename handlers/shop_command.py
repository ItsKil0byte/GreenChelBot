from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.builders import shop_generator

router = Router()


@router.message(Command("shop"))
async def shop(message: Message):
    await message.answer(
        text="Здесь будет информация о балансе пользователя и товарах от партнеров.",
        reply_markup=shop_generator(),
    )
