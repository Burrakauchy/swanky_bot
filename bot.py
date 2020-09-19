import discord
from discord.ext import commands
import json


with open("data/config.json") as cp:
    client = commands.Bot(command_prefix=json.load(cp)["prefix"])

extensions = ['cogs.questions']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
    
with open("data/token.json") as fp:
    client.run(json.load(fp)['token'])