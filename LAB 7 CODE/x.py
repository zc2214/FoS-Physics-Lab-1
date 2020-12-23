import numpy as np
import matplotlib.pyplot as plt
x = np.loadtxt("x.txt", skiprows=1 , unpack=True)
avg_x = np.average(x)
print("The average x is: %6.3f" % avg_x)
std1_x = np.std(x)
print("The population standard deviation x is: %6.3f" % std1_x)
std2_x = np.std(x, ddof=1)
print("The sample standard deviation x is: %6.3f" % std2_x)
mean = std1_x
sd = std2_x
ratio = x
plt.figure(1, figsize = (10,8))      
plt.hist(ratio, bins=9, color='blue', edgecolor ='black')
plt.title('Histogram of x\'/x1')
plt.xlabel('x\'/x1')
plt.ylabel('counts')
plt.savefig('x.png')
plt.show()
ratio_one_sd = np.logical_and(ratio>=(mean-sd), ratio<=(mean+sd))
ratio_two_sd = np.logical_and(ratio>=(mean-2*sd), ratio<=(mean+2*sd))
fraction1 = len(ratio[~ratio_one_sd])/len(ratio)
fraction2 = len(ratio[~ratio_two_sd])/len(ratio)
print("The fraction of measurements outside the range average +/- ONE \
standard deviation is: {0:.2%}".format(fraction1))
print("The fraction of measurements outside the range average +/- TWO \
standard deviation is: {0:.2%}".format(fraction2))
