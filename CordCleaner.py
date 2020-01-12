import discord
import asyncio
import json
import sys
import time
import os
import datetime
from configparser import ConfigParser


config = ConfigParser()

config.read('config.ini')

username = config.get('SETTINGS', 'username')
password = config.get('SETTINGS', 'password')

os.system("title CordCleaner - 4W#2100")
def clear():
    os.system('init' if os.name == '' else 'cls')

client = discord.Client()

clear()
with open('config.json', 'r') as handle:
    config = json.load(handle)
    token = (config["token"])
    if token == "Your Token":
        print ("You need to setup your token! - Run the program again (After setting up token)")
        time.sleep(5)
        sys.exit()
    command = (config["command"])
    print("")
    print("")
    print("CORD CLEANER | By 4W#2100")
    print("")
    print("")
    print("Logging in - Please hold on")
    print("")

@client.event
async def on_ready():
    print("Your Token: " + str(token))
    print("CordCleaner Command: " + str(command))
    print (f'Logged in as {client.user.name} | ID: {client.user.id}')
    print("")
    print ('Type "' + str(command) + '" in the channel you want to clean.')
    print("")
    print("")

@client.event
async def on_message(message):
    counter = 0
    if message.content.startswith(str(command)) and message.author == client.user:
        async for message in message.channel.history(limit=99999):
            try:
                if message.author == client.user:
                    await message.delete()
                    counter += 1
                else:
                    pass
            except:
                pass
        msg = "✅`Cleaned " + str(counter) + " messages.`"
        end = await message.channel.send(msg)
        print(f"Cleared {str(counter)} messages | {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("")
        await asyncio.sleep(1)
        await end.delete()

client.run(token, bot=False)
