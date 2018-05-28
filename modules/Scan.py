import nmap
import pymongo

def scan(nets):
    n=nmap.PortScanner()
    r=n.scan(hosts=nets,arguments='--open -n -p -O',ports=)


    for i in r.:

