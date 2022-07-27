import discord
import os
import asyncio
from itertools import cycle

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def reminder(message):
    time = float(str(message.content).split()[1]) * 60 * 60
    return time

@client.event
async def on_message(message):
    print(f"{message.content}")
    if message.author == client.user:
        return

    if '<@!350128482833006592>' in message.content.lower():
        await message.channel.send(f"<@!{message.author.id}> That's not very Bong Bong.")

    if '<@350128482833006592>' in message.content.lower():
        await message.channel.send(f"<@!{message.author.id}> That's not very Bong Bong.")

    if '<@430306959393161217>' in message.content.lower():
        await message.channel.send(f"<@!{message.author.id}> Ohoho so you have decided to summon the lord, that aint very bong bong.")

    if '<@!430306959393161217>' in message.content.lower():
        await message.channel.send(f"<@!{message.author.id}> Ohoho so you have decided to summon the lord, that aint very bong bong.")

    if 'family' in message.content.lower():
        await message.channel.send(f"https://cdn.discordapp.com/attachments/813372180087439420/857919727481389056/unknown.png")

    if '!remind' in message.content.lower():
        msg = message.content.split()
        remind = ''
        i = 2
        while i <len(msg):
          remind += ' '+ msg[i]
          i += 1
        time = reminder(message)
        hours = time / 3600
        await message.channel.send(f"<@!{message.author.id}> Reminder in {hours} hours,Message:{remind}")
        await asyncio.sleep(time)
        await message.channel.send(f"<@!{message.author.id}> Reminder from {hours} hours ago,Message:{remind}")



status = [':eyes:','Bong Bong','Pan Peko','http://dis.gd/threads']
async def change_status():
    await client.wait_until_ready()
    stat = cycle(status)

    while not client.is_closed():
        current_status = next(stat)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(60)



client.loop.create_task(change_status())

client.run(os.getenv('TOKEN'))