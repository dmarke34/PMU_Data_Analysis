import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from numpy import dtype, float64

with open("pmuData.csv", 'r') as i:
    rawdata = list(csv.reader(i, delimiter= ','))

#read measurement arrays and set them in individual arrays
measurements = np.array(rawdata[1:], dtype=str)
pckNum = measurements[:,0]

volMag = measurements[:,2]
volAng = measurements[:,3]

curMag = measurements[:,4]
curAng = measurements[:,5]

freq = measurements[:,6]
rocof = measurements[:,7]

#add '0' as element to empty indexes
volMag[volMag=='']=0.0
volAng[volAng=='']=0.0
curMag[curMag=='']=0.0
curAng[curAng=='']=0.0
freq[freq=='']=0.0
rocof[rocof=='']=0.0

#string to float
pckNum = pckNum.astype(int)
volMag = volMag.astype(float)
volAng = volAng.astype(float)
curMag = curMag.astype(float)
curAng = curAng.astype(float)
freq = freq.astype(float)
rocof = rocof.astype(float)

combined = np.stack((pckNum,volMag, volAng, curMag, curAng, freq, rocof)).T
counter = 0
for x in combined:
    if combined[counter][1] == 0.0:
        combined = np.delete(combined, counter, 0)
        counter -= 1
    counter += 1

pd.DataFrame(combined, columns=['Packet' ,'Voltage Mag', 'Voltage Angle', 'Current Mag',
'Current Angle', 'Actual Frequency', 'ROCOF']).to_csv("filteredData.csv")
