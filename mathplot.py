import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mpl_toolkits import mplot3d
from scipy.interpolate import interp2d

# def ln(x):
#     return math.log(x,math.e)
#
# x = np.linspace(0.001,100,1000000)
# y = []
# for v in x:
#     y.append((1/(math.sqrt(2*math.pi)*ln(2)))*math.exp(-((ln(v)-ln(0.01))**2/(2*ln(3)**2))))
#
# y = np.array(y)
#
#
#
# plt.plot(x,y)
# plt.xscale('log')
# plt.show()