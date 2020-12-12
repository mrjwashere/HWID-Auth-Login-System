import subprocess
import requests
import os, sys, time, traceback, pickle, random, colorama
os.system("cls")
print("Login System Made By Mr. J!")
theguys_hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip() #Pulls Up The Hwid Of The System
checking = requests.get("Your PasteBin Link To Store The HWID's") #Checks If The HWID Is Present In The Paste
try:
    if hwid in checking.text:
        pass
    else:
        print('You Tried!')
        print(f'HWID: {theguys_hwid}') 
        time.sleep(5)
except:
    print('Check Your WIFI!')
    time.sleep(5)
print('You are Logged in')
login = int(input("Please Press 1 to Countinue: "))
os.system("cls")
