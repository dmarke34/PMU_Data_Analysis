import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from numpy import dtype, float64

with open("pmuData.csv", 'r') as i:
    rawdata = list(csv.reader(i, delimiter= ','))

measurements = np.array(rawdata[1:], dtype=str)
pckNum = measurements[:,0]

volMag = measurements[:,2]
volAng = measurements[:,3]

curMag = measurements[:,4]
curAng = measurements[:,5]

freq = measurements[:,6]
rocof = measurements[:,7]

volMag[volMag=='']=0.0
volAng[volAng=='']=0.0
curMag[curMag=='']=0.0
curAng[curAng=='']=0.0
freq[freq=='']=0.0
rocof[rocof=='']=0.0

volMag = volMag.astype(float)
volAng = volAng.astype(float)
curMag = curMag.astype(float)
curAng = curAng.astype(float)
volAng = volAng.astype(float)
freq = freq.astype(float)
rocof = rocof.astype(float)

combined = np.stack((pckNum,volMag, volAng, curMag, curAng, volAng, freq, rocof)).T

pd.DataFrame(combined, columns='Packet').to_csv("filteredData.csv")
