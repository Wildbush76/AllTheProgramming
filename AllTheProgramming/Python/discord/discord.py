import os
import discord#import serial
#ser = serial.Serial('COM6',9600,timeout = 0.050)
state = 0
client = discord.Client()
@client.event
async def on_ready():
    print(f'{clinet.user} has connected to Discord')
client.run("")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (message.content == '?blink'):
        #ser.write(str(state).encode())
        print('recvived')
        
        
