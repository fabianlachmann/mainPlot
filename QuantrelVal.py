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



def QuantrelVal(data,k,a,b):
    #data = data[65:74]
    # res = 0.5
    # histavg = [0 for i in range(int(12/res))]
    # count = [0 for i in range(int(12/res))]
    x = []
    y = []
    color = []
    n = 0
    for row in data:
        x.append(float(row[k+a]))#/float(row[k+b+10])
        y.append(float(row[k+b]))
        #color.append(float(row[k+8]))
        n+=1

    xmittel = [i for i in range(43)]#43
    print(xmittel)
    ymittel = [0 for i in range(43)]
    ncount = [0 for i in range(43)]
    for row in data:
        ymittel[int(float(row[k+a]))] += float(row[k+b])
        ncount[int(float(row[k+a]))] += 1

    for i in range(len(ymittel)):
        if ncount[i]==0:
            continue
        ymittel[i] = ymittel[i]/ncount[i]




    # for row in data:
    #     histavg[int((float(row[k+a])/3.6)/res)] += float(row[k+b])/1000000
    #     count[int((float(row[k + a]) / 3.6) / res)] += 1
    #
    # for i in range(len(histavg)):
    #     if count[i] == 0:
    #         continue
    #     histavg[i] = histavg[i]/count[i]
    #
    # for i in range(int(12/res)):
    #     x.append(i*res)
    #     y.append(histavg[i])

    plt.scatter(x, y,marker = 's',label = "Datenpunkte")#c = color, cmap = 'jet',norm = matplotlib.colors.LogNorm()

    #Format Plot
    plt.xlabel('Windgeschwindigkeit[km/h]', fontsize=20)
    plt.ylabel("0.46 $\mu m$ [1/m3]", fontsize=20)
    #plt.yscale('log')
    #plt.xscale('log')
    plt.ylim(0, 7*10**7)
    #plt.xlim(0,10)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.title("n = "+str(n))
    #plt.colorbar(label='$7.25\mu m$[1/m3]')

    print(x)
    print(y)

    # xn = np.array(x)
    # yn = np.array(y)

    # def func(x, a, b, c,d,e,f,g):
    #     return g+f*x +e*x**2+d*x**3+c*x**4+b*x**5 +a*x**6
    #
    # popt, pcov = opt.curve_fit(func, xdata=xmittel, ydata=ymittel)
    # a = round(popt[0],3)
    # b = round(popt[1],3)
    # c = round(popt[2],3)
    # d = round(popt[3],3)
    # e  = round(popt[4],3)
    # f = round(popt[5],3)
    # g = round(popt[6],3)


    # plt.plot(np.linspace(60,100,1000),func(np.linspace(60,100,1000) , *popt),color = 'r',label = str(a)+'$x^6+$'+str(b)+'$x^5+$'+str(c)+'$x^4+$'+str(d)+'$x^3+$'+str(e)+'$x^2+$'+str(f)+'$x+$' +str(g))#label = str(a)+'$x^6+$'+str(b)+'$x^5+$'+str(c)+'$x^4+$'+str(d)+'$x^3+$'+str(e)+'$x^2+$'+str(f)+'$x+$' +str(g)
    plt.scatter(xmittel,ymittel,color = 'r',label = 'Nach Windgeschwindigkeit gewichtete Mittel')
    plt.legend(loc = "upper left",fontsize = 13)



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

    plt.plot(xn,yn,'r--')


    plt.show()






def meanplot(data,k,a):
    x = []
    y = []
    n = 0
    for row in data:
        y0 = 0
        c=0
        for i in range(16):
            y0 += float(row[k+i])*size[i]
            c += float(row[k+i])
        if c == 0:
            continue
        y.append(y0/c)
        x.append(float(row[k+a]))
        n+=1

    plt.scatter(x, y)
    plt.show()


def histogram(data,n):
    x = []
    k = 4
    c = 0
    for row in data:
        x.append(float(row[0]))
        c+=1

    fig,(a1,a2,a3,a4,a5) = plt.subplots(5,1)


    a1.hist(x,n)
    a1.set_title('Messungen und metereologische Bedingungen über die Zeit',fontsize = 'xx-large',fontweight = 'bold')
    a1.set_ylabel('Anzahl Mittel(h)')

    a1.set_xticks([7.1, 8,9, 9.5])#,fontsize = 'x-large'
    a1.set_yticks([0,5,10,15])#,fontsize = 'x-large'

    x = []
    y = []


    for row in data:
        x.append(float(row[0]))
        y.append(float(row[k+24]))


    a2.plot(x, y,'r--',marker = 's')
    a2.set_ylabel('Lufttemperatur [C]')
    a2.set_xticks([7.1, 8,9, 9.5])

    x = []
    y = []

    for row in data:
        x.append(float(row[0]))
        y.append(float(row[k + 25]))


    a3.plot(x, y, 'g--', marker='s')
    a3.set_ylabel('$U_{10}$ [km/h]')
    a3.set_xticks([7.1, 8,9, 9.5])
    x = []
    y = []

    for row in data:
        x.append(float(row[0]))
        y.append(float(row[k + 27]))

    a4.plot(x, y, 'm--', marker='s')
    a4.set_ylabel('RH%')
    a4.set_xticks([7.1, 8,9, 9.5])

    x = []
    y = []

    for row in data:
        x.append(float(row[0]))
        y.append(float(row[k + 35]))

    a5.plot(x, y, 'c--', marker='s')
    a5.set_xticks([7.1, 8,9, 9.5])
    a5.set_ylabel('Wassertemperatur [C]')
    a5.set_xlabel('Datum (Monate)',fontsize = 'xx-large')
    plt.show()









