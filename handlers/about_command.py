from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("about"))
async def about(message: Message):
    await message.answer(
        "Здесь будет основная информация о назначении бота и его командах."
    )
