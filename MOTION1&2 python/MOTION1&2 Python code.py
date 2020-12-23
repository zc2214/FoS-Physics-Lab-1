import numpy as np
import matplotlib.pyplot as plt
time, position, uncertainty_x = np.loadtxt("position.txt", skiprows=4 , unpack=True)
t1 = time[0]
t2 = time[1]
dt = t2 - t1
x1 = position[:-2]
x2 = position[2:]
velocity = (x2-x1)/(2*dt)
x1 = position[:-2]
x2 = position[1:-1]
x3 = position[2:]
acceleration = (x3-2*x2+x1)/dt**2
uncertainty_v = (uncertainty_x[2:]+uncertainty_x[:-2])/(2*dt)
uncertainty_a = (uncertainty_x[2:]+2*uncertainty_x[1:-1]+uncertainty_x[:-2])/dt**2
plt.figure(1, figsize = (10,8))
plt.subplot(3,1,1)
plt.plot(time, position)
plt.errorbar(time, position, fmt='yx', label="data",xerr=0, yerr=uncertainty_x, ecolor='red',capsize=1)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.subplot(3,1,2)
plt.plot(time[1:-1], velocity)
plt.errorbar(time[1:-1], velocity, fmt='yx', label="data",xerr=0, yerr=uncertainty_v, ecolor='red',capsize=1)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.subplot(3,1,3)
plt.plot(time[1:-1], acceleration)
plt.errorbar(time[1:-1], acceleration, fmt='yx', label="data",xerr=0, yerr=uncertainty_a, ecolor='red',capsize=1)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.subplots_adjust(hspace=0.5)
plt.savefig('MOTION1&2.png')
print('***FINISHED***')
