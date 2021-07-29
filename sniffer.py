import datetime
from pymongo import MongoClient
from scapy.all import *

client = MongoClient(port=27017)
db=client.paquetes

def print_pkt(pkt):
	time=datetime.now()
	datos = pkt[Raw].load.decode("utf-8")
	array_datos = datos.split(';')
	try:
		id_device = int(array_datos[1][3:])
	except Exception as ex:
		id_device = 0	
	paquete = { 'fecha': time, 'ip' : str(pkt[IP].src), 'puerto' : str(pkt.dport), 'datos' :  datos }
	result=db[str(id_device)].insert_one(paquete)

if __name__ == '__main__':
	sniff(filter='udp and port 6202', prn=print_pkt, store=0)
