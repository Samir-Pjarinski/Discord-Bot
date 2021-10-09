import discord
from discord.ext import commands


class Author(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def author(self, ctx):
        
        author = ctx.message.author
        await ctx.send("Hello " + str(author.mention))

    @commands.command()
    async def pfp(self, ctx):
        
        author = ctx.message.author
        await ctx.send(str(author.avatar_url))

    @commands.command()
    async def location(self, ctx):
        channel = ctx.message.channel
        server = ctx.message.guild
        await ctx.send("Wow this is the " + str(channel) + " chanel in the " + str(server) + " server")

def setup(bot):
    bot.add_cog(Author(bot))
