from aiogram.fsm.state import StatesGroup, State


class TrashReport(StatesGroup):
    description = State()
    location = State()
    photo = State()
