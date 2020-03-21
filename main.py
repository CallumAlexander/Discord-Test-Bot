# Property of Callum Alexander
# Bot 0.1 for Discord

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="Hey TestBot ")


@client.event
async def on_ready():
    print("Bot is up and running")


@client.event
async def on_message(ctx, message):
    joinResponses = ["Hahahaha I'm back ONLINE",
                     "Greetings",
                     "I'm back because I don't hate fun"]
    await ctx.send(f"{random.choice(joinResponses)}")


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def ping(ctx):
    await ctx.send(f"{client.latency * 1000}ms")


@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = [" It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.", "As I see it, yes.",
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
    await ctx.send(f"{random.choice(responses)}")


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


# todo - token needed
client.run("")
