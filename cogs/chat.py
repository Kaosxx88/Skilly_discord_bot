#!/usr/bin/env python3

import discord
from discord.ext import commands

class Chat(commands.Cog):

	def __init__(self, client):
		self.client = client

	'''  Ready Event '''

	@commands.Cog.listener()
	async def on_ready(self):
		print('\n...Chat module loaded correctly...')


	''' Clear method ( with permission ) '''

	@commands.command(help = '---> Clear x lines (def = 5)``` ```diff\n')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=5 , * , extra=None ):

		if extra:
			await ctx.send( f'```diff\n- To many arguments... Cunt!\n```' )

		else:
			await ctx.channel.purge(limit=amount)

def setup(client):
	client.add_cog(Chat(client))
