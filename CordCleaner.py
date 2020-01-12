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

token = config.get('SETTINGS', 'token')
command = config.get('SETTINGS', 'command')

os.system("title CordCleaner - 4W#2100")
def clear():
    os.system('init' if os.name == '' else 'cls')

client = discord.Client()

clear()

if token == "Token":
    print ("[!] You need to setup your token!")
    time.sleep(3)
    print("[!] Shutting down...")
    sys.exit()

print("")
print("")
print("CORD CLEANER | By 4W#2100")
print("")
print("")
print("Logging in - Please hold on")
print("")

t = str(token)
@client.event
async def on_ready():
    print("Your Token: ***************" + t[15:])
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
