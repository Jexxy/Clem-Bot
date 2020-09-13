import discord
import os.path
import random
from command import setup
from discord.ext import commands

###############################################################################################
# Creating an instant of commands.bot, removes the default help command, and calls the setup. #
###############################################################################################
# Gets the token from token.txt, makes an instance of commands.bot with a command prefix, then calls stup()

t = open("token.txt", "r")
TOKEN = t.read()
t.close()
bot = commands.Bot(command_prefix='--')
bot.remove_command('help')
setup(bot)

###################
# Meat of Main.py #
###################

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await bot.change_presence(activity = discord.Game('--help'))

@bot.event
async def on_command_error(ctx, error):
    err = getattr(error, "original", error)
    if isinstance(err, commands.CommandNotFound):
        return

bot.run(TOKEN)

