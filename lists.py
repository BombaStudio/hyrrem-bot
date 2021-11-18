import urllib.request

kufur_server = urllib.request.urlopen("https://raw.githubusercontent.com/ooguz/turkce-kufur-karaliste/master/karaliste.json")


kufurler = eval(kufur_server.read())


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

muzikler = [
    #no1
    "https://www.youtube.com/watch?v=1e87wv-nsyU",
    "https://www.youtube.com/watch?v=LU5FrAKJmYQ",
    "https://www.youtube.com/watch?v=V5MxQSFsxS4",
    "https://www.youtube.com/watch?v=BzjeUUfG3qw",
    "https://www.youtube.com/watch?v=NRMTI-qBFQM",
    #sansar salvo
    "https://www.youtube.com/watch?v=NhIGWG-wMDo",
    "https://www.youtube.com/watch?v=pVGzzvW3e8E",
    "https://www.youtube.com/watch?v=PwllW-SHYb4",
    "https://www.youtube.com/watch?v=7YukiDbR0sI",
    "https://www.youtube.com/watch?v=T_VB_HjibHA",
    #şehinşah
    "https://www.youtube.com/watch?v=5FvqjKbuulU",
    "https://www.youtube.com/watch?v=dC16wEIurww",
    "https://www.youtube.com/watch?v=DBL90ZsxQrY",
    "https://www.youtube.com/watch?v=ZaIuvrPSZI8",
    #hidra
    "https://www.youtube.com/watch?v=4jM2iTUfAns",
    "https://www.youtube.com/watch?v=IvzQamZ1NbE",
    "https://www.youtube.com/watch?v=a2ffJKL8WMU",
    "https://www.youtube.com/watch?v=lBO0-pf1Szk",
    "https://www.youtube.com/watch?v=huXDCyfXpvU",
    "https://www.youtube.com/watch?v=2HqwVCw27_Y",
    "https://www.youtube.com/watch?v=GeRpme9lHDg",
    "https://www.youtube.com/watch?v=FPr8aEhAghg",
    "https://www.youtube.com/watch?v=xGjsDo_VrTo",
    "https://www.youtube.com/watch?v=AVhumUW4X-8",
    "https://www.youtube.com/watch?v=l7IiXlbyi1A",
    "https://www.youtube.com/watch?v=QBGQa6zGSx8",
    #saian
    "https://www.youtube.com/watch?v=_YniC9g1T5s",
    "https://www.youtube.com/watch?v=wu_gAo_-Wfc",
    "https://www.youtube.com/watch?v=zhvnwTmcQMI",
    "https://www.youtube.com/watch?v=J-KUtPPlUqs",
    "https://www.youtube.com/watch?v=xMXO-ynIJJ4",
    "https://www.youtube.com/watch?v=3XXnOfuD388",
    #joker
    "https://www.youtube.com/watch?v=b6negnCyT7c",
    "https://www.youtube.com/watch?v=jxrCeGssyEo",
    "https://www.youtube.com/watch?v=_Fj1hn1_hC4",
    "https://www.youtube.com/watch?v=VxXcvdB29x4",
    "https://www.youtube.com/watch?v=3CqW_i4Mp6I",
    "https://www.youtube.com/watch?v=zW22iRETmqE",
    #zeynep bastık
    "https://www.youtube.com/watch?v=tcUUEJfp-Uk",
    "https://www.youtube.com/watch?v=WFdLcr7oxEg",
    "https://www.youtube.com/watch?v=3sN-DKevBuE",
    "https://www.youtube.com/watch?v=NRNwBWeii50",
    #tepki
    "https://www.youtube.com/watch?v=xNG-oXPZNGE",
    "https://www.youtube.com/watch?v=92K8_6LPl5k",
    #model
    "https://www.youtube.com/watch?v=dQ7LJ9nYKU8",
    "https://www.youtube.com/watch?v=SpJ96ZRj9dk"
]