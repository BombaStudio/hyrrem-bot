import discord
import os

load_dotenv()
TOKEN = os.getenv('OTEwNDcwMjkyOTE5NDUxNjQ4.YZTTiQ.27Rsu-uaPL22Ww8NOlYVOMP9HCM')

client = discord.Client()

kufurler = [
    "amk","oç","aq"
]

@client.event
async def on_ready():
    print('{0.user} olarak Hünkarımızın yanına geldik'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*Merhaba'):
        await message.channel.send('Merhaba')
        
    for i in range(0,len(kufurler)):
        if message.content.startswith(kufurler[i]):
            await message.channel.send('Bu ne hadsizlik !!!')
            
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)
