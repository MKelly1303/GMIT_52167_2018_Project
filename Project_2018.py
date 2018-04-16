# Mark Kelly  - 2018/04/09

# Importing Test with iris data
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd


data = pd.read_csv("data/iris.csv", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

sl = data['sepal_length']
sw = data['sepal_width']
pl = data['petal_length']
pw = data['petal_width']
cl = data['class']

#print(data)
print('Mean Sepal Length = ', '{:01.2f}'.format(np.mean(sl)))
print('Max Sepal Length = ', '{:01.2f}'.format(np.max(sl)))
print('Min Sepal Length = ', '{:01.2f}'.format(np.min(sl)))

plt.figure(1)
plt.title('Sepal Length Histogram')
plt.xlabel('mm')
#plt.subplot(211)
plt.hist(sl)

#plt.subplot(212)
#plt.hist(sw)

#plt.subplot(213)
#plt.hist(pl)

#plt.subplot(214)
#plt.hist(pw)

plt.show()

