import discord
import os
import requests
# import asyncio
import time
from discord.ext import commands
from discord.ext.commands import Bot
import re
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")



TOKEssN= os.environ.get("bottoken")

client = discord.Client()

def url_checker(urls):
    url = None
    temp_type =type(urls[0])
    if temp_type==str:
        url=urls[0]
    elif temp_type in [list,tuple]:
        for i in urls[0]:
            if len(i)>0:
                url=i
                break

    if url!=None:
        logger.info(f"--checking : {url}")
        r = requests.get(url)
        if r.status_code==200:
            return (True,url)

    logger.error(f" -- invalid link :  {url}")
    return (False,url)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    url =message.content
    if message.author == client.user:
        return
    exp = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    validate =re.findall(exp, url)
    print(validate)
    if len(validate)>0:
        check = url_checker(validate)
        if check[0]:
            await message.channel.send("Valid")
        else:
            await message.channel.send(f"Invalid : {check[1]}")

client.run(TOKEssN)