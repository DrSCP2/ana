import discord
import asyncio
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime

client = discord.Client()
bot = ChatBot('Ana')

conv = ['-oi', 'oi', '-Qual é o seu nome?', 'Meu nome é Ana']

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
    await client.send_message(member, "Bem vindo a " + server.name)
    print("Foi mandado uma mensagem para ", member.name)

@client.event
async def on_message(message):

    if message.content.startswith("-"):
            response = bot.get_response(message.content)
            if float(response.confidence) > 0.5:
                await client.send_message(message.channel, response)
            else:
                await client.send_message(message.channel, "Não confio em você")

  
client.run(process.env.BOT_TOKEN);
