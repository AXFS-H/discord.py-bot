import discord
import json
import requests
import random
import datetime
from config import *

client = discord.Client()

prefix = '!'

limit = 50
search = 'ricardo_milos'

@client.event
async def on_ready():
  print('Ricardo Milos is ready to dance!')
  await client.change_presence(status=discord.Status.idle, activity=discord.Game("!ricardo"))

@client.event
async def on_message(message):
  if message.author == client.user: return

  if message.content.startswith('%sricardo' % prefix):
    req = requests.get('https://api.tenor.com/v1/search?media_filter=minimal&key=%s&q=%s&limit=%s' % (api_key, search, limit))
    if req.status_code == 200:
      results = json.loads(req.content)["results"]
      choice = random.choice(results)
      fileUrl = str(choice.get("media")[0].get("tinygif").get("url"))
      embed = discord.Embed(title="Ricardo is dancing", color=0xe63e58).set_footer(text="Ricardo Milos", icon_url="https://i.imgur.com/VJ8oioL.jpg").set_image(url=fileUrl)
      return await message.channel.send(embed=embed)
    else:
      return await message.channel.send("Sorry, something went wrong. Please try again")

client.run(token)