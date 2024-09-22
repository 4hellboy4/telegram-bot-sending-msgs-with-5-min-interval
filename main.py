from bot.utils import schedule_messages
from bot.loader import bot


async def main():
    await bot.start()
    await schedule_messages()


if __name__ == '__main__':
    bot.run(main())
