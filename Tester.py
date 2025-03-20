import time
import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()

time.sleep(3)
for i in range(15):
    print("")
    time.sleep(0.01)
#ed.fdsdssfddss
time.sleep(3.5)
print("                                                   "+Back.BLUE+"     "+Style.RESET_ALL+"  "+Back.LIGHTGREEN_EX+"     ")
time.sleep(1)
print(Style.RESET_ALL+"                                                   "+Back.BLUE+"     "+Style.RESET_ALL+"  "+Back.LIGHTGREEN_EX+"     ")
#Middle Blank Part
time.sleep(1)
print(Style.RESET_ALL+" ")
time.sleep(1)
#Normal Again
print(Style.RESET_ALL+"                                                   "+Back.LIGHTGREEN_EX+"     "+Style.RESET_ALL+"  "+Back.BLUE+"     ")
time.sleep(1)
print(Style.RESET_ALL+"                                                   "+Back.LIGHTGREEN_EX+"     "+Style.RESET_ALL+"  "+Back.BLUE+"     ")
time.sleep(1)
# print(Style.RESET_ALL+"                                                      "+Fore.BLUE+"Mega"+Fore.RED+"OS"+Style.RESET_ALL)
print(Style.RESET_ALL+"                                                      "+Fore.BLUE+"Mega"+Fore.RED+"O"+Fore.LIGHTGREEN_EX+"S"+Style.RESET_ALL)
time.sleep(1)
exec(open('/home/henery/Desktop/MegaOS/STUP.py').read())