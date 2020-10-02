import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d

def f(x,sig,dg):
    return (1/(math.sqrt(2*math.pi)*ln(sig)))*math.exp(-((ln(x)-ln(dg))**2/(2*ln(sig)**2)))


def ln(x):
    return math.log(x,math.e)



x = np.linspace(0.001,100,1000000)
y = []
y1 = []
y2=[]
for v in x:
    y.append(200*f(v,1.5,0.07)+50*f(v,3.5,0.15))
    y1.append(200*f(v,1.5,0.07))
    y2.append(50*f(v,3.5,0.15))


y = np.array(y)



fig,(a1,a2,a3) =  plt.subplots(1,3)
a1.plot(x,y1,'r--')
a1.plot(x,y2,'y--')
a1.plot(x,y,'b')
a1.set_title('Grössenverteilung',fontsize = 'xx-large')
a1.set_ylabel('$dN/d\ln{D}$',fontsize = 'xx-large')

a1.set_xlabel('Durchmesser',fontsize = 'xx-large')

a1.set_xscale('log')

y = []
y1=[]
y2=[]
for v in x:
    y.append(4*math.pi*v**2*(200*f(v,1.5,0.07)+50*f(v,3.5,0.15)))
    y1.append(4*math.pi*v**2*(200*f(v,1.5,0.07)))
    y2.append(4*math.pi*v**2*(50*f(v,3.5,0.15)))

a2.plot(x,y1,'r--')
a2.plot(x,y2,'y--')
a2.plot(x,y,'b')
a2.set_title('Flächenverteilung',fontsize = 'xx-large')
a2.set_ylabel('$dS/d\ln{D}$',fontsize = 'xx-large')

a2.set_xlabel('Durchmesser',fontsize = 'xx-large')
a2.set_xscale('log')


y = []
y1=[]
y2=[]
for v in x:
    y.append(4/3*math.pi*v**3*(200*f(v,1.5,0.07)+50*f(v,3.5,0.15)))
    y1.append(4/3*math.pi*v**3*(200*f(v,1.5,0.07)))
    y2.append(4/3*math.pi*v**3*(50*f(v,3.5,0.15)))


a3.plot(x,y1,'r--')
a3.plot(x,y2,'y--')
a3.plot(x,y,'b')
a3.set_title('Volumenverteilung',fontsize = 'xx-large')
a3.set_ylabel('$dV/d\ln{D}$',fontsize = 'xx-large')
a3.set_xlabel('Durchmesser',fontsize = 'xx-large')
a3.set_xscale('log')

fig.legend()
plt.show()

# plt.plot(x,y)
# plt.xscale('log')
# plt.show()