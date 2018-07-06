import discord
import asyncio
import random
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime

client = discord.Client()
bot = ChatBot('Ana')
now = datetime.now()

conv = ['#oi', 'oi', '#Qual é o seu nome?', 'Meu nome é Ana']

d20 = 0
d220 = 0
d100 = 0
d10 = 0
p1nr = 0

id1 = "342077525184479232" #Lucas_Gabriel
id2 = "404123866353631232" #Melhor_mestre
id3 = "185067692766658560" #Chanceler
id4 = "335202598766379010" #Dr.SCP


@client.event
async def on_ready():
    print("----@@@--------@@@----")
    print("Estou pronta")
    print("Nome:", client.user.name)
    print("Id:", client.user.id)
    print("----@@@--------@@@----")
    print(now.year,'/',now.month,'/',now.day)
    print(now.hour,':',now.minute,':',now.second)

@client.event
async def on_member_join(member):
    print("Alguém chamado" + member.name + "Entrou no servidor")
    await client.send_message(member, "Bem vindo a Fámilia TJ")
    print("Foi mandado uma mensagem para" + member.name)

@client.event
async def on_message(message):


    print(message.author, message.content ,message.channel)

    if now.year == (2018) and now.month == (7) and now.day == (4):
        message.channel== 'chatdosdrodi'
        await client.send_message(message.channel, "oi?")


    if message.content.startswith("-"):
        if message.author.id == id4 or message.author.id == id3 or message.author.id == id2 or message.author.id == id1:

            response = bot.get_response(message.content)
            if float(response.confidence) > 0.5:
                await client.send_message(message.channel, response)
            else:
                await client.send_message(message.channel, "Não confio em você")

    if message.content.startswith("1d20"):
        if message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            d20 = random.randrange(1,20)
            await client.send_message(message.channel, message.author.name)
            await client.send_message(message.channel, "Seu resultado")
            await client.send_message(message.channel, d20)
        else:
            await client.send_message(message.channel, "Você não tem permissão")

    if message.content.startswith("1d20"):
        if message.author.id == id1:
            d220 = random.randrange(1,5)
            await client.send_message(message.channel, message.author.name)
            await client.send_message(message.channel, "Seu resultado")
            await client.send_message(message.channel, d220)
        else:
            await client.send_message(message.channel, "Você não tem permissão")

    if message.content.startswith("1d.100"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            d100 = random.randrange(1,100)
            await client.send_message(message.channel, message.author.name)
            await client.send_message(message.channel, "Seu resultado")
            await client.send_message(message.channel, d100)
        else:
            await client.send_message(message.channel, "Você não tem permissão")

    if message.content.startswith("1d10"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            d10 = random.randrange(1, 10)
            await client.send_message(message.channel, message.author.name)
            await client.send_message(message.channel, "Seu resultado")
            await client.send_message(message.channel, d10)
        else:
            await client.send_message(message.channel, "Você não tem permissão")

    if message.content.startswith("+"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            p1nr = random.randrange(1, 33)

            if p1nr < 21 :
                await client.send_message(message.channel, message.author.name)
                await client.send_message(message.channel, "Tente denovo, se tiver coragem")
                await client.send_message(message.channel, p1nr)

            if p1nr > 21 :
                await client.send_message(message.channel, message.author.name)
                await client.send_message(message.channel, "Passou um pouquinho, só um pouquinho")
                await client.send_message(message.channel, p1nr)

            if p1nr == 21 :
                await client.send_message(message.channel, message.author.name)
                await client.send_message(message.channel, "Parabéns, estou muito surpresa")
                await client.send_message(message.channel, p1nr)

        else:
            await client.send_message(message.channel, "Você não tem permissão")

    if message.content.startswith("Atrib:Arqueiro Amarelo"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            emb = (discord.Embed(description = "Arqueiro Amarelo", colour= 0xffff00))
            emb.set_thumbnail(url= "https://cdn.discordapp.com/attachments/417132517582307329/464134410883694594/Joao_Marcos-Terra_44.png")
            emb.set_footer(text="Pericia: Contrabando")
            emb.add_field(name='Atributo', value = 'força:', inline=True)
            emb.add_field(name='Valor', value='10 +10', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Agilidade:', inline=True)
            emb.add_field(name='Valor', value='13', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Vitalidade:', inline=True)
            emb.add_field(name='Valor', value='12', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Defesa:', inline=True)
            emb.add_field(name='Valor', value='5 +20', inline=True)
            emb.add_field(name='Habilidade', value='Benção da Águia', inline=False)
        await client.send_message(message.channel, embed = emb);

    if message.content.startswith("Atrib:Ceifador Roxo"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            emb = (discord.Embed(description = "Ceifador Roxo", colour= 0x800080))
            emb.set_thumbnail(url= "https://media.discordapp.net/attachments/417132517582307329/464134067567460352/Lucas.png?width=568&height=568")
            emb.set_footer(text="Pericia: Música")
            emb.add_field(name='Atributo', value = 'força:', inline=True)
            emb.add_field(name='Valor', value='10 +3', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Agilidade:', inline=True)
            emb.add_field(name='Valor', value='8', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Vitalidade:', inline=True)
            emb.add_field(name='Valor', value='11', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Defesa:', inline=True)
            emb.add_field(name='Valor', value='8', inline=True)
            emb.add_field(name='Habilidade', value='Escravo da Morte', inline=False)
        await client.send_message(message.channel, embed = emb);

    if message.content.startswith("Atrib:Ninja Azul"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            emb = (discord.Embed(description = "Ninja Azul ", colour= 0x66ffff))
            emb.set_thumbnail(url= "https://cdn.discordapp.com/attachments/417132517582307329/464143434878418954/Esdras.png")
            emb.set_footer(text="Pericia: Navegação")
            emb.add_field(name='Atributo', value = 'força:', inline=True)
            emb.add_field(name='Valor', value='5 +5', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Agilidade:', inline=True)
            emb.add_field(name='Valor', value='6 +15', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Vitalidade:', inline=True)
            emb.add_field(name='Valor', value='14', inline=True)
            emb.add_field(name='------', value='------', inline=False)
            emb.add_field(name='Atributo', value='Defesa:', inline=True)
            emb.add_field(name='Valor', value='5 +10', inline=True)
            emb.add_field(name='Habilidade', value='Benção da nevasca', inline=False)
        await client.send_message(message.channel, embed = emb);

    if message.content.startswith("Equip:Arqueiro Amarelo"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            emb = (discord.Embed(description = "Arqueiro Amarelo", colour= 0xffff00))
            emb.set_thumbnail(url= "https://cdn.discordapp.com/attachments/417132517582307329/464134410883694594/Joao_Marcos-Terra_44.png")
            emb.set_footer(text="Arma padrão: Besta(enchant:Burn)")
            emb.add_field(name='Equipamentos', value = '50 flechas(equipadas), besta(equipado), anel de golem(equipado), Rel.Mercantes(equipada), Rel.Espinhos(quipada), isqueiro,trapos, M9(carregada),revolver(carregada) ', inline=True)
        await client.send_message(message.channel, embed = emb);

    if message.content.startswith("Equip:Ceifador Roxo"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            emb = (discord.Embed(description = "Ceifador Roxo", colour= 0x800080))
            emb.set_thumbnail(url= "https://media.discordapp.net/attachments/417132517582307329/464134067567460352/Lucas.png?width=568&height=568")
            emb.set_footer(text="Arma padrão: Foice")
            emb.add_field(name='Equipamentos', value = 'Foice(equipada), mascara branca, Rel.Somra verde, Rel.ceus, sobretudo(equipado), 1 diamante, cabo, alabarda, M-110(carregada e equipada)', inline=True)
        await client.send_message(message.channel, embed = emb);

    if message.content.startswith("Equip:Ninja Azul"):
        if message.author.id == id1 or message.author.id == id2 or message.author.id == id3 or message.author.id == id4:
            emb = (discord.Embed(description = "Ninja Azul", colour= 0x66ffff))
            emb.set_thumbnail(url= "https://cdn.discordapp.com/attachments/417132517582307329/464143434878418954/Esdras.png ")
            emb.set_footer(text="Arma padrão: Tekko-Kagi")
            emb.add_field(name='Equipamentos', value = 'Tekko-Kagi(equipada), Anel da vida real(equipada), sobretudo longo(equipada), armadura comum(equipada), Rel.Covarde(equipada), Rel.Trapaça(equipada), 2 rubis, escudo, Cruz velha, pedaço de metal muito bem arquitetado, Tar-21(carregada e equipada)', inline=True)
        await client.send_message(message.channel, embed = emb);



client.run(process.env.BOT_TOKEN);
