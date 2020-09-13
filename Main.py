import discord
import os.path
import random
import command
from discord.ext import commands
t = open("token.txt", "r")
TOKEN = t.read()
t.close()
bot = commands.Bot(command_prefix='--')
bot.remove_command('help')
command.setup(bot)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await bot.change_presence(activity = discord.Game('--help'))


bot.run(TOKEN)

