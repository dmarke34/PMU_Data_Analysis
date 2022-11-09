
from hashlib import new
import sys
from scapy.all import *
import struct
import pandas as pd
import numpy as np


#read pcap file from Wireshark
p = rdpcap('C:/Users/Aaron/PCAP_Files/Test.pcap') 

#address for pmu as source ip address
hx = '0x52'
def main_function(p):
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

    #rect to polar (magnitude)
    def rect2polroh(x, y):
        if int(x or 0) | int(y or 0) != 0.0:
            rho = np.sqrt(x**2.0 + y**2.0)
            return (round(rho, 2))
        else:
            return

    #rect to polar (angle)
    def rect2polphi(x,y):
        if int(x or 0) | int(y or 0) != 0.0:
            phi = np.arctan2(y,x)
            return round(math.degrees(phi), 2)
        else:
            return

    #print(rect2pol(rawdata_conversion(1000, 6, 4), rawdata_conversion(1000, 10, 4)))    

    #initial package
    x = 0
    df = pd.DataFrame([[x,rawdata_conversion(x, 6, 4), rawdata_conversion(x, 10, 4), rawdata_conversion(x, 14, 4), rawdata_conversion(x, 18, 4),
    rawdata_conversion(x, 6, 5) ,rawdata_conversion(x, 10, 5)]],
    index =[x], columns=['Packet','Voltage Mag', 'Voltage Angle', 'Current Mag', 'Current Angle', 'Actual Frequency', 'ROCOF'])
    for x in range(1, 150, 1):
        #add new packages and concat them to the initial package DataFrame
        a = rawdata_conversion(x, 6, 4)
        b = rawdata_conversion(x, 10, 4)
        c = rawdata_conversion(x, 14, 4)
        d = rawdata_conversion(x, 18, 4)

        new_row = pd.DataFrame([[x,rect2polroh(a, b), rect2polphi(a, b), rect2polroh(c, d), 
        rect2polphi(c, d), rawdata_conversion(x, 6, 5) ,rawdata_conversion(x, 10, 5)]],
        index =[x], columns=['Packet','Voltage Mag', 'Voltage Angle', 'Current Mag', 'Current Angle', 'Actual Frequency', 'ROCOF'])
        df = pd.concat([df, new_row])

    df = df.iloc[1:]
    df.to_csv('pmuData.csv') 
    #df.to_excel('pmuData.xlsx' , sheet_name="new_sheet_name" )


main_function(p)