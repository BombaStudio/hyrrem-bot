import discord
import os

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

client.run(os.getenv('OTEwNDcwMjkyOTE5NDUxNjQ4.YZTTiQ.27Rsu-uaPL22Ww8NOlYVOMP9HCM'))
