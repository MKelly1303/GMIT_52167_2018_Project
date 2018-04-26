# Mark Kelly - 26/04/2018 - GMIT - 52167 - Final Project


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("data/iris.csv", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
#Importing the data set into an array called data and naming each column.

sl = data['sepal_length']
sw = data['sepal_width']
pl = data['petal_length']
pw = data['petal_width']
cl = data['class']
# creating a shortnamed variable for each data column.

# Print headings for each data type.
print('        Sepal Length   Sepal Width      Petal Length       Petal Width')
# Print headings for each data type.

print('Mean  =   ', '{:01.2f}'.format(np.mean(sl)),'          ', '{:01.2f}'.format(np.mean(sw)), '            ', '{:01.2f}'.format(np.mean(pl)),'            ', '{:01.2f}'.format(np.mean(pw)))
# generating and printing the mean value for each data column and formatting it to 2 decimal places.

print('Min   =   ', '{:01.2f}'.format(np.min(sl)),'          ', '{:01.2f}'.format(np.min(sw)), '            ', '{:01.2f}'.format(np.min(pl)),'            ', '{:01.2f}'.format(np.min(pw)))
# generating and printing the min value for each data column and formatting it to 2 decimal places.

print('Max   =   ', '{:01.2f}'.format(np.max(sl)),'          ', '{:01.2f}'.format(np.max(sw)), '            ', '{:01.2f}'.format(np.max(pl)),'            ', '{:01.2f}'.format(np.max(pw)))
# generating and printing the max value for each data column and formatting it to 2 decimal places.
	
print('Sum   =  ', '{:01.1f}'.format(np.sum(sl)),'         ', '{:01.1f}'.format(np.sum(sw)), '           ', '{:01.1f}'.format(np.sum(pl)),'           ', '{:01.1f}'.format(np.sum(pw)))
# generating and printing the sum value for each data column and formatting it to 1 decimal places.


print("Mean Values for each class...")
print(pd.pivot_table(data, index=['class'], aggfunc='mean'))
print(" ")
print("Min Values for each class...")
print(pd.pivot_table(data, index=['class'], aggfunc='min'))
print(" ")
print("Max Values for each class...")
print(pd.pivot_table(data, index=['class'], aggfunc='max'))
print(" ")
print("Sum Values for each class...")
print(pd.pivot_table(data, index=['class'], aggfunc='sum'))
	

groups=data[['class','sepal_length','sepal_width', 'petal_length', 'petal_width']].groupby('class')
#Creating a group that is differeniated and grouped on the different values of 'class'

fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8),(ax9, ax10, ax11, ax12),(ax13, ax14, ax15, ax16)) = plt.subplots(4, 4, sharex='none', sharey='none')
# Creating a 4 x 4 subplot matix with plots names ax1 to ax16 where each row and column will not share the axis'.      
 
#https://stackoverflow.com/questions/42592493/displaying-pair-plot-in-pandas-data-frame/45195783 Trying to recreate the images seen on this page as I felt it shows a good visual representation of the differences between the classes.


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
# Using a for loop to generate each plot where they will be grouped by the value in class. For each data column, there will be be a histogram generated along with a scatterplot against all other data type. They will be coloured differently depending on the value of class. As there are 3 flower types in our class column, there will be 3 colours each depicting the different flower types.

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
# Setting the legend to appear on each histogram. Labels will only be generated once for each row and column on the left of the charts and at the bottom.

plt.show()
# Plot the chart
