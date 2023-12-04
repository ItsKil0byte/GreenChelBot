import asyncio

from aiogram import Bot, Dispatcher

from handlers import start_command, trash_command, about_command, shop_command

from config_loader import config


async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        start_command.router,
        trash_command.router,
        about_command.router,
        shop_command.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
