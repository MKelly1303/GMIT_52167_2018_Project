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
	
groups=data[['class','sepal_length','sepal_width', 'petal_length', 'petal_width']].groupby('class')
	
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8),(ax9, ax10, ax11, ax12),(ax13, ax14, ax15, ax16)) = plt.subplots(4, 4, sharex='col', sharey='row')
 
#https://i.stack.imgur.com/R0qI4.jpg TRYING TO recreate this image.
for name, group in groups: 
    ax1.hist(group.sepal_length,label=name)
    ax2.scatter(group.sepal_width,group.sepal_length,label=name)
    ax3.scatter(group.petal_length,group.sepal_length,label=name)
    ax4.scatter(group.petal_width,group.sepal_length,label=name)

    ax5.scatter(group.sepal_length,group.sepal_width,label=name)
    ax6.hist(group.sepal_width,label=name)
    ax7.scatter(group.petal_length,group.sepal_width,label=name)
    ax8.scatter(group.petal_width,group.sepal_width,label=name)

    ax9.scatter(group.sepal_length,group.petal_length,label=name)
    ax10.scatter(group.sepal_width,group.petal_length,label=name)
    ax11.hist(group.sepal_width,label=name)
    ax12.scatter(group.petal_width,group.petal_length,label=name)

    ax13.scatter(group.sepal_length,group.petal_width,label=name)
    ax14.scatter(group.sepal_width,group.petal_width,label=name)
    ax15.scatter(group.petal_length,group.petal_width,label=name)
    ax16.hist(group.petal_width,label=name)
ax1.legend()
ax1.set_ylabel('Sepal Length(cm)')
ax5.set_ylabel('Sepal Width(cm)')
ax9.set_ylabel('Petal Length(cm)')
ax13.set_ylabel('Petal Width(cm)')
ax13.set_xlabel('Sepal Length(cm)')
ax14.set_xlabel('Sepal Width(cm)')
ax15.set_xlabel('Petal Length(cm)')
ax16.set_xlabel('Petal Width(cm)')
ax6.legend()
ax11.legend()
ax16.legend()
#ax5.legend()
#ax6.legend()
#ax7.legend()
#ax8.legend()

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
