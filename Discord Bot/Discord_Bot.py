#Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os, random

#Variables
load_dotenv(os.path.join(os.getcwd(), '.env'))
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
bot = commands.Bot(command_prefix = PREFIX + " ")
online = True
check = False

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

@bot.command()
async def meme(ctx):

    memes = [
        "https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043", 
        "https://i.pinimg.com/originals/e3/2c/e7/e32ce76b21b7953e0badb1eceffff524.jpg", 
        "https://media-assets-03.thedrum.com/cache/images/thedrum-prod/s3-news-tmp-349138-meme7--default--1050.png", 
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_HyGoBdwM_CYB2F20uM4sEPI0AH-st6eAEA&usqp=CAU", 
        "https://tenor.com/view/relatable-cat-funny-animals-wifi-gif-14384030"
        ]

    await ctx.send(random.choice(memes))

@bot.command() 
async def maths(ctx, firstnumber: float, operator: str, secondnumber: float, rond = "pdWMycpOtPBottZRtJFu", dp = "HTmvVPwywbOsgmLZmrbx"):
    if operator == "+":
        result = firstnumber + secondnumber
        round_bool = False

    elif operator == "-":
        result = firstnumber - secondnumber
        round_bool = False

    elif operator == "/":
        result = firstnumber / secondnumber
        round_bool = False

        if rond != "pdWMycpOtPBottZRtJFu" and dp == "HTmvVPwywbOsgmLZmrbx":
            round_result = round(result, 1)
            round_bool = True

        elif rond != "pdWMycpOtPBottZRtJFu" and dp != "HTmvVPwywbOsgmLZmrbx":
            round_result = round(result, int(dp))
            round_bool = True

    elif operator == "*":
        result = firstnumber * secondnumber
        round_bool = False

        if rond != "pdWMycpOtPBottZRtJFu" and dp == "HTmvVPwywbOsgmLZmrbx":
            round_result = round(result, 1)
            round_bool = True

        elif rond != "pdWMycpOtPBottZRtJFu" and dp != "HTmvVPwywbOsgmLZmrbx":
            round_result = round(result, int(dp))
            round_bool = True

    elif operator == "^":
        result = firstnumber ** secondnumber
        round_bool = False

    elif operator == "%":
        result = firstnumber % secondnumber
        round_bool = False

    else:
        result = "That is not an accpted arithmatic operator"

    if round_bool == True:
        await ctx.send(round_result)
    else:
        await ctx.send(result)

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