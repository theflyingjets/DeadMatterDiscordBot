import discord
import re
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def players(ctx):
    theFile = open('deadmatter.log','r')
    FILE = theFile.readlines()
    theFile.close()
    printList = []
    for line in FILE:
        if ('left!' in line) or ('connected!' in line):
            printList.append(line)
            players = re.search(r'\((.*?)\)',printList[-1]).group(1)

    await ctx.send(f'The amount of players in the server are: {players}')

client.run('<API Key or token goes here!>')
