import time
import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()


print("Downloading data...")
time.sleep(3)
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {--------------------------------------------------} %0")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {=-------------------------------------------------} %1")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {#-------------------------------------------------} %2")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {#=------------------------------------------------} %3")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {##------------------------------------------------} %4")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {##=-----------------------------------------------} %5")
time.sleep(1) #Setup Waitinfg
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {###-----------------------------------------------} %6")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {###=----------------------------------------------} %7")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {####----------------------------------------------} %8")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {####=---------------------------------------------} %9")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {#####---------------------------------------------} %10")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")

print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {#########################-------------------------} %50")
time.sleep(1) #Setup Waiting
for i in range(50):
    print("")
print(Fore.BLACK+Back.GREEN+"Progress:" + Style.RESET_ALL+" {##################################################} %100")
time.sleep(3)