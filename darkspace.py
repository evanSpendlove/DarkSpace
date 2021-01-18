import os
import datetime

from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
FILE_NAME = "timetable.txt"
HOURS_PER_DAY = 24
DAYS_PER_WEEK = 5

timetable = [[None for h in range(HOURS_PER_DAY)] for d in range(DAYS_PER_WEEK)]
bot = commands.Bot(command_prefix="!")

def readTimetable(timetable):
    with open(FILE_NAME, 'r') as f:
        classes = f.read().strip().split('\n')
        for c in classes:
            day, hour, module, link = c.split(',')
            timetable[int(day)][int(hour)] = (module, link)
    return timetable

def search(day, hour):
    while hour < HOURS_PER_DAY and timetable[day][hour] is None:
        hour += 1
    if hour == HOURS_PER_DAY:
        return None
    return timetable[day][hour]

def formatMessage(details, search=False):
    if details is None:
        if search:
            return "You've got no more class today, time to game!"
        else:
            return "You've got no class right now, use \"!nextClass\" to find your next class today."
    else:
        return f"You've got a class for {details[0]}! Here's the link: {details[1]}"

def getCurrentTime():
    now = datetime.datetime.now()
    return now.weekday(), now.hour

def getDetails(day, hour):
    return timetable[day][hour]

@bot.command(pass_context=True)
async def currentClass(ctx):
    day, hour = getCurrentTime()
    await ctx.send(formatMessage(getDetails(day, hour)))

@bot.command(pass_context=True)
async def nextClass(ctx):
    day, hour = getCurrentTime()
    await ctx.send(formatMessage(search(day, hour + 1), search=True))

@bot.event
async def on_ready():
    readTimetable(timetable)
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)
