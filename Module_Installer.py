import subprocess
import socket
import sys
import warnings

def is_Connect():
	try:
		x = socket.create_connection(("www.google.com",80))
		if x is not None:
			x.close
		return True
	except OSError:
		pass
	return False

def main(name):
	try:
		subprocess.check_call([sys.executable,"-m","pip","install",name])
		print(f"{name} is successfully Installed ")
		return True
	except ConnectionError:
		print(f"{name} is Unsuccessfully Installed ")
		print(" Check Internet Connection stable")
		return False
		

def getname():
	temp=input(" Enter the Module Name :  ")
	if temp.isalnum():
		print(" module can't have numberic character")	
	else:
		return temp

if __name__ == "__main__":	
	if is_Connect():
		numtimes = 1
		numtimes =int(input(" Enter the Number of times : "))	
		while numtimes>0: 
			name = getname()
			if name:
				main(name)
			numtimes-=1
	else:
		# print(" Please Connect Internet required this process ")
		warnings.warn("Please Connect InterNet Connection Required This Process")