import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("28311539"))
API_HASH = os.getenv("9a7592276f76490009ffadd3f2b2f8a0")
SESSION = os.getenv("AgCqwVKbcndeyXWg5OVJvlkk82dG5zA73Tm5zECCPrs6gk6d6zDa-EoSZfFGgK_ifhEJT85YH-wD0b6QtLU4iNelJYRLKE7UzD82RmTIvbDzxfWuyMvWx4XOBHvLhFq9BGmamLVwm1M1sndWYwBE_8zkCgHL7P9s87RGJ5bge2P9PX6X19mKzKZUy4AZYf1DNp1qnwiARj75tgPjNeOqAqS6VA2yDmxGbEX7GOOuO7btG5DnvehtFt86fXGqCEjtJHsrCid8sf2_V3Soyb1Y0Esv_hDS2pOAtDc7mRQ9r8TcdPNAiAoQb5yXYckLn4QrbKEDtdHMEh_6witYN-oM99sRAAAAAWWMR7cA")
OWNER = os.getenv("bbvvr")
OWNER_NAME = os.getenv("bbvvr")
HNDLR = os.getenv("HNDLR", "$")
PING_PIC = os.getenv("PING_PIC") 
THUMB_PIC = os.getenv("THUMB_PIC")
SUDO_USERS = list(map(int, os.getenv("5990068364").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
