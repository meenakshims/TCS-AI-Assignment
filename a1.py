import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. Using Pandas, load the dataset from https://www.kaggle.com/uciml/iris/data to a variable name iris
iris=pd.read_csv("Iris.csv")

#2.Create a list named headers with all the column header names in the given order.
header=["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"] 

#3.Using the slice operation on headers, extract the column names with index 1 to 4 onto a list called features.

features=header[1:5] 

#4.Display the first five records of iris
print(iris.head(5))
print('------------')



#5.Make a scatterplot of the Iris features.
#colors={'Iris-virginica':'#1b9e77', 'Iris-setosa':'#d95f02', 'Iris-versicolor':'#7570b3'}
plt.scatter(iris.SepalWidthCm,iris.SepalLengthCm)
plt.xlabel("SepalWidth(Cm)")
plt.ylabel("SepalLength(cm)")
plt.show()


plt.scatter(iris.PetalWidthCm,iris.PetalLengthCm)
plt.xlabel("PetalWidth(Cm)")
plt.ylabel("PetalLength(Cm)")
plt.show()


#6.What is the range of ‘SepalLengthCm’ in the dataset? What is the second largest value of ‘SepalLengthCm’ in the dataset?
sepallength=np.array(iris.SepalLengthCm)
max1=iris["SepalLengthCm"].max()
print("Range of SepalLengthCm:",iris["SepalLengthCm"].max()-iris["SepalLengthCm"].min()) 

sort=sorted(sepallength)
for i in reversed(sort):
	if i!=max1:
		print("Second Largest:",i)
		break
print('------------')

#7.Find the mean of all the values in SepalWidthCm using numpy
sepalwidth=np.array(iris.SepalWidthCm)
print("Mean of SepalWidthCm:",np.mean(sepalwidth)) 
print('------------')

#8. Identify  ‘SepalLengthCm’  values less than 5. Create a new column named ‘Length’ , categorise each entry as ‘Small’ or ‘Large’, if less than 5.
l=[]
for i in sepallength:
	if i<5.0:
		l.append('small')
	else: 
		l.append('large')
iris['length']=l
print(iris)
print('------------')

#9. Group dataFrame by the "Species" column. Make a histogram of the same.
plt.hist(iris['Species'])
plt.ylabel("Frequency")
plt.xlabel("Species")
plt.show()

#10.Find the deviation of length for ‘SepalLengthCm’ from the average
print("Deviation:",np.std(sepallength)) 

#11.Find correlation between columns and display columns with more than 70% percent correlation (either positive or negative).

c=iris.drop(['Id','Species'], axis=1).corr()
print(c)
col = []

for i in features:
    for j in features:
        if (abs(c[i][j]) > 0.7) and (i != j):
            col.append(i)
print("Columns with >70%")
print(np.unique(col))


#12.Impute missing values if present using mean of the dataset.
for i in range(len(features)):
	iris[features[i]].fillna((iris[features[i]].mean()), inplace=True)

#13.Save the current dataFrame out to a new csv file.
iris.to_csv('new_iris.csv',index=False)





