import os
from discord.ext import commands
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from test import test_site
import discord
from span import test_signup_button
from pricing import test_pricing_button
from login import test_login_button
from startButton import test_google_button
from emailControl import selenium_test_email
from demo import selenium_test_demo_button
from discord import Embed
from datetime import datetime


load_dotenv()
scheduler = AsyncIOScheduler()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    if not scheduler.running:
        scheduler.start()


async def send_error(channel, filename):
    await channel.send(file=discord.File(filename))
    


async def send_message():
    all_works = True
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        test_result, screenshot_path = test_site()
        final_message1 = test_result

        if "WebSite is working well" not in test_result:
           
            await channel.send(final_message1)
            if screenshot_path: 
                all_works = False
                await send_error(channel, screenshot_path)
        

        signup_result, signup_screenshot_path = test_signup_button()
        final_message3 = signup_result

        if "Sign Up button works well" not in signup_result:
            
            await channel.send(final_message3)
            if signup_screenshot_path:  
                all_works=False
                await send_error(channel, signup_screenshot_path)
        

        login_result, login_screenshot_path = test_login_button()
        final_message4 = login_result

        if "Login button works well" not in login_result:
            await channel.send(final_message4)
            if login_screenshot_path:  
                all_works=False
                await send_error(channel, login_screenshot_path)
        

        pricing_result, pricing_screenshot_path = test_pricing_button()
        final_message5 = pricing_result

        if "Pricing button works well" not in pricing_result:
            await channel.send(final_message5)
            if pricing_screenshot_path: 
                all_works=False 
                await send_error(channel, pricing_screenshot_path)
        

        google_result, google_screenshot_path = test_google_button()
        final_message6 = google_result

        if "Google button works well" not in google_result: 
            await channel.send(final_message6)
            if google_screenshot_path:  
                all_works=False
                await send_error(channel, google_screenshot_path)
        
        
        email_result, email_screenshot_path =  selenium_test_email()
        final_message7 = email_result

        if "Email button works well" not in email_result:
            await channel.send(final_message7)
            if email_screenshot_path: 
                all_works=False 
                await send_error(channel, email_screenshot_path)
        

        demo_result, demo_screenshot_path =  selenium_test_demo_button()
        final_message8 = demo_result

        if "Demo , mic and camera buttons are works well" not in demo_result:
            
            await channel.send(final_message8)
            if demo_screenshot_path:  
                all_works=False
                await send_error(channel, demo_screenshot_path)
        

        if all_works:
                
            embed = Embed(title="Total Test Result", description="All tests passed!", color=0x00ff00)  # 0x00ff00 yeşil renktir.
            embed.add_field(name="Status", value="No problem on Perculus", inline=False)
            await channel.send(embed=embed)



async def sendError():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        test_result, screenshot_path = test_site()
        final_message1 = test_result

        if "WebSite is working well" not in test_result:
            await channel.send(final_message1)
            if screenshot_path: 
                await send_error(channel, screenshot_path)  


        signup_result, signup_screenshot_path = test_signup_button()
        final_message3 = signup_result

        if "Sign Up button works well" not in signup_result:
            await channel.send(final_message3)
            if signup_screenshot_path:  
                await send_error(channel, signup_screenshot_path)

        pricing_result, pricing_screenshot_path = test_pricing_button()
        final_message4 = pricing_result

        if "Pricing button works well" not in pricing_result:
            await channel.send(final_message4)
            if pricing_screenshot_path:  
                await send_error(channel, pricing_screenshot_path)

        
        login_result, login_screenshot_path = test_login_button()
        final_message5 = login_result

        if "Login button works well" not in login_result:
            await channel.send(final_message5)
            if login_screenshot_path:  
                await send_error(channel, login_screenshot_path)

        google_result, google_screenshot_path = test_google_button()
        final_message6 = google_result

        if "Google button works well" not in google_result:
            await channel.send(final_message6)
            if google_screenshot_path:  
                await send_error(channel, google_screenshot_path)

        email_result, email_screenshot_path =  selenium_test_email()
        final_message7= email_result

        if "Email button works well" not in email_result:
            await channel.send(final_message7)
            if email_screenshot_path:  
                await send_error(channel, email_screenshot_path)

        demo_result, demo_screenshot_path =  selenium_test_demo_button()
        final_message8= demo_result

        if "Demo , mic and camera buttons are works well" not in demo_result:
            await channel.send(final_message8)
            if demo_screenshot_path:  
                await send_error(channel, demo_screenshot_path)


scheduler.add_job(send_message, 'cron', hour=11,minute=50)  
scheduler.add_job(send_message, 'cron', hour=16,minute=54)  
scheduler.add_job(send_message, 'cron', hour=21,minute=5)
scheduler.add_job(sendError, 'interval', minutes=10)


bot.run(BOT_TOKEN)
