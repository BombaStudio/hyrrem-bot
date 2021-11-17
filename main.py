import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} olarak Hünkarımızın yanına geldik'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('*Merhaba'):
        await message.channel.send('Merhaba')

client.run(os.getenv('OTEwNDcwMjkyOTE5NDUxNjQ4.YZTTiQ.27Rsu-uaPL22Ww8NOlYVOMP9HCM'))
