import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('login')
    print(client.user.id)
    print('------------------------')


client.run("OTUwMjM1ODM5NjU5NjUxMTg1.YiV-Fg.861iJXkK4WPPLgG59drfjFjoeCU")
