import discord
from discord.ext import commands
from discord.reaction import Reaction
from discord import User
import random

class Games(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qna(self, ctx):
        
        def checkvalid(reaction : Reaction, user : User):
            return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id

        place = await ctx.send("Are you happy")
        await place.add_reaction("🇾")
        await place.add_reaction("🇳")

        reaction, user = await self.bot.wait_for(event = "reaction_add", check = checkvalid)

        if reaction.emoji == "🇾":
            await ctx.send("That's good")
        elif reaction.emoji == "🇳":
            await ctx.send("Don't worry it'll all be okay soon")
        
        await place.remove_reaction("🇳", self.bot.user)

    @commands.group(invoke_without_commnads=True)
    async def game(self, ctx):
        
        global check

        await ctx.send("Pick a number between 1 and 10")
        await ctx.send("Use the command .sa game guess *number* ")

        check = True
    
    
    @game.command(name="guess")
    async def game_subcommand(self, ctx, user_number: int):
        
        global check
        bot_number = random.randint(1, 10)

        if check == True:
            if user_number > 10:
                await ctx.send("That number is higher than 10")
            elif user_number == bot_number:
                await ctx.send("Correct")
                check = False
            elif user_number < 1:
                await ctx.send("That number is lower than 1")
            else:
                await ctx.send("Thats the wrong number")
                await ctx.send("The correct number was " + str(bot_number))
                check = False

    @commands.command(aliases=["8Ball", "8ball", "EightBall", "Eightball"])
    async def _8ball(self, ctx, *, question):
        
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]

        await ctx.send(f"Question: {question} \n Answer: {random.choice(responses)}")

    @commands.command()
    async def rps(self, ctx):
        
        def checkvalid(reaction : Reaction, user : User):
            return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id

        bot_r = random.randint(1,3)

        if bot_r == 1:
            bot_choice = "<:the_rock:888669317900677150>"
            img = "https://images.news18.com/ibnlive/uploads/2020/10/1602213968_sports-2020-10-09t085537.964.png"
        if bot_r == 2:
            bot_choice = "🧻"
            img = "https://5.imimg.com/data5/UC/EF/MY-46388924/tissue-roll-500x500.jpg"
        if bot_r == 3:
            bot_choice = "✂️"
            img = "https://image.shutterstock.com/image-vector/open-scissor-white-background-icon-260nw-1414191452.jpg"
        
        embedvariable = discord.Embed(title="Game", description="Choose Rock, Paper, or Scissors", colour=0xFFFF00)
        embedvariable.set_thumbnail(url="https://www.esquireme.com/public/styles/full_img/public/images/2017/05/29/rock_paper_scissors__2x.png?itok=7H3NxSxN")
        place = await ctx.send(embed=embedvariable)
        await place.add_reaction("<:the_rock:888669317900677150>")
        await place.add_reaction("🧻") 
        await place.add_reaction("✂️")

        reaction, user = await self.bot.wait_for(event = "reaction_add", check = checkvalid)
        if str(reaction.emoji) == "<:the_rock:888669317900677150>":
            if bot_choice == "<:the_rock:888669317900677150>":
                win = "Trying to make fire are we"
            if bot_choice == "🧻":
                win = "Covered"
            if bot_choice == "✂️":
                win = "Scissors Break"
            await place.remove_reaction("<:the_rock:888669317900677150>", self.bot.user)
            await place.remove_reaction("🧻", self.bot.user)
            await place.remove_reaction("✂️", self.bot.user)  

        if reaction.emoji == "🧻":
            if bot_choice == "🧻":
                win = "Wow A Whole Lotta Nothing"
            if bot_choice == "✂️":
                win = "Snip Snip Snip"
            if bot_choice == "<:the_rock:888669317900677150>":
                win = "Um You Covered Me"
            await place.remove_reaction("<:the_rock:888669317900677150>", self.bot.user)
            await place.remove_reaction("🧻", self.bot.user)
            await place.remove_reaction("✂️", self.bot.user)  

        if reaction.emoji == "✂️":
            if bot_choice == "✂️":
                win = "Clang Clang"
            if bot_choice == "<:the_rock:888669317900677150>":
                win = "Scissors Breaks"
            if bot_choice == "🧻":
                win = "Cut Cut Cut"
            await place.remove_reaction("<:the_rock:888669317900677150>", self.bot.user)
            await place.remove_reaction("🧻", self.bot.user)         
            await place.remove_reaction("✂️", self.bot.user)    

        embedvariable.add_field(name="My choice was:", value=bot_choice, inline=True)
        embedvariable.add_field(name="Result:", value=win, inline=True)
        embedvariable.set_image(url=img)
        await place.edit(embed=embedvariable)

    @commands.command()
    async def memes(self, ctx):
        
        memes = [
            "https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043", 
            "https://i.pinimg.com/originals/e3/2c/e7/e32ce76b21b7953e0badb1eceffff524.jpg", 
            "https://media-assets-03.thedrum.com/cache/images/thedrum-prod/s3-news-tmp-349138-meme7--default--1050.png", 
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_HyGoBdwM_CYB2F20uM4sEPI0AH-st6eAEA&usqp=CAU", 
            "https://tenor.com/view/relatable-cat-funny-animals-wifi-gif-14384030"
            ]

        await ctx.send(random.choice(memes))

    @commands.command()
    async def pog(self, ctx, pog):
        
        t = await ctx.send("reacting...")
        if pog == "troll":
            await t.add_reaction("<:trollololol:842127808162955274>")
        if pog == "pog":
            await t.add_reaction("<:pog:730280874204987442>")

def setup(bot):
    bot.add_cog(Games(bot))
