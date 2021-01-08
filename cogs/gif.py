#!/usr/bin/env python3

import discord
from discord.ext import commands
import random
import giphy_client
from giphy_client.rest import ApiException

''' Giphy Token '''

giphy_token = 'YOUR_GIPHY_TOKEN_HERE'

''' Custom gif '''

gif_1 = "https://giphy.com/gifs/7x0Q9F50Mo7c2lwNCj"

gif_2 = "https://giphy.com/gifs/ReNp5xRPYRCKwYvY47"

gif_3 = "https://giphy.com/gifs/DLM7Q1vcYFAsRcJPmq"


''' Giphy Instance '''

api_instance = giphy_client.DefaultApi()

''' Functions Search Giphy '''

def search_gifs(query):
    try:
        return api_instance.gifs_search_get(giphy_token, query, limit=5, rating = 'g')

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

def gif_response(emotion):
    gifs = search_gifs(emotion)
    lst = list(gifs.data)
    gif = random.choices(lst)

    return gif[0].url

''' Start Class bot '''
 
class Gif(commands.Cog):

	def __init__(self, client):
		self.client = client

	''' Event on ready '''

	@commands.Cog.listener()
	async def on_ready(self):
		print('\n...Gif module loaded correctly...')

	''' Event gif '''

	@commands.command( help = '---> Load a gif from giphy.com ( Special retarded, same, lmao )``` ```')
	async def gif(self, ctx, gif_name , * , extra= None):

		if extra:
			await ctx.send("```diff\n- To many argument stupid.... \n```")
		else:
			if gif_name == "retarded":
				await ctx.send(gif_1)
			elif gif_name == "same":
				await ctx.send(gif_2)
			elif gif_name == "lmao":
				await ctx.send(gif_3)
			else:
				await ctx.send(gif_response(gif_name))

	''' Error handling for gif '''
		
	@gif.error
	async def gif_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('```diff\n- MissingRequiredArgument :\n+ gif <name>\n```')

def setup(client):
	client.add_cog(Gif(client))
