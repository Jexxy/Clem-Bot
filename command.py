import discord
import utilities
import os
from discord.ext import commands



class Command(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello! You ready to do somthing with your life?')
    

    @commands.command()
    async def help(self, ctx):
        await ctx.send('''
    --ping :: See if Clem is awake!
    --roll (Amount of dice D number of sides on the dice) :: Clem likes the click clack noises!
    --stats :: Clem decides your characters fate!!!
    --create :: Creates an account at clems bank!
    --add [mention the player] [amount to add]:: DM use Only!! Adds clemy moneys to a given users account. 
    --bal :: Clem will tell you the amount of moneys you have!!
    ''')


    @commands.command()
    async def roll(self, ctx, inp):
        try:
            roll_dice = await utilities.roll_dice(inp,ctx)
            await ctx.send(roll_dice)
        except ValueError:
            await ctx.send("Somthing went wrong!!!!")


    @commands.command()
    async def bal(self, ctx):
        userPath = str(ctx.author.id) + ".txt"
        if os.path.isfile(userPath):
            op = open(userPath, "r+")
            read = op.read()
            await ctx.send(f"You have {read} moneys in your account!")
        else:
            await ctx.send("You dont have an account dummy!!! Type --create")


    @commands.command()
    async def add(self, ctx, user, ammount):
    #user[3:-1]
        if ctx.message.author.guild_permissions.administrator:
            added_ammount = 0
            userPath = str(user[3:-1]) + ".txt"
            if os.path.isfile(userPath):
                #reading the ammount in the file
                op = open(userPath, "r+")
                added = op.read()
                added_ammount += int(ammount) + int(added)
                op.close()
                #writing the new ammount to the file
                op1 = open(userPath, "w+")
                op1.write(str(added_ammount))
                await ctx.send(f"I have added {ammount} to your account! Your new balance is {added_ammount} ")
                op1.close()
            else:
                await ctx.send('You dont have an account! Please Type "--create" ')
        else:
            await ctx.send("Cheater!!!!!!")


    @commands.command()
    async def stats(self, ctx):
        await ctx.send(utilities.create_stats())

    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!!! *Happy bird noises*')


    @commands.command()
    async def create(self, ctx):
        userPath = str(ctx.author.id) + ".txt"
        if os.path.isfile(userPath):
            await ctx.send("You already have an account, cheater!!")
        else:
            await ctx.send("Creating...")
            f = open(userPath, "w+")
            f.write("0")
            await ctx.send("Created!")
            f.close()
    


def setup(bot):
    bot.add_cog(Command(bot))