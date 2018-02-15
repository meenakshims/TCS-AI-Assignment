import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


iris=pd.read_csv("Iris.csv") #1.

header=["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"] #2.

features=header[1:5] #3.

print(iris.head(5)) #4.



#5.
colors={'Iris-virginica':'#1b9e77', 'Iris-setosa':'#d95f02', 'Iris-versicolor':'#7570b3'}
plt.scatter(iris.SepalWidthCm,iris.SepalLengthCm,color=colors)
plt.xlabel("SepalWidth(Cm)")
plt.ylabel("SepalLength(cm)")
plt.show()


plt.scatter(iris.PetalWidthCm,iris.PetalLengthCm)
plt.xlabel("PetalWidth(Cm)")
plt.ylabel("PetalLength(Cm)")
plt.show()



sepallength=np.array(iris.SepalLengthCm)
max1=iris["SepalLengthCm"].max()
print("Range of SepalLengthCm:",iris["SepalLengthCm"].max()-iris["SepalLengthCm"].min()) #6.

sort=sorted(sepallength)
for i in reversed(sort):
	if i!=max1:
		print("Second Largest:",i)
		break

sepalwidth=np.array(iris.SepalWidthCm)
print("Mean of SepalWidthCm:",np.mean(sepalwidth)) #7.

for i in sepallength:
	if i<5.0:
		l.append['small']
	else: 
		l.append['large']

#for index,SepalLengthCm in iris.iteritems():
#	if iris.loc['SepalLengthCm'] <5:
#		iris["Length"]='Small'
#	else:
#		iris["Length"]='Large'
print(iris)

g=iris.groupby('Species')

plt.hist(g) #9.
plt.show()

#sepallength=np.array(iris.SepalLengthCm)
print("Deviation:",np.std(sepallength)) #10.

c=iris.drop(['Id','Species'], axis=1).corr()
print(c)
#for i in range(len(c.columns)):
 #       for j in range(i):
  #          if c.iloc[i, j] >= 0.7:
   #             colname = c.columns[i]
	#	print("name",colname)







