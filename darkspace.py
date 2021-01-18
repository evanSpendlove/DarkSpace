import os
import datetime

from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
FILE_NAME = "timetable.txt"

timetable = {}
bot = commands.Bot(command_prefix="!")

def readTimetable(timetable):
    with open(FILE_NAME, 'r') as f:
        classes = f.read().strip().split('\n')
    for c in classes:
        day, hour, module, link = c.split(',')
        timetable[(int(day), int(hour))] = (module, link)
    return timetable

def getCurrentTime():
    now = datetime.datetime.now()
    return (now.weekday(), now.hour)

def getClassLink(currentTime):
    if currentTime not in timetable:
        return "You got no class coming up, enjoy the break!"
    module, link = timetable[currentTime]
    msg = f"You've got {module} coming up! Here's the link: {link}"
    return msg

@bot.command(pass_context=True)
async def currentClass(ctx):
    await ctx.send(getClassLink(getCurrentTime()))

@bot.command(pass_context=True)
async def nextClass(ctx):
    day, hour = getCurrentTime()
    currentTime = (day, hour + 1)
    await ctx.send(getClassLink(currentTime))

@bot.event
async def on_ready():
    readTimetable(timetable)
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)
