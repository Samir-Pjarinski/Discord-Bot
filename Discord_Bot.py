#Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os, random

#Variables
load_dotenv(os.path.join(os.getcwd(), ".env"))
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
bot = commands.Bot(command_prefix = f"{PREFIX} ")

#Bot OnReady Event
@bot.event
async def on_ready():
    print("logged on as")
    print(bot.user.name)
    print(bot.user.id)
    print("---------")
    await bot.change_presence(status="online")
    load_extensions()
    global online
    online = True

#Removes the help command
@bot.remove_command("help")

@bot.event
async def on_command_error(ctx, error):
    
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command does not exist")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}") 
    await ctx.send(f"Loaded extension '{extension}'")
    print(f"Loaded extension '{extension}'")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}") 
    await ctx.send(f"Unloaded extension '{extension}'") 
    print(f"Unloaded extension '{extension}'") 

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}") 
    bot.load_extension(f"cogs.{extension}") 
    await ctx.send(f"Reloaded extension '{extension}'")
    print(f"Reloaded extension '{extension}'")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Your ping is: {int(bot.latency * 1000)}ms")

def load_extensions():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

#Bot Run Event
bot.run(TOKEN)