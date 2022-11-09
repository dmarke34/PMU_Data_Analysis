from scapy.all import *
from scapy.layers.inet import IP, TCP
conf.L3socket=L3RawSocket

sport=4712
dport=1793
pkt=IP(src="172.24.4.82", dst="172.24.4.90")

SYN=pkt/TCP(sport=sport, dport=dport, flags="S")
SYNACK=sr(SYN)
ACK=pkt/TCP(sport=sport, dport=dport, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1)
send(ACK)

# ...

FIN=pkt/TCP(sport=sport, dport=dport, flags="FA", seq=SYNACK.ack, ack=SYNACK.seq + 1)
FINACK=sr(FIN)
LASTACK=pkt/TCP(sport=sport, dport=dport, flags="A", seq=FINACK.ack, ack=FINACK.seq + 1)
send(LASTACK)