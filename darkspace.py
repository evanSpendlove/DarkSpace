import os
import datetime

from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

FILE_NAME = "timetable.txt"

bot = commands.Bot(command_prefix="!")
timetable = {}

def readTimetable(timetable):
    with open(FILE_NAME, 'r') as f:
        classes = [c.split(' ') for c in f.read().strip().split('\n')]
        for c in classes:
            day, hour = int(c[0]), int(c[1])
            module, link = c[2], c[3]
            timetable[(day, hour)] = (module, link)
    return timetable

def getCurrentTime():
    now = datetime.datetime.now()
    return (now.weekday(), now.hour)

def getClassLink(currentTime):
    module, link = timetable[currentTime]
    msg = f"You've got {module} coming up! Here's the link: {link}"
    return msg

@bot.command(pass_context=True)
async def current_class(ctx):
    currentTime = getCurrentTime()
    msg = getClassLink(currentTime)
    await bot.send_message(ctx.message.channel, msg)

@bot.command(pass_context=True)
async def next_class(ctx):
    day, hour = getCurrentTime()
    currentTime = (day, hour + 1)
    msg = getClassLink(currentTime)
    await bot.send_message(ctx.message.channel, msg)

@bot.event
async def on_ready():
    readTimetable(timetable)
    print(timetable)
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)
