import subprocess
import platform
import socket
from datetime import datetime
import os

### Goal To make a terminal containing ###
# pinging
# Display desktop name and ip
# show date
# Open files in a diractory
# List files on a diractory


path='/mnt/C/'
host_name= socket.gethostname()
host_ip  = socket.gethostbyname(host_name)

print('Tman Terminal v_1.0')

while True:
	code=input(':~$ ')
	
	if code=='ping':
		host=input("Enter Website to ping: ")
		number=input("Enter How many times to ping: ")

		def ping(host):
			param="-n" if platform.system().lower()=='windows' else '-c'
			command=['ping',param,number,host]
			return subprocess.call(command)

		print(ping(host))

	if code=="whoami":
		print("IP address         :"+host_ip)
		print("Destop Name        :"+host_name)

	if code=="date":
		now = datetime.now()
		print("Currnet date:      :",now)

	if code=="lidir":
		path = os.getcwd()
		print(path)
		# print(dir_list)

	if code=="help":
		msg="Tman Terminal, version 1.0"
		print(msg,"\nThese commands are defined internally. Type 'help' to see the list of commands\n",
			"\nping","\nwhoami","\ndate","\nlidir","\nexit")

	if code=="exit":
		exit()

	# if code=="cd":
	# 	os.chir