import time
import os
import sys
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import platform
import psutil
import random
import string
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("COINHUNT VERSION 2.3 - STATUS: IDLE")

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (------------)                                  ","cyan"))
print(colored("                               IMPORTING LIBS.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (====>-------)                                  ","cyan"))
print(colored("                             CHECKING RESOURCES.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (========>---)                                  ","cyan"))
print(colored("                            ALLOCATING RESOURCES.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","cyan"))
print(colored("                                LOAD SUCCESS.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
clear()
print("")
time.sleep(0.03)
print("")
time.sleep(0.03)
print(colored("               █████╗  █████╗ ██╗███╗  ██╗██╗  ██╗██╗   ██╗███╗  ██╗████████╗","cyan"))
time.sleep(0.03)
print(colored("              ██╔══██╗██╔══██╗██║████╗ ██║██║  ██║██║   ██║████╗ ██║╚══██╔══╝","cyan"))
time.sleep(0.03)
print(colored("              ██║  ╚═╝██║  ██║██║██╔██╗██║███████║██║   ██║██╔██╗██║   ██║   ","cyan"))
time.sleep(0.03)
print(colored("              ██║  ██╗██║  ██║██║██║╚████║██╔══██║██║   ██║██║╚████║   ██║   ","cyan"))
time.sleep(0.03)
print(colored("              ╚█████╔╝╚█████╔╝██║██║ ╚███║██║  ██║╚██████╔╝██║ ╚███║   ██║   ","cyan"))
time.sleep(0.03)
print(colored("               ╚════╝  ╚════╝ ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝   ","cyan"))
time.sleep(0.03)
print("")
time.sleep(0.03)
print("")


welcome = Fore.CYAN + "Welcome back, Ready to hunt some coins?\n"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)

threads = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "coinhunt threads set 120\n"
for char in threads:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "Successfully set threads to 120.")

server = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "coinhunt server connect fastest\n"
for char in server:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "Checking subscription...")
time.sleep(1.0)
print(Fore.LIGHTMAGENTA_EX + "Subscription valid!")
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Connecting to 'DENMARK-2'!")
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Connected.")

start = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "coinhunt hunt start\n"
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)



time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Launching hunter.")
time.sleep(1.5)

print("")
print("")

ctypes.windll.kernel32.SetConsoleTitleW("COINHUNT VERSION 2.3 - STATUS: MINING")

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.CYAN + "COINHUNT" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTRED_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.RED + "0.002785 BTC" + Fore.WHITE + "]")

for i in range(2500):
    get_random_string(35)
    time.sleep(0.02)
    


def get_random_win(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.CYAN + "COINHUNT" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTGREEN_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "0,002785 BTC" + Fore.WHITE + "]")

time.sleep(0.3)

get_random_win(35)

time.sleep(0.5)

ctypes.windll.kernel32.SetConsoleTitleW("COINHUNT VERSION 2.3 - STATUS: FOUND BTC!")

print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "COINHUNT" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " SAVING '1.34 BTC' TO WALLET.TXT" + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]") 
time.sleep(1)
print("")

do
X=MsgBox("Error while transferring. Do you want to fix it?",0+48,"Computer")
X=MsgBox("Your computer has been hacked. Do you want to fix it?",0+48,"Computer")
X=MsgBox("357869 virusses are detected!",0+48,"virus Scanner") 
X=MsgBox("Are you sure?",0+48,"Computer")
X=MsgBox("Your stupid lmao",1+64,"AstraZ") 
loop




