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

xfloat = volMag.astype(float)
yfloat = volAng.astype(float)

combined = np.stack((xfloat, yfloat)).T

print(combined)