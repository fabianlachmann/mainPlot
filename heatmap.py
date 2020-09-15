import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d

size = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
Messgrössen = [[0.38,0.54],[0.54,0.78],[0.78,1],[1,1.3],[1.3,1.6],[1.6,2.1],[2.1,3],[3,4],[4,5],[5,6.5],[6.5,8],[8,10],[10,12],[12,14],[14,16],[16,100]]


def twoDplot(data,k):
    #data = data[153:193]
    x = []
    X = []
    y = []
    Y = []
    z = []
    Z = []

    #for row in data:
    #    x.append(float(row[0])+(float(row[k+1])/30)+(float(row[2])/(30*24)))

    for i in range(len(data)):
        x.append(i)

    for entry in size:
        X.append(x)

    for i in range(len(data[0][3:19])):
        z=[]
        for row in data:
            z.append(float(row[i+k])*1000)
        Z.append(z)

    for entry in Messgrössen:
        y = []
        for row in data:
            y.append(entry[0])
        Y.append(y)


    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)


    fig = plt.figure()
    plt.pcolormesh(Y,X,Z,cmap='jet',norm = matplotlib.colors.LogNorm(),shading='gouraud')
    plt.xscale('log')
    plt.ylabel("Measurement",fontsize = 'x-large',fontweight='bold')
    plt.colorbar()
    plt.legend()
    plt.xlabel("r $[\mu m]$",fontsize= 'x-large',fontweight='bold')
    plt.show()
