import discord
import os
from dotenv import load_dotenv
from lists import *
import json
import random


with open(os.path.dirname(__file__) + "config.json", "r+") as f:
    data = json.load(f)
    BotToken = data["BotToken"]
    AdminID = data["AdminID"]


load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} olarak Hünkarımızın yanına geldik'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('*author'):
        await message.channel.send(str(message.author))
    if message.content.startswith('*tag'):
        await message.channel.send(str(message.author.role))
    if message.content.startswith('*authorid'):
        await message.channel.send(str(message.author.id))
        
    if message.content.startswith('*Merhaba'):
        await message.channel.send('Merhaba')
    if message.content.upper() == "benim için müzik önerir misin".upper():
        await message.channel.send(animeler[1])
        await message.channel.send("\n\n Bu müziğin sana iyi geleceğinden eminim canım.\n\n" + muzikler[random.randint(0,len(muzikler))])
        
    if message.content.startswith('*stop'):
        await message.voice_client.disconnect()
        
    if "sefere gidiyorum" in message.content or "sefere gidiyoruz" in message.content or "sefere çıkıyorum" in message.content or "sefere çıkıyoruz" in message.content:
        #e = discord.Embed()
        #e.set_image(url=animeler[8])
        if str(message.author.id) == AdminID:
            await message.channel.send(animeler[8])
            await message.channel.send('Beni de bekle Hünkarım seni yanlız bırakamam')
        else:
            await message.channel.send(animeler[6])
            await message.channel.send('Bu savaşı da zafelerle getirin yiğitlerim')
    if message.content.upper() == "SENI SEVIYORUM HÜRREM":
        if str(message.author.id) == AdminID:
            await message.channel.send(animeler[3])
            await message.channel.send('Bende sizi Hünkarım')
        else:
            await message.channel.send(animeler[5])
            await message.channel.send('Tombul oldum diye sevme beni küstüm')

    for i in range(0,len(kufurler)):
        if kufurler[i].upper() in message.content.upper():
            if str(message.author.id) == AdminID:
                await message.channel.send(animeler[9])
                await message.channel.send('Kalbimi kırdınız Hünkarım')
            else:
                await message.channel.send(animeler[2])
                await message.channel.send('Mahidevran benimle doğru konuş zira karşında sultan süleymanın nikahlı karısı var sen bir köle cariyesin ben ise gerçek bir sultanım')
        
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Osmanlı Cumhuriyeti ne hoşgeldin tatlım!'
    )

client.run(BotToken)
