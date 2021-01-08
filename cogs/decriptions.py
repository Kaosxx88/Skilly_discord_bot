#!/usr/bin/env python3

import discord
from discord.ext import commands
import base64
import requests
import hashlib
from bs4 import BeautifulSoup

class Decriptions( commands.Cog ):

	def __init__( self , client ):
		self.client = client

	''' On ready Event'''

	@commands.Cog.listener()
	async def on_ready( self ) :
		print ( '\n...Decriptions module loaded correctly...' )

	''' Commands Base64 conversion '''

	@commands.command( help = '---> Base64 encode / decode' )
	async def base64 ( self, ctx , mode , * , element ):

		''' Check if the selected mode is encode or decode '''

		if mode.lower() == 'encode' :
			code_encoded = base64.b64encode( element.encode ( 'utf-8' ) )
			await ctx.send( f'Input:```diff\n+ { element }\n```encode:```diff\n- { code_encoded }\n```' )

		elif mode.lower() == 'decode' :
			code_decoded = base64.b64decode( element ).decode( 'utf-8' )
			await ctx.send( f'Input:```diff\n- { element }\n```\ndecode:```diff\n+ { code_decoded }\n```' )
			
		else:
			await ctx.send( f'```diff\n- Input only encode/decode.... Fuckers..\n```' )


	''' Commans Md5 conversion '''

	@commands.command( help = '---> md5 hash -> local - crack  -> online' )
	async def md5(self , ctx , mode, * , element ):

		''' Check if the selected mode is encode or crack  '''

		if mode.lower() == 'hash':

			# Md5 function for hash ( import hashlib )

			encode = hashlib.md5(element.encode("utf-8")).hexdigest()

			await ctx.send(f"```diff\n- The md5 Hash for --> {element} is :\n+ {encode}\n```")

		elif mode.lower() == 'crack':	

			''' In case of website error it will let the user know ''' 

			try:

				''' Burp suite python request '''

				burp0_url = "https://md5.gromweb.com:443/?md5=%s" % (element)
				
				page = requests.get(burp0_url)

				soup = BeautifulSoup(page.text, 'html.parser')

				find_result = soup.find_all('p')[0].get_text()

				''' Check if the site find the answer or not '''

				# In the case the site dont find the hash in the db, it will print ( some error were encountered)

				if find_result == "Some errors were encountered:":

					await ctx.send( f"```diff\n- md5.gromweb.com\n+ Sorry, No hash found on the database```" )

				else:
					await ctx.send( f"```diff\n- md5.gromweb.com\n+ {find_result[111:]}```" )



				''' In case of website error it will let the user know '''

			except:
				await ctx.send(f'```diff\n- Web Site loading problem \n```')


 	

		else:
			await ctx.send(f'```diff\n- Input only encode/crack .... Fucker... \n```')

	''' Error Handling Just for the md5 commands '''

	@md5.error
	async def md5_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('```diff\n- MissingRequiredArgument :\n+ md5 <encode/crack > <Characters to be ...>\n```')


	''' Commands sha1 conversion '''

	@commands.command( help = '  ---> sha1 hash -> local - crack -> online' )
	async def sha1(self , ctx , mode, * , element ):

		''' Check if the selected mode is encode or crack  '''

		if mode.lower() == 'hash':

			# sha1 function for encode ( import hashlib )

			encode = hashlib.sha1(element.encode("utf-8")).hexdigest()

			await ctx.send(f"```diff\n- The sha1 hash for --> {element} is :\n+ {encode}\n```")

		elif mode.lower() == 'crack':	

			''' In case of website error it will let the user know ''' 

			try:

				''' Burp suite python request '''

				burp0_url = "https://sha1.gromweb.com/?hash=%s" % (element)
				
				page = requests.get(burp0_url)

				soup = BeautifulSoup(page.text, 'html.parser')

				find_result = soup.find_all('p')[0].get_text()

				''' Check if the site find the answer or not '''

				# In the case the site dont find the hash in the db, it will print ( some error were encountered)

				if find_result == "Some errors were encountered:":

					await ctx.send( f"```diff\n- sha1.gromweb.com\n+ Sorry, No hash found on the database```" )

				else:
					await ctx.send( f"```diff\n- sha1.gromweb.com\n+ {find_result[111:]}```" )


			except:
				await ctx.send(f'```diff\n- Web Site loading problem \n```')


	''' Error Handling Just for the sha1 commands '''

	@sha1.error
	async def sha1_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('```diff\n- MissingRequiredArgument :\n+ sha1 <hash/crack > <Characters to be ...>\n```')


	''' Commands sha256 conversion '''

	@commands.command( help = '---> sha256 hash ' )
	async def sha256(self , ctx , mode, * , element ):

		''' Check if the selected mode is encode or crack  '''

		if mode.lower() == 'hash':

			# Md5 function for encode ( import hashlib )

			encode = hashlib.sha256(element.encode("utf-8")).hexdigest()

			await ctx.send(f"```diff\n- The sha256 hash for --> {element} is :\n+ {encode}\n```")

		else:
			await ctx.send(f'```diff\n- Wrong parameter, The third parameter must be hash \n```')

	''' Error Handling Just for the sha256 commands '''

	@sha256.error
	async def sha256_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('```diff\n- MissingRequiredArgument :\n+ sha256 <encode/crack > <Characters to be ...>\n```')


	''' Commans sha512 conversion '''

	@commands.command( help = '---> sha512 hash ``` ```' )
	async def sha512(self , ctx , mode, * , element ):

		''' Check if the selected mode is encode or crack  '''

		if mode.lower() == 'hash':

			# sha512 function for hash ( import hashlib )

			encode = hashlib.sha512(element.encode("utf-8")).hexdigest()

			await ctx.send(f"```diff\n- The sha512 Hash for --> {element} is :\n+ {encode}\n```")

		else:

			await ctx.send(f'```diff\n- Wrong parameter, The third parameter must be hash \n```')

	''' Error Handling Just for the sha512 commands '''

	@sha512.error
	async def sha512_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('```diff\n- MissingRequiredArgument :\n+ sha512 <encode/crack > <Characters to be ...>\n```')




def setup(client):
	client.add_cog(Decriptions(client))
