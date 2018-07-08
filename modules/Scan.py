import nmap
import pymongo
import masscan

db=pymongo.MongoClient().scan_ip_info

def NTP_scan():
    global db
    m_scan=masscan.PortScanner()
    m_scan.scan(hosts='0.0.0.0',ports='123',arguments='--rate=100000')
    n_scan=nmap.PortScanner()
    for scan_ip in  m_scan.all_hosts:
        n_scan.scan(hosts=scan_ip,arguments='-Pn -n -sU -pU:123 --script=ntp_monlist.nse')
        if n[scan_ip]:
            col=db.NTP
            col.insert()



    for i in r.:

def DNS_scan(nets):
    global db


def SNMPv2_scan(net):
    global db