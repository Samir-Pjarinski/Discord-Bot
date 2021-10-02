import discord
from discord.ext import commands

class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name = "help", invoke_without_command=True)
    async def helpcmd(self, ctx):
        
        await ctx.send("Chosose page with, .sa help *page number*")
    
    
    @helpcmd.command(name="page_1", aliases=["1"])
    async def help_page_1(self, ctx):
    
        embedvariable = discord.Embed(title="", description="", colour=0x0000FF)
        embedvariable.set_author(name="Help (.sa)")

        embedvariable.add_field(name="8ball", value="Type a question and it will answer it", inline=False)
        embedvariable.add_field(name="author", value="Mentions the author", inline=False)
        embedvariable.add_field(name="clear", value="Sets the bot's status to online, and clears any activities", inline=False)
        embedvariable.add_field(name="creep", value="Sets the bot's status to idle, can be inputted with a name", inline=False)
        embedvariable.add_field(name="embedex", value="Embed test", inline=False)
        embedvariable.add_field(name="game", value="Starts a number guessing game", inline=False)
        embedvariable.add_field(name="hello", value="Sends you a message, can be inputted with a name", inline=False)
        embedvariable.add_field(name="hw", value="Sends you a message", inline=False)
        embedvariable.add_field(name="location", value="Sends the channel name and the server name", inline=False)
        embedvariable.add_field(name="maths", value="You enter a number, an arithmatical operator, and \nanother number and it gives you the result", inline=False)
        embedvariable.add_field(name="meme", value="Sends you a random meme", inline=False)

        embedvariable.set_footer(text="Page 1, use .sa help *page number* to select another page")
        await ctx.send(embed=embedvariable) 
    
    @helpcmd.command(name="page_2", aliases=["2"])
    async def help_page_2(self, ctx):
    
        embedvariable = discord.Embed(title="", description="", colour=0x0000FF)
        embedvariable.set_author(name="Help (.sa)")

        embedvariable.add_field(name="name", value="Raps a song, must be entered with a name", inline=False)
        embedvariable.add_field(name="offline", value="Makes rge bot go offline", inline=False)
        embedvariable.add_field(name="online", value="Makes the bot come online", inline=False)
        embedvariable.add_field(name="pfp", value="Sends the authors profile picture", inline=False)
        embedvariable.add_field(name="ping", value="Tells you your ping", inline=False)  
        embedvariable.add_field(name="qna", value="Asks you a question", inline=False)
        embedvariable.add_field(name="reactme", value="A reaction timing game", inline=False)
        embedvariable.add_field(name="rh", value="Send 'raised' ", inline=False)
        embedvariable.add_field(name="rps", value="Lets you play rock, paper, scissors", inline=False)
        embedvariable.add_field(name="sad", value="Comforts you", inline=False)

        embedvariable.set_footer(text="Page 2, use .sa help *page number* to select another page")
        await ctx.send(embed=embedvariable) 

def setup(bot):
    bot.add_cog(Help(bot))
