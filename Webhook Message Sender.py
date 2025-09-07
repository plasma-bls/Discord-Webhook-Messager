import dhooks
from dhooks import Webhook
import colorama
from colorama import Fore
import os
import sys
import time
from time import sleep
colorama.init()

def start():
   print(Fore.RED + '''

 __        __   _     _   _             _      __  __                                  ____                 _           
 \ \      / /__| |__ | | | | ___   ___ | | __ |  \/  | ___  ___ ___  __ _  __ _  ___  / ___|  ___ _ __   __| | ___ _ __ 
  \ \ /\ / / _ \ '_ \| |_| |/ _ \ / _ \| |/ / | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \ \___ \ / _ \ '_ \ / _` |/ _ \ '__|
   \ V  V /  __/ |_) |  _  | (_) | (_) |   <  | |  | |  __/\__ \__ \ (_| | (_| |  __/  ___) |  __/ | | | (_| |  __/ |   
    \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_|  |_|\___||___/___/\__,_|\__, |\___| |____/ \___|_| |_|\__,_|\___|_|   
                                                                          |___/                                         
   ''')


   webhook_link = input(Fore.GREEN + "Enter the webhook URL > ")
   while True:
      data1 = input(Fore.GREEN + "Messagge (Q to quit) [o]> ")
   
      hook = Webhook(webhook_link)
      if data1 == "Q":
         print(Fore.GREEN + "Have a great day!")
         time.sleep(2)
         sys.exit()
      else:
         hook.send(f"{data1}")

start()

