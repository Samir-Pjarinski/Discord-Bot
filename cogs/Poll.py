import discord
from discord import channel
from discord.ext import commands
from discord import Color
from discord.ext.commands import MemberConverter, MessageConverter
from discord.reaction import Reaction
from discord import User
from datetime import datetime
import asyncio

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Poll(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def poll(self, ctx, question, option1, option2, option3 = None, option4 = None): 

    #     options = {1: option1, 2: option2, 3: option3, 4: option4}

    #     if option3 == None and option4 == None:
    #         if option1 == "yes" and option2 == "no":
    #             reactions = ["✅", "❌"]
    #         else:
    #             reactions = ["1⃣", "2⃣"]
    #     elif option3 != None and option4 == None:
    #         reactions = ["1⃣", "2⃣", "3️⃣"]
    #     else:
    #         reactions = ["1⃣", "2⃣", "3️⃣", "4️⃣"]            

    #     description = []
    #     for i in range(0, len(reactions)):
    #         description += f" {reactions[i]} {options[i + 1]}  "
        
    #     embed = discord.Embed(title=question, description="".join(description), colour = 0, timestamp = datetime.utcnow())
    #     react_Message = await ctx.send(embed = embed)
        
    #     for i in range(0, len(reactions)):
    #         await react_Message.add_reaction(reactions[i])
        
    #     embed.set_footer(text=f"Poll ID: {react_Message.id}")
    #     await react_Message.edit(embed=embed)

    @commands.command()
    async def poll(self, ctx, question, *options): 

        if len(options) > 10:
            await ctx.send("10 options MAX")
        else:
            embed = discord.Embed(title = "Poll", description = question)
            fields = [("Options:", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False), 
                    ("Instructions", "React to add a vote.",  False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)

            react_Message = await ctx.send(embed = embed)

            for i in range(len(options)):
                await react_Message.add_reaction(numbers[i])
            
            # await react_Message.add_reaction("❓")

            embed.set_footer(text=f"Poll ID: {react_Message.id}")
            await react_Message.edit(embed=embed)

            def checkvalid(reaction : Reaction, user : User):
                return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id

            # member = ctx.message.author
            # channel = await member.create_dm()
            
            # while True:
            #     reaction, user = await self.bot.wait_for(event = "reaction_add", check = checkvalid)
            #     if reaction.emoji == "❓":
            #         await channel.send("This will do something later")
            #         break

    @commands.command()
    async def tally(self, ctx, id: discord.Message):
        
        options = {1: "Option 1", 2: "Option 2", 3: "Option 3", 4: "Option 4", 5: "Option 5", 6: "Option 6", 7: "Option 7", 8: "Option 8", 9: "Option 9", 10: "Option 10"}

        poll_message = id
        embed = poll_message.embeds[0]
        optcount = []
        users = ["TTA Test Bot"]

        for i in range(0, (len(poll_message.reactions) - 1)):
            botCount = 0

            user = await poll_message.reactions[i].users().flatten()
            for j in range(0, len(user)):
                
                for k in range(0, len(users)):
                    if user[j].name == users[k]:
                        botCount += 1
                
                if user[j].name != users[k]:
                    users.append(user[j].name)

            optcount.append(poll_message.reactions[i].count - botCount)
            botCount = 0

        output = f"Results of the poll for '{embed.title}':"
        
        winnerValue = -1
        winner = "Tie"
        tieCount = []
        for i in range(0, len(optcount)):
            
            if optcount[i] > winnerValue:
                tie = False
                winnerValue = optcount[i]
            elif optcount[i] == winnerValue:
                tie = True
                tieCount.append(i + 1)

        for i in range(0, (len(poll_message.reactions) - 1)):
            
            output += f"\nOption {i + 1}: {optcount[i]}"
            if not tie:
                if winnerValue == optcount[i]:
                    winner = options[i + 1]
            else:
                winner = f"Tie between options"
                for i in range(len(tieCount)):
                    if i == len(tieCount) - 1:
                        winner += f" {tieCount[i]}"
                    else:
                        winner += f" {tieCount[i]} and"
        
        output += f"\nWinner: {winner}"
        await ctx.send(output)

    @poll.error
    async def poll_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to give a question and at least one option with the poll command.")

    @tally.error
    async def tally_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to give a message id with the tally command.")

def setup(bot):
    bot.add_cog(Poll(bot))
