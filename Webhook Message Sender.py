import dhooks
from dhooks import Webhook
import colorama
from colorama import Fore
colorama.init()
import os

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
   
   data1 = input(Fore.GREEN + "Messagge > ")

   hook = Webhook(webhook_link)
   hook.send(f"{data1}")
   
   c1 = input(Fore.GREEN + "Do you wanna send another message, y|n > ")
   if c1 == "y":
      os.system('cls' if os.name == 'nt' else 'clear')
      start()
   if c1 == "n":
      print(Fore.GREEN + "Have a great day!")
      input(Fore.GREEN + "Press enter to exit > ")

start()
