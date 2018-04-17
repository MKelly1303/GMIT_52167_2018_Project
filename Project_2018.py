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

 

#f, ((ax1, ax2, ax3, ax4)) = plt.subplots(1, 4, sharex='col', sharey='row')
#ax1.hist(sl)
#ax1.set_title('Sepal Length')
#ax2.hist(s)
#ax2.set_title('Sepal Width')
#ax3.hist(pl)
#ax3.set_title('Petal Length')
#ax4.hist(pw)
#ax4.set_title('Petal Width')
 
plt.scatter(sw,sl, color='red')
plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.show()

data['class']=data['class'].astype("category")
data["class"].cat.set_categories(["Iris-setosa","Iris-versicolor","Iris-virginica"],inplace=True)

df = pd.pivot_table(data,index=['class'], aggfunc='mean')
print("Mean Values for each class...")
print(df)

df2 = pd.pivot_table(data,index=['class'], aggfunc='min')
print("Min Values for each class...")
print(df2)

df3 = pd.pivot_table(data,index=['class'], aggfunc='max')
print("Max Values for each class...")
print(df3)