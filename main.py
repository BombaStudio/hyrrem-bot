import discord
import os
from dotenv import load_dotenv


load_dotenv()

client = discord.Client()

kufurler = [
    "amk","oç","aq"
]
animeler = [
    #seferde
    "https://cdn.myanimelist.net/s/common/uploaded_files/1449740311-6a7b98fbf1ec9f4edcb3101834263ac2.jpeg",
    #müzik dinliyor
    "https://cdn.discordapp.com/attachments/891598729096876063/910475982408912946/hot-Maki-Nishikino-anime-girl-smile.png",
    #sinirli
    "https://cdn.discordapp.com/attachments/891598729096876063/910476117859762197/1449739970-dc7f29fde95a3ec6ca48108a42efc359.png",
    #güler yüzlü
    "https://cdn.discordapp.com/attachments/891598729096876063/910476303055069235/adorable-anime-freckles-ginger-Favim.png",
    #tatlı bakış
    "https://cdn.discordapp.com/attachments/891598729096876063/910476392586698752/c479512a08ab6582dd16032b94081257.png",
    #sonbahar
    "https://cdn.discordapp.com/attachments/891598729096876063/910476437608361995/original.png",
    #deathnote
    "https://cdn.discordapp.com/attachments/891598729096876063/910476601022640158/f3133c20e2d84f5e894d46b7ad1f6671.png",
    #sefere hazırlık
    "https://cdn.discordapp.com/attachments/891598729096876063/910476700062711808/d6c2735a69253d56c637203a109b4d79.png",
    #sefer bitti
    "https://cdn.discordapp.com/attachments/891598729096876063/910476952681447494/d4f771bde4bc78d9ec8bbc12b66a8e50.png",
    #ağlamak
    "https://cdn.discordapp.com/attachments/891598729096876063/910477068658163753/1479932380-a9153da45d1a5c0ded4210c22b264e22.png",
    #gezmek
    "https://cdn.discordapp.com/attachments/891598729096876063/910478431102332938/8a5dc8b37d211d1bb3065d1c369b08a6.png"
]

@client.event
async def on_ready():
    print('{0.user} olarak Hünkarımızın yanına geldik'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('*author'):
        await message.channel.send(str(message.author))
    if message.content.startswith('*authorid'):
        await message.channel.send(str(message.author.id))
        
    if message.content.startswith('*Merhaba'):
        await message.channel.send('Merhaba')
        
    if "sefere gidiyorum" in message.content:
        e = discord.Embed()
        #e.set_image(url=animeler[8])
        await message.channel.send(animeler[8])
        await message.channel.send('Beni de bekle Hünkarım seni yanlız bırakamam')

    for i in range(0,len(kufurler)):
        if kufurler[i] in message.content:
            await message.channel.send('Bu ne hadsizlik !!!')
        
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Osmanlı Cumhuriyeti ne hoşgeldin tatlım!'
    )

client.run('OTEwNDcwMjkyOTE5NDUxNjQ4.YZTTiQ.dKrL5BfVQITanWlLICmJ6oorruY')
