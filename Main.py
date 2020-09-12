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
bot.change_presence()
command.setup(bot)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await bot.change_presence(status=discord.Status.online, activity= discord.Game('Playing hide and seek!'))


bot.run(TOKEN)

