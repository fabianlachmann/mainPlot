import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d


def Gong(r):
    return 1.373*10**3.41*r**-(4.7*(1+30*r)**(-0.017*r**(-1.44)))*(1+0.057*r**(3.45))*10**(1.607*math.exp(-1*(1-(math.log10(r)/0.433))**2))*(0.3+1-0.76+0.21)

def Schwarz(r):
    return (800*((10**2.5)/(r**2.5)))

def Andreas(r):
    return r*1.2*(10**3)*(math.exp(5.2 -1.14*r))


y1 = []
y2  = []
y3 = []
x1 = np.linspace(0.07,20,1000000)
x2 =  np.linspace(3,25,1000000)
x3 =  np.linspace(0.25,7,1000000)
for r in x1:
    y1.append(Gong(r))

for r in x2:
    y2.append(Schwarz(r))

for r in x3:
    y3.append(Andreas(r))

y1 = np.array(y1)
y2 = np.array(y2)
y2 = np.array(y2)

plt.plot(x1,y1,'r',label = 'Gong et al. 2003')
plt.plot(x2,y2,'g',label = 'Lewis and Schwartz 2004')
plt.plot(x3,y3,'c',label = 'Andreas 2007')

plt.xticks([0.01,0.1,1,10])
plt.yscale('log')
plt.ylabel('$dF/d\log(r_{80})$',fontsize = 'x-large')
plt.xscale('log')
plt.xlabel('Radius ($r_{80}$)',fontsize = 'x-large')
plt.title('Plot der Fluxformulierungen',fontsize = 'xx-large')
plt.legend(loc = 'lower left')
plt.show()








# for v in x:
#     y.append(4*math.pi*v**2*(200*f(v,1.5,0.07)+50*f(v,3.5,0.15)))
#     y1.append(4*math.pi*v**2*(200*f(v,1.5,0.07)))
#     y2.append(4*math.pi*v**2*(50*f(v,3.5,0.15)))
#
# a2.plot(x,y1,'r--')
# a2.plot(x,y2,'y--')
# a2.plot(x,y,'b')
# a2.set_title('Flächenverteilung',fontsize = 'xx-large')
# a2.set_ylabel('$dS/d\ln{D}$',fontsize = 'xx-large')
#
# a2.set_xlabel('Durchmesser',fontsize = 'xx-large')
# a2.set_xscale('log')
#
#
# y = []
# y1=[]
# y2=[]
# for v in x:
#     y.append(4/3*math.pi*v**3*(200*f(v,1.5,0.07)+50*f(v,3.5,0.15)))
#     y1.append(4/3*math.pi*v**3*(200*f(v,1.5,0.07)))
#     y2.append(4/3*math.pi*v**3*(50*f(v,3.5,0.15)))
#
#
# a3.plot(x,y1,'r--')
# a3.plot(x,y2,'y--')
# a3.plot(x,y,'b')
# a3.set_title('Volumenverteilung',fontsize = 'xx-large')
# a3.set_ylabel('$dV/d\ln{D}$',fontsize = 'xx-large')
# a3.set_xlabel('Durchmesser',fontsize = 'xx-large')
# a3.set_xscale('log')
#
# fig.legend()
# plt.show()

# plt.plot(x,y)
# plt.xscale('log')
# plt.show()