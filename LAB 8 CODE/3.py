import numpy as np
import matplotlib.pyplot as plt
x, y = np.loadtxt("3.txt", skiprows=1 , unpack=True)
def LineFit(x, y):
    xavg = x.mean()
    slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
    yint = y.mean()-slope*xavg
    N = len(y) 
    d_y = np.sqrt(((y-slope*x-yint)**2).sum()/(N-2))
    delta = N*(x**2).sum()-(x.sum())**2
    d_slope = d_y*np.sqrt(N/delta)
    d_yint = d_y*np.sqrt((x**2).sum()/delta) 
    return slope, yint, d_y, d_slope, d_yint

slope, yint, d_y, d_slope, d_yint = LineFit(x, y)

print("Slope: {} +/- {}".format(slope, d_slope))
print("Y-intercept: {} +/- {}".format(yint, d_yint))

x1 = np.array([x.min(), x.max()])
y1 = slope * x1 + yint

plt.figure(1, figsize = (8,6))
plt.scatter(x, y, color='b', s=10)
plt.plot(x1, y1, color='k', linewidth=2.0)

plt.axis([0,5,-1,15])

plt.xlabel('Time')
plt.ylabel('Angular Velocity')
plt.grid(True)
plt.text(0.1, 12.5, r'$y=A+Bx$', fontsize=12)
plt.text(0.1, 11.5, r'A:$%s\pm%s$'% (yint, d_yint), fontsize=12)
plt.text(0.1, 11, r'B:$%s\pm%s$'% (slope, d_slope), fontsize=12)
plt.title('Angular Velocity vs Time 3\n')

plt.savefig("Angular_Velocity_and_Time 3.png")
plt.show()


