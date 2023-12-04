from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("trash"))
async def trash(message: Message):
    await message.answer("Здесь будет заявка по сбору мусора.")
