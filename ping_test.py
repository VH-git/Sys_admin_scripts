#!/usr/bin/env python3

import os, subprocess, time


#Victor Hermes
#Script 1
#Professor Weissman
#Due 1/28/2022

#colors for outputs
red = "\033[91m"
white = "\033[0m"
green = "\033[92m"
yellow = "\033[93m"

gateway = os.popen('route -n | head -3 | tail -1 | tr -s " " | cut -d " " -f 2').read().strip()
#print(gateway)


def mainMenu():
	print("\t*******************************************************")
	print(f"\t**************{green}Ping Test TroubleShooting{white}****************")
	print("\t*******************************************************")
	#ping selections
	print("Enter Selection:\n")
	print("\t1 - Test connectivity to your gateway.")
	print("\t2 - Test for remote connectivity.")
	print("\t3 - Test for DNS Resolution.")
	print("\t4 - Display gateway IP address.")

def ping_gateway():
	os.system("clear")
	print("Testing connectivity to your gateway, please wait...")
	#ping statement for testing connectivity	
	ping = subprocess.Popen("ping -c 1 " + str(gateway) + " 2> /dev/null", shell=True, stdout=subprocess.PIPE)
	ping.wait()
	#if statement check for fail
	if ping.returncode != 0:
		print(f"Please inform your system administrator that the gateway test {red} FAILED{white}.")
	elif ping.returncode == 0:
		print(f"Please inform your system administrator that the gateway test was {green}SUCCESSFUL{white}.")
	time.sleep(4)
	os.system("clear")

def ping_remote():
	os.system("clear")
	print("Testing connectivity to a remote ip, please wait...")	
	ping = subprocess.Popen("ping -c 1 129.21.3.17 2> /dev/null", shell=True, stdout=subprocess.PIPE)
	ping.wait()
	
	if ping.returncode != 0:
		print(f"Please inform your system administrator that the remote test {red} FAILED{white}.")
	elif ping.returncode == 0:
		print(f"Please inform your system administrator that the remote test was {green}SUCCESSFUL{white}.")
	time.sleep(4)
	os.system("clear")

def ping_dnsResolution():
	os.system("clear")
	print("Testing connectivityfor DNS resolution, please wait...")	
	ping = subprocess.Popen("ping -c 1 google.com 2> /dev/null", shell=True, stdout=subprocess.PIPE)
	ping.wait()

	if ping.returncode != 0:
		print(f"Please inform your system administrator that the test {red} FAILED{white}.")
	elif ping.returncode == 0:
		print(f"Please inform your system administrator that the test was {green}SUCCESSFUL{white}.")
	time.sleep(4)
	os.system("clear")
def print_gateway():
	print("The gateway is " + gateway)
	time.sleep(4)
	os.system("clear")

while True:
	os.system("clear")	
	mainMenu()
	usrInput = input(f"Please enter a number {green}(1-4){white} or {green}Q/q{white} to quit: ")
	#if statement for each input
	if usrInput == "1":
		ping_gateway()
	elif usrInput == "2":
		ping_remote()
	elif usrInput == "3":
		ping_dnsResolution()
	elif usrInput == "4":
		print_gateway()
	elif usrInput == "q" or usrInput == "Q":
		os.system("clear")		
		print("Thank you, have a good day!")
		exit(0)
	else:
		os.system("clear")		
		print("Not a valid input. Try again")




