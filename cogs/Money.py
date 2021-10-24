import discord, json
from discord.ext import commands
from discord.reaction import Reaction
from discord import User, Message
import random, asyncio

class Money(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def get_money(self, message):
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)

        return money[str(message.message.author.id)]

    @commands.command(aliases = ["loadacc", "resetmoney", "resetacc"])
    async def load_money(self, ctx):
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)
        
        money[str(ctx.message.author.id)] = 0

        with open("cogs/Money.json", "w") as f:
            json.dump(money, f, indent = 4)
            
    @commands.command(aliases = ["removeacc"])
    async def delete_account(self, ctx):
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)
        
        money.pop(str(ctx.message.author.id))

        with open("cogs/Money.json", "w") as f:
            json.dump(money, f, indent = 4)

    @commands.command(aliases = ["work"])
    async def add_money(self, ctx, amt = 5):
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)
        
        money[str(ctx.message.author.id)] += amt

        with open("cogs/Money.json", "w") as f:
            json.dump(money, f, indent = 4)     

        await ctx.send(f"You have succesfully earned: ${amt}")   

    @commands.command()
    async def rpsbet(self, ctx, bet : int = 100):
        
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)

        if bet > money[str(ctx.message.author.id)]:
            await ctx.send("You do not enough money")
        else:

            money[str(ctx.message.author.id)] -= bet

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
                    result = "Tie"
                if bot_choice == "🧻":
                    win = "Covered"
                    result = "Loss"
                if bot_choice == "✂️":
                    win = "Scissors Break"
                    result = "Win"
                await place.remove_reaction("<:the_rock:888669317900677150>", self.bot.user)
                await place.remove_reaction("🧻", self.bot.user)
                await place.remove_reaction("✂️", self.bot.user)  

            if reaction.emoji == "🧻":
                if bot_choice == "🧻":
                    win = "Wow A Whole Lotta Nothing"
                    result = "Tie"
                if bot_choice == "✂️":
                    win = "Snip Snip Snip"
                    result = "Loss"
                if bot_choice == "<:the_rock:888669317900677150>":
                    win = "Um You Covered Me"
                    result = "Win"
                await place.remove_reaction("<:the_rock:888669317900677150>", self.bot.user)
                await place.remove_reaction("🧻", self.bot.user)
                await place.remove_reaction("✂️", self.bot.user)  

            if reaction.emoji == "✂️":
                if bot_choice == "✂️":
                    win = "Clang Clang"
                    result = "Tie"
                if bot_choice == "<:the_rock:888669317900677150>":
                    win = "Scissors Breaks"
                    result = "Loss"
                if bot_choice == "🧻":
                    win = "Cut Cut Cut"
                    result = "Win"
                await place.remove_reaction("<:the_rock:888669317900677150>", self.bot.user)
                await place.remove_reaction("🧻", self.bot.user)         
                await place.remove_reaction("✂️", self.bot.user)    

            embedvariable.add_field(name="My choice was:", value=bot_choice, inline=True)
            embedvariable.add_field(name="Result:", value=win, inline=True)
            embedvariable.set_image(url=img)
            await place.edit(embed=embedvariable)

            if result == "Win":
                bet *= 2
                await ctx.send(f"You have succesfully earned: ${bet}")   
            elif result == "Tie":
                bet = bet
                await ctx.send(f"You gain nothing you lose nothing")   
            else:
                bet = 0
                await ctx.send(f"You lost everything")   
            
            money[str(ctx.message.author.id)] += bet

            with open("cogs/Money.json", "w") as f:
                json.dump(money, f, indent = 4)   

    @commands.command(aliases=["headsortails", "coinflip"])
    async def flip(self, ctx, call, bet : int = 100):
        
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)
        
        if bet > money[str(ctx.message.author.id)]:
            await ctx.send("You do not enough money")
        else:

            money[str(ctx.message.author.id)] -= bet

            coin = random.choice(["heads", "tails"])

            if coin == call:
                bet *= 2
                await ctx.send(f"{call} you win ${bet}")
            else:
                bet = 0
                await ctx.send(f"{call} you lose you bet")

            money[str(ctx.message.author.id)] += bet

            with open("cogs/Money.json", "w") as f:
                json.dump(money, f, indent = 4)   

    @commands.command(aliases=["wordscramble", "scramble"])
    async def word_scramble(self, ctx, bet : int = 100):
        
        with open("cogs/Money.json", "r") as f:
            money = json.load(f)
        
        words = ["ROLLER COASTER", "PARADE", "SWIMMING POOL", "BIKE RIDES", "VACATION", "PICNIC", "CAMPING", "BEACH", "THEME PARK", "MOVIES", "FIREWORKS", "MOUNTAINS" ]
        scrambles = ["LROLRE CSOAETR", "ERAPDA", "MSIMNPWG OPOL", "KBIE IDRSE", "NVOAICTA", "ICCPNI", "ACMINGP", "EBCAH", "MHETE RPAK", "EOVMIS", "RFIESORWK", "OUNAMINTS" ]
        choice = random.randint(0, len(words) - 1)

        if bet > money[str(ctx.message.author.id)]:
            await ctx.send("You do not enough money")
        else:
            
            def checkvalid(message: Message, user : User): 
                return (user.author == ctx.author and user.channel == ctx.channel) and message == ctx.message  

            money[str(ctx.message.author.id)] -= bet

            await ctx.send(f"What is the correct word? {scrambles[choice]}")
            await ctx.send("Answer: ")

            try:
                message, user = await self.bot.wait_for("message", timeout = 120.0, check = checkvalid)
            except asyncio.TimeoutError:
                await ctx.send("Type faster next time. Bet has been refunded")
            else:
                print(message)
                if message.message == words[choice]:
                    bet *= 2
                    await ctx.send(f"Right, you won: ${bet}")
                else:
                    bet *= 0
                    await ctx.send("You lost your bet")


            money[str(ctx.message.author.id)] += bet

            with open("cogs/Money.json", "w") as f:
                json.dump(money, f, indent = 4)  

    @commands.command()
    async def savings(self, ctx):
        
        money = self.get_money(ctx)

        await ctx.send(f"You have: ${money}")

def setup(bot):
    bot.add_cog(Money(bot))