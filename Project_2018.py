# Importing Test with iris data
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

#with open("data/iris.csv") as f:
#  for line in f:
  #  str0 = (line.split (',')[0])
 #   str1 = (line.split (',')[1])
  #  str2 = (line.split (',')[2])
   # str3 = (line.split (',')[3])
   # print('{0:>3} {1:>3} {2:>3} {3:>3}'.format(str0, str1, str2, str3))

#data = np.genfromtxt("data/iris.csv", delimiter=",")
data = pd.read_csv("data/iris.csv")

print(data)
#plt.plot(data[1])
#plt.plot(y, 'r+', markersize=20)
#plt.show()
