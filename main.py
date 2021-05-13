# Clientbot : 841946101493923851
# Token : ODQxOTQ2MTAxNDkzOTIzODUx.YJuJaQ.YrK9ExapUWCqGrh5Zws-KG59HiY
# Permission : https://discord.com/api/oauth2/authorize?client_id=841946101493923851&permissions=452672&scope=bot

import discord
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

from discord.ext import commands
from datetime import datetime, timedelta

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Mibot Help", description="All available bot commands", color=0x42f5a7)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="send", value="Send Hallo message to user", inline=False)
    await ctx.channel.send(embed=emBed)

@bot.command()
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send("Hello")

@bot.event
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == '!logout':
        await bot.logout()
    await bot.process_commands(message)

bot.run("ODQxOTQ2MTAxNDkzOTIzODUx.YJuJaQ.YrK9ExapUWCqGrh5Zws-KG59HiY")