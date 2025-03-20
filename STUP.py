import time
import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.GREEN+"Welcome to the setup!")
time.sleep(3)
choice = input("Would you like to start installing? "+Style.RESET_ALL+"("+Back.GREEN+Fore.BLACK+"Y"+Back.BLACK+Fore.WHITE+"/"+Back.RED+Fore.BLACK+"n"+Fore.WHITE+Back.BLACK+")")
if choice == "" or choice == "Y" or choice == "y":
    print(Fore.BLACK+Back.BLUE+"Initiating setup...")
elif choice == "N" or choice == "n":
    print("Exiting setup...")
    time.sleep(3)
    sys.exit()
    
print(Style.RESET_ALL+"Startng setup in 5 seconds...")
time.sleep(5)
print("Now starting setup...")
time.sleep(3)
print("Downloading data...")
time.sleep(3)
# print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {} %")
# time.sleep(5)
# print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {##################################################} %")

print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {--------------------------------------------------} %0")
time.sleep(1)
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {#########################-------------------------} %50")
time.sleep(1)
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {##################################################} %100")
time.sleep(3)
for i in range(50):
    print("")
# print("                      "+Fore.BLACK+Back.BLUE+"Finishing up...")
print("                                      "+Fore.BLACK+Back.BLUE+"Finishing up..."+Style.RESET_ALL)
time.sleep(10)
print("DONE! ENJOY!")

