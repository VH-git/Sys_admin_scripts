#!/usr/bin/env python3

import os, subprocess, time

#Victor Hermes
#Script 3
#Professor Weissman
#Due 2/25/2022

#colors for outputs
red = "\033[91m"
white = "\033[0m"
green = "\033[92m"
yellow = "\033[93m"

#main menu for selecting options
def mainMenu():
   print("\t*******************************************************")
   print(f"\t****************** {green}Shortcut Creater{white} *******************")
   print("\t*******************************************************")
   print("")
   print("")
   print("Enter Selection: \n")
   print("\t1 - Create a shortcut in your home directory.")
   print("\t2 - Remove a shortcut from your home directory.")
   print("\t3 - Run shortcut report.")
   print("")

   
def createShortcut():
   #asks user for text file to create shortcut
   os.system("clear")
   file = input(f'Please enter the file name to create a shortcut:\t')
   foundFile = subprocess.Popen('find / -name ' + file, shell=True, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.DEVNULL)
   foundFile.wait()
   path = foundFile.communicate()[0].strip()
   print(f"Searching for file...")
   time.sleep(4)
   if path == "":
      print(f"Sorry, could't find {red}" + file)
      print(f"{white}Returning to menu...")
      time.sleep(4)
   else:
      choice = input(f"Found {green}" + path + f"{white} Select Y/y to create shortcut: \n")
      if choice == "y" or choice == "Y":
         print("Creating shortcut, please wait")
         time.sleep(4)
         os.system("ln -s " + path)
         print(f"{green}Shortcut created!{white}")
         print("Returning to menu...")
         time.sleep(3)
      else:
         print("Canceling shortcut creation.")
         print("Returning to menu...")
         time.sleep(4)
 
def removeShortcut():
   #asks user for text file to delete shortcut
   os.system("clear")
   file = input(f'Please enter the file name to remove a shortcut:\t')
   foundFile = subprocess.Popen('find . -name ' + file, shell=True, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.DEVNULL)
   foundFile.wait()
   path = foundFile.communicate()[0].strip()
   print(f"Searching for file...")
   time.sleep(4)
   if path == "":
      print(f"Sorry, could't find {red}" + file)
      print(f"{white}Returning to menu...")
      time.sleep(4)
   else:
      choice = input(f"Are you sure you want to remove " + f"{green}" + path + f"{white} Select Y/y to remove shortcut: \n")
      if choice == "y" or choice == "Y":
         print("Removing shortcut, please wait")
         time.sleep(4)
         os.system("rm " + path)
         print(f"{green}Shortcut deleted!{white}")
         print("Returning to menu...")
         time.sleep(3)
      else:
         print("Canceling shortcut deletion.")
         print("Returning to menu...")
         time.sleep(4)
   
def report():
   os.system("clear")
   #searches for all symlinks
   print("\t*******************************************************")
   print(f"\t****************** {green}Shortcut Report{white} *******************")
   print("\t*******************************************************")
   print("\n")
   pwd = os.getcwd()
   print(f"Your current directory is {yellow}" + pwd + f"{white}.")
   links = subprocess.Popen("readlink *", universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
   links.wait()
   textFile = subprocess.Popen("find . -type l | cut -c 3-", universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
   textFile.wait()
   
   existingLinks = links.communicate()[0].strip()
   fileName = textFile.communicate()[0].strip()
   
   allLinks = existingLinks.split("\n")
   allFiles = fileName.split("\n")
   
  
   print("")
   print("")
   print(f"\n\nThe number of links is: {green}" + str(len(allLinks)) + f"{white}.\n")
   print(f"{yellow} Symbolic Link \t\t\t Target Path{white}")
   for i in range(len(allLinks)):
      print(" " + allFiles[i] + "\t\t\t " + allLinks[i])
   
   choice = input(f"\nTo return to the {yellow}Main Menu{white}, press {yellow}Enter{white}. Or select {yellow}R/r{white} to remove a link:\t")
   if(choice == "r" or choice == "R"):
      removeShortcut()
      
#while loop for the main code

while True:
   os.system("clear")
   mainMenu()
   usrInput = input(f'Please enter a {green}number (1-3){white} or {green}"Q/q"{white} to quit the program: ')
   if usrInput == "1":
      createShortcut()
   elif usrInput == "2":
      removeShortcut()
   elif usrInput == "3":
      report()
   elif usrInput == "q" or usrInput == "Q":
      os.system("clear")		
      print("Thank you, have a good day! Returning to shell.")
      time.sleep(4)
      exit(0)
   else:
      os.system("clear")		
      print("Not a valid input. Try again")
      time.sleep(4)
