import pyfiglet
from os import system, name
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[92m'
    MAIN = '\033[95m'
    MAIN1 = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
namemain = "bluesnarfer"
permite = "sudo apt"
ascii_banner = pyfiglet.figlet_format("Installing....")
print(bcolors.MAIN+ascii_banner)
print(bcolors.MAIN1+"                                       BlueHunter V1.0")
print(" ")
print(" ")
os.system("mkdir -p /dev/bluetooth/rfcomm")
os.system("mknod -m 666 /dev/bluetooth/rfcomm/0 c 216 0")
os.system(permite+" install "+namemain)