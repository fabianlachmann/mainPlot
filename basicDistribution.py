import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d

size = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
Messgrössen = [[0.38,0.54],[0.54,0.78],[0.78,1],[1,1.3],[1.3,1.6],[1.6,2.1],[2.1,3],[3,4],[4,5],[5,6.5],[6.5,8],[8,10],[10,12],[12,14],[14,16],[16,17]]


def basicDistribution(data,k):
    x = []
    y = []
    y2 = []

    for row in data:
        for i in range(16):
            x.append(size[i])
            y.append(float(row[k+i]))# siehe Physik unserer Umwelt Die Atmosphäre S.18 /(math.log10(Messgrössen[i][1])-math.log10(Messgrössen[i][0]))


        plt.plot(x, y, marker='s',label = "Korrigiert")
        #plt.plot(x,y2,marker = 's',label = "Normal")

        # Format Plot
        plt.title("Mittlere Konzentrationen", fontsize=24)#"Aerosol Konzentration am " + row[0] + "." + row[1] + ". um " + row[2] + " Uhr"
        plt.xlabel('Durchmesser $[\mu m]$', fontsize=16)
        plt.ylabel("$dN/dlogD\;[m^{-3}]$", fontsize=16)
        plt.yscale('log')
        plt.xscale('log')
        plt.ylim(10**3.5,10**7.8)
        #plt.xticks([0.38, 0.54, 0.78, 1, 1.3, 1.6, 2.1, 3, 4, 5, 6.5, 8, 10, 12, 14, 16, 100])
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.legend(loc ="upper right",fontsize = 16)
        plt.show()

        x = []
        y = []
    # plt.legend(loc='upper right')
    # plt.show()