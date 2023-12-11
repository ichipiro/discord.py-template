import os
from dotenv import load_dotenv


load_dotenv()
EXTENTIONS = [
    # extentions here
    "cogs.ping",
]
TOKEN = os.environ["TOKEN"]
