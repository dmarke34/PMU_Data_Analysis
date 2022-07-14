
from hashlib import new
import sys
from scapy.all import *
import struct
import pandas as pd

#read pcap file from Wireshark
p = rdpcap('C:/Users/gabea/Documents/testCapture.pcap') 

#address for pmu as source ip address
hx = '0x52'

#convert rawdata from Wireshark to PMU measurement data
def rawdata_conversion(pck, byte, offset):
    raw_data = raw(p[pck - 1])
    if hex(raw_data[29]) == hx:
        first_digit = hex(raw_data[(offset*16) + byte])    
        second_digit = hex(raw_data[(offset*16) + (byte+1)])    
        third_digit = hex(raw_data[(offset*16) + (byte+2)])    
        fourth_digit = hex(raw_data[(offset*16) + (byte+3)])
        
        first_final = str(first_digit[2:].zfill(2))    
        second_final = str(second_digit[2:].zfill(2))    
        third_final = str(third_digit[2:].zfill(2))    
        fourth_final = str(fourth_digit[2:].zfill(2))

        result = first_final + second_final + third_final + fourth_final 
        return round(struct.unpack('!f', bytes.fromhex(result))[0], 2)
    else:
        return


#initial package
x = 1000
df = pd.DataFrame([[x,rawdata_conversion(x, 6, 4), rawdata_conversion(x, 10, 4), rawdata_conversion(x, 14, 4), rawdata_conversion(x, 18, 4),
rawdata_conversion(x, 6, 5) ,rawdata_conversion(x, 10, 5)]],
index =[x], columns=['Packet','Voltage Mag', 'Voltage Angle', 'Current Mag', 'Current Angle', 'Actual Frequency', 'ROCOF'])
for x in range(1001, 1100, 1):
    #add new packages and concat them to the initial package DataFrame
    new_row = pd.DataFrame([[x,rawdata_conversion(x, 6, 4), rawdata_conversion(x, 10, 4), rawdata_conversion(x, 14, 4), 
    rawdata_conversion(x, 18, 4), rawdata_conversion(x, 6, 5) ,rawdata_conversion(x, 10, 5)]],
    index =[x], columns=['Packet','Voltage Mag', 'Voltage Angle', 'Current Mag', 'Current Angle', 'Actual Frequency', 'ROCOF'])
    df = pd.concat([df, new_row])

df.to_csv('pmuData.csv') 
#df.to_excel('pmuData.xlsx' , sheet_name="new_sheet_name" )
#print(df)