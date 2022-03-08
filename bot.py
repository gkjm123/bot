import configparser
import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

option = configparser.ConfigParser()
option.read("setting.ini", encoding="utf-8")
token = option["setting"]["token"]
number = option["setting"]["number"]
invite_role = option["setting"]["invite_role"]
list_role = option["setting"]["list_role"]
channel = option["setting"]["channel"]


@client.event
async def on_ready():
    print('login')
    print(client.user.id)
    print('------------------------')


@client.event
async def on_message(message):
    if message.content != "" and message.channel.id == int(channel):
        with open('chat.txt', 'a', encoding='utf-8') as f:
            f.write(message.author.name+"#"+message.author.discriminator+" : "+message.content+"\n\n")

    if message.content.startswith("/초대"):
        r = message.guild.get_role(int(invite_role))
        mem = await message.guild.fetch_member(message.author.id)
        list = await message.guild.invites()
        for i in list:
            if i.inviter.id == message.author.id:
                await message.channel.send(message.author.name + "님은 지금까지 " + str(i.uses) + "명을 초대했습니다.")
                if i.uses >= int(number) and r not in mem.roles:
                    await mem.add_roles(r)
                    await message.channel.send(str(number) + "명을 초대해 " + r.name + " 역할이 되셨습니다.")
                return
        await message.channel.send("아직 생성한 초대코드가 없습니다. 초대코드를 생성후 멤버를 불러보세요.")

    if message.content.startswith("/인증"):
        r = message.guild.get_role(int(list_role))
        with open('member.txt', 'r', encoding='utf-8') as file:
            cli = file.readlines()
            if message.author.name in cli:
                mem = await message.guild.fetch_member(message.author.id)
                if r not in mem.roles:
                    await mem.add_roles(r)
                    await message.channel.send("인증되었습니다. 역할이 부여됩니다.")
                else:
                    await message.channel.send("이미 인증되어 역할이 부여되었습니다.")


client.run(token)
