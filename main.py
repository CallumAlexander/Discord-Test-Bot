# Property of Callum Alexander
# Bot 0.1 for Discord

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def ping(ctx):
    await ctx.send(f"{client.latency * 1000}ms")


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = [" It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.", ]
    await ctx.send(f"Question : {question} , Answer : {random.choice(responses)}")


client.run("NjkwNTQ0NTU2Mjk0NDA2MTg0.XnULdA.X7k5Wp3mKkFxm4T4UR070AfASqc")
