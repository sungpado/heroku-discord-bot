import asyncio
import discord
import os
import time as t
t2 = t.gmtime()
if t2.tm_wday == 0:
    w = '일'
elif t2.tm_wday == 1:
    w = '월'  
elif t2.tm_wday == 2:
    w = '화'
elif t2.tm_wday == 3:
    w = '수'
elif t2.tm_wday == 4:
    w = '목'
elif t2.tm_wday == 5:
    w = '금'
elif t2.tm_wday == 6:
    w = ''
else :
    pass

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)


@client.event
async def on_message(message):
    if message.content.startswith('~날짜'):
        await client.send_message(message.channel, '오늘은 {}요일입니다. :wink: '.format(w))
client.run('MzkwMDQzNTkwMzc1NTA1OTIx.DWB6hg.V6S3bBJjVZBo0sDfTfgnTcakJE8')
