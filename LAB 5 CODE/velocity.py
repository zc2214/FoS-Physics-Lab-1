import numpy as np
import matplotlib.pyplot as plt
v = np.loadtxt("velocity.txt", skiprows=1 , unpack=True)
avg_v = np.average(v)
print("The average velocity is: %6.3f" % avg_v)
std1_v = np.std(v)
print("The population standard deviation velocity is: %6.3f" % std1_v)
std2_v = np.std(v, ddof=1)
print("The sample standard deviation velocity is: %6.3f" % std2_v)
mean = std1_v
sd = std2_v
ratio = np.random.normal(mean, sd, 1000)
plt.figure(1, figsize = (10,8))      
plt.hist(ratio, bins=25, color='blue', edgecolor ='black')
plt.title('Histogram of v\'/v1')
plt.xlabel('v\'/v1')
plt.ylabel('counts')
plt.savefig('velocity.png')
plt.show()
ratio_one_sd = np.logical_and(ratio>=(mean-sd), ratio<=(mean+sd))
ratio_two_sd = np.logical_and(ratio>=(mean-2*sd), ratio<=(mean+2*sd))
fraction1 = len(ratio[~ratio_one_sd])/len(ratio)
fraction2 = len(ratio[~ratio_two_sd])/len(ratio)
print("The fraction of measurements outside the range average +/- ONE \
standard deviation is: {0:.2%}".format(fraction1))
print("The fraction of measurements outside the range average +/- TWO \
standard deviation is: {0:.2%}".format(fraction2))
