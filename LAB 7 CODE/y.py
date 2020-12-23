import numpy as np
import matplotlib.pyplot as plt
y = np.loadtxt("y.txt", skiprows=1 , unpack=True)
avg_y = np.average(y)
print("The average y is: %6.3f" % avg_y)
std1_y = np.std(y)
print("The population standard deviation y is: %6.3f" % std1_y)
std2_y = np.std(y, ddof=1)
print("The sample standard deviation y is: %6.3f" % std2_y)
mean = std1_y
sd = std2_y
ratio = y
plt.figure(1, figsize = (10,8))      
plt.hist(ratio, bins=12, color='blue', edgecolor ='black')
plt.title('Histogram of y\'/y1')
plt.xlabel('y\'/y1')
plt.ylabel('counts')
plt.savefig('y.png')
plt.show()
ratio_one_sd = np.logical_and(ratio>=(mean-sd), ratio<=(mean+sd))
ratio_two_sd = np.logical_and(ratio>=(mean-2*sd), ratio<=(mean+2*sd))
fraction1 = len(ratio[~ratio_one_sd])/len(ratio)
fraction2 = len(ratio[~ratio_two_sd])/len(ratio)
print("The fraction of measurements outside the range average +/- ONE \
standard deviation is: {0:.2%}".format(fraction1))
print("The fraction of measurements outside the range average +/- TWO \
standard deviation is: {0:.2%}".format(fraction2))
