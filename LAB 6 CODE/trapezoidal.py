import numpy as np
import matplotlib.pyplot as plt
x, y = np.loadtxt("force position.txt", skiprows=1 , unpack=True)
s = np.trapz(x,y)
print('The integral of the data using trapezoidal rule is:', s)

