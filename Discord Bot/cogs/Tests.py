import discord
from discord.ext import commands
from datetime import datetime

class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["embed"])
    async def embedex(self, ctx):
        
        embedvariable = discord.Embed(title="Funny Embed", description="Insert Funny", colour=ctx.author.colour, timestamp = datetime.utcnow())
        embedvariable.add_field(name="Funny 1", value="How many dog", inline=False)
        embedvariable.add_field(name="Funny 2", value="Cat Video", inline=True)
        embedvariable.add_field(name="Funny 3", value="Parrot Video", inline=True)
        embedvariable.add_field(name="Funny 3", value="Parrot Video", inline=True)
        embedvariable.add_field(name="Funny 3", value="Parrot Video", inline=True)
        embedvariable.set_footer(text="This is the footer", icon_url="https://img.icons8.com/material-sharp/24/000000/link--v2.png")
        embedvariable.set_image(url="https://img.icons8.com/material-sharp/24/000000/link--v2.png")
        await ctx.send(embed=embedvariable) 

def setup(bot):
    bot.add_cog(Tests(bot))
