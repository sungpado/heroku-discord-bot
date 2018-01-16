import asyncio
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)


@client.event
async def on_message(message):
    print("Message received!")
    print(message.mentions[0].name)
    if client.user.name in [mention.name for mention in message.mentions]:
        await client.send_message(message.channel, ":D")

client.run(os.environ['DISCORD_TOKEN'])

