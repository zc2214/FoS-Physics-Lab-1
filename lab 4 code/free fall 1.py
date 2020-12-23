print('1 is for 10cm, 2 is for 20cm, 3 is for 30cm')
import numpy as np
E1, E2, E3 = np.loadtxt("free fall 1.txt", skiprows=1 , unpack=True)
avg_E1 = np.average(E1)
print("The average delta E of 1 is: %6.3f" % avg_E1)
avg_E2 = np.average(E2)
print("The average delta E of 2 is: %6.3f" % avg_E2)
avg_E3 = np.average(E3)
print("The average delta E of 3 is: %6.3f" % avg_E3)
deltad=0.00003
D=0.031150
deltah=0.00025
Delta1=2*deltad/D
Delta=np.sqrt(deltah**2 + Delta1**2)      
Deltae1=avg_E1*Delta
Deltae2=avg_E2*Delta
Deltae3=avg_E3*Delta
print ('uncertainty in delta E1=uncertainty in V1=%6.3f' % Deltae1)
print ('uncertainty in delta E2=uncertainty in V2=%6.3f' % Deltae2)
print ('uncertainty in delta E3=uncertainty in V3=%6.3f' % Deltae3)
std1_E1 = np.std(E1)
print("The population standard deviation of data set 1 is: %6.3f" % std1_E1)
std1_E2 = np.std(E2)
print("The population standard deviation of data set 2 is: %6.3f" % std1_E2)
std1_E3 = np.std(E3)
print("The population standard deviation of data set 3 is: %6.3f" % std1_E3)
std2_E1 = np.std(E1, ddof=1)
print("The sample standard deviation of data set 1 is: %6.3f" % std2_E1)
std2_E2 = np.std(E2, ddof=1)
print("The sample standard deviation of data set 2 is: %6.3f" % std2_E2)
std2_E3 = np.std(E3, ddof=1)
print("The sample standard deviation of data set 3 is: %6.3f" % std2_E3)
N1 = len(E1)
sdom_E1 = std2_E1/np.sqrt(N1)
print("The standard deviation of the mean 1 is: %6.3f" % sdom_E1)
N2 = len(E2)
sdom_E2 = std2_E2/np.sqrt(N2)
print("The standard deviation of the mean 2 is: %6.3f" % sdom_E2)
N3 = len(E3)
sdom_E3 = std2_E3/np.sqrt(N3)
print("The standard deviation of the mean 3 is: %6.3f" % sdom_E3)
fusd = 1/(np.sqrt(2*(N1-1)))
print("The fractional uncertainty in standard deviation is: %6.3f" % fusd)
