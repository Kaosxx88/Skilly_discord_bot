#!/usr/bin/env python3

import discord
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
import random
import os


#################### Variables #########################################################

''' Token of the bot '''
with open ( "token.txt" , "r") as tk:
	token = tk.readline()

''' Trigger word for the bot '''

bot_trigger_names = ['molly, ', 'Molly, ', 'skilly, ', 'Skilly, ', 'bot, ' , 'fucker, ' , 'M, ' , 'm, ' , 'S, ', 's, ']

''' bot status '''

message_status = [ 'with your sister...!','with your Mamy...!','behind you...', 'Waiting for your stupid question...']

''' Answers in case of wrong commands'''

no_command_answers = [" ```css\nWhat do you want now?\nYou don't even know the commands......\n```" ,
				      " ```css\nAre you stupid or what?\n```" , 
				      " ```css\nLazy bastard, learn the commands!\n```",
				      " ```css\nYou are WRONG, so so Wrong...\n```",
				      " ```css\n__Fuck the Admin!!__\n```"] 

##################### Main program ######################################################

now = datetime.now()
print ( f"\nBot started --> {now.strftime('%B/%d/%Y %H:%M:%S')}")

''' Definition bot '''

client = commands.Bot(command_prefix = bot_trigger_names)

''' Messages Status ( discord.Status.idle )''' 

status = cycle(message_status)

''' Tasks '''

@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

''' login event '''

@client.event
async def on_ready():
	change_status.start()
	print(f'\nBot Name : {client.user.name} - {client.user.id}\n\nDiscord version: {discord.__version__}')

''' Load extension cogs '''

@client.command(help = '---> Load an extension')
async def load(ctx, extension ):
	client.load_extension(f'cogs.{extension}')

''' Unload extension cogs'''

@client.command(help = '---> Unload an extension``` ```')
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

''' Reload extension cogs'''

@client.command(help = '---> Reload an extension')
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

''' Error Handling All Event ( Command Not Found! ) '''

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):		
		response = random.choice(no_command_answers)
		await ctx.send(response)

''' Load the cog  ( External py file in folder ./cog )'''

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)

 


