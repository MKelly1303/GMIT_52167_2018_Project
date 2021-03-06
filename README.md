# GMIT_52167_2018_Project
Problem statement
The following project concerns the well-known Fisher’s Iris data set [3]. The project
entails you researching the data set, and then writing documentation and code in the
Python programming language [1] based on that research.
An online search for information on the data set will convince you that many people
have investigated and written about it previously, and many of those are not experienced
programmers. You are expected to be able to break this project into several smaller tasks
that are easier to solve, and to plug these together after they have been completed. You
might do that for this project as follows:
1. Research background information about the data set and write a summary about it.
2. Keep a list of references you used in completing the project.
3. Download the data set and write some Python code to investigate it.
4. Summarise the data set by, for example, calculating the maximum, minimum and
mean of each column of the data set. A Python script will quickly do this for you.
5. Write a summary of your investigations.
6. Include supporting tables and graphics as you deem necessary.
-----------------------------------------------------------------------------------------------------------------------------

Fisher's Iris Data Set - Mark Kelly - 2018 - GMIT - Programming and Scripting 52167

In a 1936 paper titled 'The use of multiple measurements in taxonomic problems' biologist and 
statistician Ronald Fisher introduced the Iris flower data set. This is an example of a 
multivariate data set and has been used extensively in the field of data analytics. It is often 
used in testing machine learning algorithm and visualisation. 

This data set composes of three variants of iris flowers (setosa, veriscolor and virginica). There 
are 50 samples of each flower totalling 150 entries in the entire data set. There are four data 
entries in this set that gives us the measurements of the flowers in centimetres of sepal width, 
sepal length, petal width and petal length.
[High level information taken from https://en.wikipedia.org/wiki/Iris_flower_data_set]


Figure 1 table gives us the Mean, Min, Max and Sum of all fields in the data set.   

![alt text](https://github.com/MKelly1303/GMIT_52167_2018_Project/blob/master/Fig2.JPG)

Fig 1

The interesting thing about this table is that the sepal length is on average the largest of 
the datasets while the petal width is the smallest. Petal length has the largest variations within 
it's data while the sepal width has the smallest.

Using the panda's pivot table functionality, the Mean, Min, Max and Sum values for each of the three 
flower types were generated. These are seen in figures 2, 3, 4 and 5.

![alt text](https://github.com/MKelly1303/GMIT_52167_2018_Project/blob/master/Fig3.JPG)

Fig 2


![alt text](https://github.com/MKelly1303/GMIT_52167_2018_Project/blob/master/Fig4.JPG)

Fig 3


![alt text](https://github.com/MKelly1303/GMIT_52167_2018_Project/blob/master/Fig5.JPG)

Fig 4

![alt text](https://github.com/MKelly1303/GMIT_52167_2018_Project/blob/master/Fig6.JPG)

Fig 5

A histogram has been generated for each attribute giving a different colour for each flower type. 
Scatter plots have also been created comparing the 4 different attributes against each other.
Again, each flower type has its own colour. These charts are generated into a single plot and is 
seen in figure 6.

![alt text](https://github.com/MKelly1303/GMIT_52167_2018_Project/blob/master/Fig1.JPG)
Fig 6

The pivot tables and the plots through up some interesting observations. The most obvious point is that 
the flower type setosa is very different from the other two. Setosa has a smaller petal width and petal 
length. It has the smallest variation of any of the attributes for all classes and makes it clearly 
identifiable just from the petal size. Versicolor and Viginica are closer in petal size with Virginica 
on average being larger for both length and width. It is also noticed that petal length has the largest 
variation of all the attributes.

Sepal sizes are much closer between the 3 classes. This makes it harder to clearly define each class 
based on sepal sizes but its still possible to identify some trends. Setosa, in general, has largest 
sepal width with one outlier that has a width of approx 2.4cm. Setosa however also has the smallest sepal 
length. Virginica has the largest variation in sepal length while versicolor has in general the smallest 
sepal width.

In general, the Fisher Iris dataset is an excellent dataset to start in data analytics. The dataset size is
very manageable with only 150 entries and only 5 data columns. The variations in the attributes can lead to 
some interesting observations and insights and is very useful in cluster analysis and generating scatter plots.

