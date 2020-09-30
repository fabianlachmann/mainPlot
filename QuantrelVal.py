import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d

size = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
Messgrössen = [[0.38,0.54],[0.54,0.78],[0.78,1],[1,1.3],[1.3,1.6],[1.6,2.1],[2.1,3],[3,4],[4,5],[5,6.5],[6.5,8],[8,10],[10,12],[12,14],[14,16],[16,100]]



def QuantrelVal(data,k,a,b):

    x = []
    y = []
    n = 0
    for row in data:
        x.append(float(row[k+a]))
        y.append(float(row[k+b]))
        n+=1

    plt.scatter(x, y)

    # Format Plot
    # plt.xlabel('Diameter $[\mu m]$', fontsize=16)
    # plt.ylabel("$dN/dlogD\;[m^{-3}]$", fontsize=16)
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.ylim(0, 10 ** 7)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.title("n = "+str(n))

    print(x)
    print(y)

    xn = np.array(x).reshape((-1,1))
    yn = np.array(y)

    model = LinearRegression()
    model.fit(xn,yn)
    r_sq = model.score(xn,yn)
    print(r_sq)
    print(model.intercept_)
    print(model.coef_)

    xn = np.linspace(0,max(x),100)
    yn = model.coef_*xn + model.intercept_

    plt.plot(xn,yn)
    plt.show()






