import requests
import json
import pymongo
from Crypto.Hash import SHA
#from bson.objectid import ObjectId

def Get_whitelist():
	col=pymongo.MongoClient().Jormungabdr.targets
	r=requests.get('http://ftp.apnic.net/stats/apnic/delegated-apnic-extended-latest')
	
	sha=SHA.new()
	sha.update(b"{r.text}")
	if sha.hexdigest() == col.find_one({})['md5']:
		return 1
	else:
		col.remove({})
		col.insert_one({'md5':sha.hexdigest()})
		r=r.text.split('\n')
		for i in r:
			if len(i.split['|']) >=2:
				i=i.split['|']
				if i[1] == 'CN':
					if ip[2] == 'ipv4':
						col.insert_one({'ipv4':ip[3]})
					elif ip[2] == 'ipv6':
						col.insert_one({'ipv6':ip[3]})
			else:
				continue
		return 1

