from hashlib import new
import sys
from scapy.all import *
import struct
import pandas as pd

#read pcap file from Wireshark
p = rdpcap('C:/Users/gabea/Documents/testCapture.pcap') 

hx = '0x52'
raw_data = raw(p[1089])
src_address = hex(raw_data[(29)])
if src_address == hx:
    print("Working")



