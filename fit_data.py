import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

filename = "example_data.csv"
data = np.loadtxt(filename, delimiter=",", skiprows=1)
plt.plot(data[:,0], data[:,1], "ro")

def model(x, p1, p2):
   return p1 * np.cos(p2 *x) + p2 * np.sin(p1 * x)

popt, pcov = curve_fit(model, data[:,0], data[:,1], p0=(1, 0.2))

x = np.linspace(-2, 2.9, 100)
plt.plot(x, model(x, *popt))

plt.show()



