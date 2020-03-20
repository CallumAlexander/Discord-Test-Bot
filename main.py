# Property of Callum Alexander
# Bot 0.1 for Discord

from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")


client.run("NjkwNTQ0NTU2Mjk0NDA2MTg0.XnUETQ.HEV7ImbGH0mh8flHLWxj5hhQ5dw")
