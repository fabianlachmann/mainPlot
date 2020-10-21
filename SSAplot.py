import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d
import scipy.optimize as opt

size = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
Messgrössen = [[0.38,0.54],[0.54,0.78],[0.78,1],[1,1.3],[1.3,1.6],[1.6,2.1],[2.1,3],[3,4],[4,5],[5,6.5],[6.5,8],[8,10],[10,12],[12,14],[14,16],[16,17]]



def SSAplot(data,a,b,w,y,z):
    x = []
    S = []
    Gong = []
    Schwarz = []
    Andreas = []
    n = 0
    for row in data:
        x.append(float(row[a]))
        S.append(float(row[b]))
        Schwarz.append(float(row[w]))
        Gong.append(float(row[y]))
        Andreas.append(float(row[z]))
        #color.append(float(row[k+8]))
        n+=1

    # xmittel = [i+10 for i in range(14)]#43
    # print(xmittel)
    # ymittel = [0 for i in range(14)]
    # ncount = [0 for i in range(14)]
    # for row in data:
    #     ymittel[int(float(row[k+a])-10)] += float(row[k+b])
    #     ncount[int(float(row[k+a])-10)] += 1
    #
    # for i in range(len(ymittel)):
    #     if ncount[i]==0:
    #         continue
    #     ymittel[i] = ymittel[i]/ncount[i]



    #plt.plot(x, S,marker = 's',label = "Datenpunkte")#c = color, cmap = 'jet',norm = matplotlib.colors.LogNorm()
    plt.scatter(x,Gong, 'r--',marker = '^')
    plt.scatter(x,Schwarz, 'g--',marker = '^')
    plt.scatter(x,Andreas, 'b--',marker = '^')
    #Format Plot
    #plt.yscale('log')
    #plt.xscale('log')
    #plt.ylim(0, 10**8)
    #plt.xlim(0,10)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.title("n = "+str(n))
    #plt.colorbar(label='$7.25\mu m$[1/m3]')

    print(x)
    print(y)

    xn = np.array(S).reshape((-1, 1))
    yn = np.array(Gong)

    model = LinearRegression()
    model.fit(xn, yn)
    r_sq = model.score(xn, yn)
    print(r_sq)
    print(model.intercept_)
    print(model.coef_)

    xn = np.linspace(0, max(x), 100)
    yn = model.coef_ * xn + model.intercept_

    plt.plot(xn, yn, 'r--')

    plt.show()


    # plt.plot(np.linspace(60,100,1000),func(np.linspace(60,100,1000) , *popt),color = 'r',label = str(a)+'$x^6+$'+str(b)+'$x^5+$'+str(c)+'$x^4+$'+str(d)+'$x^3+$'+str(e)+'$x^2+$'+str(f)+'$x+$' +str(g))#label = str(a)+'$x^6+$'+str(b)+'$x^5+$'+str(c)+'$x^4+$'+str(d)+'$x^3+$'+str(e)+'$x^2+$'+str(f)+'$x+$' +str(g)
    # plt.scatter(xmittel,ymittel,color = 'r',label = 'Nach Temperatur gewichtete Mittel')
    # plt.legend(loc = "upper left",fontsize = 13)


    plt.show()



