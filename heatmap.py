import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
import scipy as s
from scipy.interpolate import griddata

size = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
Messgrössen = [[0.38,0.54],[0.54,0.78],[0.78,1],[1,1.3],[1.3,1.6],[1.6,2.1],[2.1,3],[3,4],[4,5],[5,6.5],[6.5,8],[8,10],[10,12],[12,14],[14,16],[16,17]]


def basicheatmap(data,k):
    #data = data[95:95+90]
    x = []
    X = []
    y = []
    Y = []
    z = []
    Z = []

    # for row in data:
    #     x.append(float(row[k-3])+(float(row[k-2])/30)+(float(row[k-1])/(30*24)))

    for i in range(len(data)):
        x.append(i)

    for entry in size:
        X.append(x)

    for i in range(len(data[0][3:19])):
        z=[]
        for row in data:
            z.append(float(row[i+k]))
        Z.append(z)

    for entry in Messgrössen:
        y = []
        for row in data:
            y.append(entry[0])
        Y.append(y)


    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)

    # points = []
    # n=0
    # for row in data:
    #     for i in range(16):
    #         points.append([row[0],size[i]])
    #         if float(row[k + i]) < 3:
    #             Z.append(3)
    #             continue
    #         Z.append(float(row[k+i]))
    #
    #
    #
    #     n+=1



    # f = interp2d(X, Y,Z, kind='cubic')
    # xnew = np.arange(np.min(X), np.max(X), 0.05)
    # ynew = np.arange(np.min(Y),np.max(Y), 0.05)
    # data1 = f(xnew, ynew)
    # Xn, Yn = np.meshgrid(xnew, ynew)
    # plt.pcolormesh(Xn, Yn, data1, cmap='RdBu')



    # grid_x, grid_y = np.mgrid[7:10:5000j, 0.38:16.5:200j]
    # grid_z2 = griddata(points, Z, (grid_x, grid_y), method='cubic')


    fig = plt.figure()
    plt.pcolormesh(X,Y,Z,cmap='jet',norm = matplotlib.colors.LogNorm())
    plt.yscale('log')
    #plt.xlim(7.3,9.3)
    plt.ylabel("Durchmesser $[\mu m]$",fontsize = 'x-large',fontweight='bold')
    plt.colorbar(label = '$ dN/d\logr$')
    plt.xlabel("Monate",fontsize= 'x-large',fontweight='bold')
    plt.show()
