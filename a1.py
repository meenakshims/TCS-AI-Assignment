import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


iris=pd.read_csv("Iris.csv") #1.

header=["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"] #2.

features=header[1:5] #3.

print(iris.head(5)) #4.



#5.
#colors={'Iris-virginica':'#1b9e77', 'Iris-setosa':'#d95f02', 'Iris-versicolor':'#7570b3'}
plt.scatter(iris.SepalWidthCm,iris.SepalLengthCm)
plt.xlabel("SepalWidth(Cm)")
plt.ylabel("SepalLength(cm)")
plt.show()


plt.scatter(iris.PetalWidthCm,iris.PetalLengthCm)
plt.xlabel("PetalWidth(Cm)")
plt.ylabel("PetalLength(Cm)")
plt.show()


#6.
sepallength=np.array(iris.SepalLengthCm)
max1=iris["SepalLengthCm"].max()
print("Range of SepalLengthCm:",iris["SepalLengthCm"].max()-iris["SepalLengthCm"].min()) 

sort=sorted(sepallength)
for i in reversed(sort):
	if i!=max1:
		print("Second Largest:",i)
		break

sepalwidth=np.array(iris.SepalWidthCm)
print("Mean of SepalWidthCm:",np.mean(sepalwidth)) #7.

#8.
l=[]
for i in sepallength:
	if i<5.0:
		l.append('small')
	else: 
		l.append('large')
iris['length']=l
print(iris)

#9.
#g=iris.groupby('Species')
#plt.hist(g,bins=20)
#plt.show()

#10.
print("Deviation:",np.std(sepallength)) 

c=iris.drop(['Id','Species'], axis=1).corr()
print(c)
col = []

for i in features:
    for j in features:
        if (abs(c[i][j]) > 0.7) and (i != j):
            col.append(i)
print("Columns with >70%")
print(np.unique(col))


#12.
print(iris.isnull())

#13.
iris.to_csv('new_iris.csv',index=False)





