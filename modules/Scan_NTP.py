import nmap
import masscan
import pymongo
import time
import queue

err_q=queue.Queue()
mdb=pymongo.MongoClient().scan.ntp

def scan():
    global err_q
    global mdb

    m=masscan.PortScanner()
    n=nmap.PortScanner()
    for ip in range(1,255):
        try:
            ips=ip+'.0.0.0/8'
            m.scan(hosts=ips,ports='U:123',arguments='--rate=10000')
        except:
            try:
                time.sleep(10)
                ips=ip+'.0.0.0/8'
                m.scan(hosts=ips,ports='U:123',arguments='--rate=10000')
            except:
                err_q.put(ip+'0.0.0/8')

        if m.all_hosts() != []:
            for IP in m.all_hosts():
                try:
                    n.scan(hosts=IP,ports='U:123',arguments='-sU -Pn -n --script=ntp-monlist')
                except:
                    try:
                        n.scan(hosts=IP,ports='U:123',arguments='-sU -Pn -n --script=ntp-monlist')
                    except:
                        continue
                if type(n[IP]['udp'][123].get('script')) == dict:
                    if n[IP]['udp'][123]['script'].get('ntp-monlist') != None:
                        if len(n[IP]['udp'][123]['script']['ntp-monlist'])>400:
                            mdb.insert_one({'IP':IP})
    f=open('./err_q_ip.txt','rw+')
    while not err_q.empty():
        ips=err_q.get()
        f.write(ips+'\n')
        print(ips)
    f.close()
                              
if __name__ == '__main__':
    scan()                       

