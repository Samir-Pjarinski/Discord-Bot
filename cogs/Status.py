import discord
from discord.ext import commands

class Status(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def online(self, ctx):
        
        await ctx.send("And we're back")
        await self.bot.change_presence(status="online")

    @commands.command()
    async def offline(self, ctx):

        await ctx.send("https://tenor.com/view/hooray-its-weekend-ok-bye-ciao-slide-gif-15739082")
        await self.bot.change_presence(status="invisible")

    @commands.command()
    async def creep(self, ctx, who = "WMqiksNuwSgoXZjneztL"):
    
        if who != "WMqiksNSuwSgoXZjneztL":
            await self.bot.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name=who))
            await ctx.send(f"Now watching {who}")
        else:
            await self.bot.change_presence(status="idle", activity=discord.Activity(type=discord.ActivityType.watching, name="You"))
            await ctx.send("Now watching you")

    @commands.command()
    async def clear(self, ctx):
        await self.bot.change_presence(status="online")

def setup(bot):
    bot.add_cog(Status(bot))
