from pyrogram import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")
login = os.getenv("LOGIN")

bot = Client(name='schedule_bot', api_id=api_id, api_hash=api_hash, phone_number=phone)
