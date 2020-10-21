# Hier File auswählen und dann zu funtion in anderem file schicken
from basicDistribution import *
from heatmap import *
from plot3D import *
from QuantrelVal import *
#from mathplot import *
from SSAplot import *

import numpy as np
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d
string1 = 'windspeedKmph'
string2 = '0.46[n/ml]'


data = []
k=4
with open("C:/Users/User/Desktop/Aerosol/Data/WolltihrdentotalenCronc_NeuSSA.CSV") as csv_file:#öffnet das csv-file "C:/Users/User/Desktop/Aerosol/Data/WolltihrdentotalenCronc_NeuSSA.CSV"
    csv_reader = csv.reader(csv_file, delimiter=',') #initialisiert den Reader fürs csv
    for row in csv_reader:
        if row == []:
            continue
        elif row[0] == "Month":
            print(row[3])
            k = 3
            for i in range(len(row)):
                if row[i] == string1:
                    a = i-k
                    print(row[a+k])
                if row[i] == string2:
                    b = i-k
                    print(row[b+k])
                    print(row[b+k+10])

            continue


        elif row[0] == "Station":
            print(row[8])
            k = 8
            for i in range(len(row)):
                if row[i] == string1:
                    a = i - k
                    print(row[a+k])
                if row[i] == string2:
                    b = i - k
                    print(row[b+k])

            continue


        elif row[0] == "Timecode":
            print(row[44])
            print(row[4])
            k = 4
            for i in range(len(row)):
                if row[i] == string1:
                    a = i - k
                    print(row[a+k])
                if row[i] == string2:
                    print(row[44])
                    print(row[45])
                    print(row[46])
                    print(row[47])
                    b = i - k
                    print(row[b+k])


            continue

        data.append(row)



#basicDistribution(data,k)
#basicheatmap(data,k)
#plot3D(data,k)
#QuantrelVal(data,k,a,b)
#histogram(data,100)
#meanplot(data,k,a)
SSAplot(data,a=0,b=44,w=45,y=46,z=47)