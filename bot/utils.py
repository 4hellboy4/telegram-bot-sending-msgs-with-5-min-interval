import asyncio
from datetime import datetime, timedelta

from dotenv import load_dotenv

from bot.loader import bot
import os

load_dotenv()


async def schedule_messages() -> None:
    try:
        channels: list[str] = await get_channels()
        for i in range(0, len(channels)):
            # время через которое должно отправиться сообщение
            schedule_time = datetime.now() + timedelta(minutes=(i + 1) * 5)
            await bot.send_message(
                chat_id=os.getenv('USER'),
                text=f'/add_group <a href="{channels[i]}">{channels[i]}</a>',
                schedule_date=schedule_time,
            )
            # время задержки между отправкой запланированных сообщений
            await asyncio.sleep(25)
    except Exception as e:
        print(e)


# собираем все группы телеграмм для отправки
async def get_channels() -> list[str]:
    try:
        with open('./data/channels.txt', 'r', encoding='utf-8') as f:
            channels = f.read().splitlines()
            for elem in channels:
                print(elem)
        return channels
    except Exception as e:
        print('Something went wrong while sending messages')
        return []
