#!/usr/bin/python3

import os
import sys
import pymongo
from modules import Scan_NTP,Ssh_Cracked,Telnet_Cracked,GET_Whitelist

print('Welcome to Jormungandr system (^ ^)')
col=pymongo.MongoClient()

while True:
	print('''Please chose you modules!:
		1,ssh cracked
		2,ntp scan
		3,telnet scracked
		enter you chose number:
		''')
    client_chose=input('<<')
    
    resul=GET_Whitelist.Get_whitelist()

    if resul != 1:
    	print('Whitelist Falid!!!')
    	sys.exit(0)
    	
    if client_chose == '1':
    	Ssh_cracked.
    if client_chose == '2':
    	Scan_NTP.
    if client_chose == '3':
    	Telnet_cracked





