import discord
import os.path
import random
import command
import praw
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
command.setup(bot)

##################################
# Creating an instance of reddit #
##################################
# Gets the client secret from Redditsecret.txt, makes an instance of reddit

t = open("Redditsecret", "r")
client_secret1 = t.read()
t.close
reddit = praw.Reddit(client_id="k8NE3qqhrsUOCg",
                     client_secret=client_secret1,
                     user_agent="windows:Clem_Bot_Meme_Command:v0.1 (by /u/TheJexxyBoi):python3:PRAW")

###################
# Meat of Main.py #
###################

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'You connection with reddit is {reddit.read_only}')
    await bot.change_presence(activity = discord.Game('--help'))

@bot.event
async def on_command_error(ctx, error):
    err = getattr(error, "original", error)
    if isinstance(err, commands.CommandNotFound):
        return

bot.run(TOKEN)

