import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('login')
    print(client.user.id)
    print('------------------------')


token = os.environ["TOKEN"]
client.run(token)
