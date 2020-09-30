# Hier File auswählen und dann zu funtion in anderem file schicken
from basicDistribution import *
from heatmap import *
from plot3D import *
from QuantrelVal import *
from mathplot import *


import numpy as np
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d


data = []
k=3
with open(askopenfilename()) as csv_file:#öffnet das csv-file
    csv_reader = csv.reader(csv_file, delimiter=',') #initialisiert den Reader fürs csv
    for row in csv_reader:
        if row == []:
            continue
        elif row[0] == "Month":
            k = 3
            continue
        elif row[0] == "Station":
            k = 8
            continue
        elif row[0] == "Timecode":
            print(row[4])
            k = 4
            continue
        data.append(row)



#basicDistribution(data,k)
#basicheatmap(data,k)
#plot3D(data,k)
QuantrelVal(data,k,25,33)