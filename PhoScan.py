#!/usr/bin/python

import requests
import subprocess
from time import sleep 
import string
import nmap
import random
import sys
import os

os.system("clear")

def banner():
 print(""" 
\t \033[91m _____  _     _  _____  _______ _______ _______ __   _
\t \033[91m|_____] |_____| |     | |______ |       |_____| | \  |
\t \033[91m|       |     | |_____| ______| |_____  |     | |  \_|\033[0m

\t \033[97m[*] Author  : Dominic404
\t \033[97m[*] Team    : PhobiaXploit
\t \033[97m[*] Version : 1.0
\t \033[97m[*] Port Scanning Takes a Long Time So Please Be Patient 
""") 

def help():
    print("""
\tCommand:
\t       set host      : Set Your Target Host(e.g set host 192.168.1.2)
\t       set metode    : Set Metode Scan(e.g set metode TCP_SYN) 
\t       Metode        : TCP_SYN, TCP_connect, UDP, TCP_NULL, FIN, Xmas 
\t       start         : Start Scanner  
\t       show          : Show host and metode
\t       clear         : Clean The Screen
\t       exit          : Exiting Tools 
   
\tContact:
\t       Facebook      : www.facebook.com/Dominic404
\t       Official Blog : www.phobiaxploit.me
\t       Email         : phobiaxploit@gmail.com
\t                     : fgaming386@gmail.com   
""")    
 
def main():
    global host, metode

    while True:
        px = raw_input("root@porsc:~# ").lower() 
            
        if px == 'banner':
            os.system("clear")
            banner()
            main()
            
        elif "clear" in px:
            os.system("clear")
          
        elif 'exit' in px:
            os.system("clear") 
            exit()    
            
        elif 'help' in px:
            os.system("clear")
            banner()
            help()  
            
        elif 'set host' in px:
           host = px.split()[-1]  
           
        elif 'set metode' in px:
            metode = px.split()[-1]  
           
        elif px == "show":
            print "\n[+] HOST   : %s\n[+] METODE  : %s\n"%(host,metode)   
            
        elif px == "start": 
            if host != " " and metode != " ":
            
                if metode == 'tcp_syn':
                    os.system("sudo nmap -sS %s\n"%(host))
                
                elif metode == 'tcp_connect':
                    os.system("sudo nmap -sT %s\n"%(host))
                
                elif metode == 'udp':
                    os.system("sudo nmap -sU %s\n"%(host))
                
                elif metode == 'tcp_null':
                    os.system("sudo nmap -sN %s\n"%(host))
                
                elif metode == 'fin':
                    os.system("sudo nmap -sF %s\n"%(host))
            
                elif metode == 'xmas':
                    os.system("sudo nmap -sX %s\n"%(host))
                else:
                    os.system("clear")
                    banner()
                    print"\n[*] HOST   : %s"%(host)
                    print"[*] Metode : %s"%(metode)
                    print"[!]The Method You Entered Is Incorrect\n"                      
            
            else:
                print"\n[*] HOST  : %s\n[*] METODE  : %s\n"%(host,metode)
            
        else:
            print("[+] What Your Entered Is Wrong . . .")
            main()      
            
def control():
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\n[+] CTRL+C Detected Exiting Tools...")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
    control()                                        
