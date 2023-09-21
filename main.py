import subprocess
import time
from discord.ext import tasks, commands
import discord
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID")) 

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.wait_until_ready()
    send_message.start()

@tasks.loop(seconds=1800)
async def send_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Web sitesi şu anda çalışıyor.")

bot.run(BOT_TOKEN)

while True:
    subprocess.Popen(["/usr/local/bin/python3.10", "test.py"])
    subprocess.Popen(["/usr/local/bin/python3.10", "button.py"])
    subprocess.Popen(["/usr/local/bin/python3.10", "span.py"])
    time.sleep(1800)
