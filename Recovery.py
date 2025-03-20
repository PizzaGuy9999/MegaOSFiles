import time
import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.GREEN+"Welcome to the recovery system!")
time.sleep(3)
choice = input("Would you like to reinstall files? "+Style.RESET_ALL+"("+Back.GREEN+Fore.BLACK+"Y"+Back.BLACK+Fore.WHITE+"/"+Back.RED+Fore.BLACK+"n"+Fore.WHITE+Back.BLACK+")")
if choice == "" or choice == "Y" or choice == "y":
    print(Fore.BLACK+Back.BLUE+"Reinstalling......")
elif choice == "N" or choice == "n":
    print("Recovery mode exited....")
    time.sleep(3)
    sys.exit()