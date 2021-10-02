import discord
from discord.ext import commands
from discord.reaction import Reaction
from discord import User
import asyncio

class Commands(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, name = "clhzVQtPmGORFaiLBlsK"):
        author = ctx.message.author

        if name != "clhzVQtPmGORFaiLBlsK":
            await ctx.send(f"Hi {name}")
            await ctx.send("How are you ")
        else:
            await ctx.send(f"Hi {author.name}")
            await ctx.send("How are you")

    @commands.command()
    async def sad(self, ctx):
        def checkvalid(reaction : Reaction, user : User):
            return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id
    
        await ctx.send("Now hush little baby don't you cry")
        place = await ctx.send("Everythings gonna be alright")
        await place.add_reaction("😭")

        reaction, user = await self.bot.wait_for(event = "reaction_add", check = checkvalid)
        if reaction.emoji == "😭":
            await ctx.send("Nice you reacted")

    @commands.command()
    async def reactme(self, ctx):
        def checkvalid(reaction : Reaction, user : User):
            return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id
        await ctx.send("Quick! React to this message!")
        
        try:
            reaction, user = await self.bot.wait_for(event = 'reaction_add', check = checkvalid, timeout = 10.0)
        except asyncio.TimeoutError:
            await ctx.send("noob can't even add reaction in 10 sec")
            return
        else:
            await ctx.send("You reacted in time!")

    @commands.command()
    async def name(self, ctx, name: str):
        await ctx.send(f"Hi! `{name}`\nMy name is \nWhat? \nMy name is \nWho? \nMy name is \nChika-chika \nSlim Shady")

    @commands.command()
    async def hw(self, ctx):
        
        await ctx.send("Ew!")
        await ctx.send("I hate homework")
        await ctx.send("Disgusting")

    @commands.command()
    async def rh(self, ctx):
        await ctx.send("raised")

def setup(bot):
    bot.add_cog(Commands(bot))
