import numpy as np
from numpy import *

#1.Create a function which creates an n×n array with (i,j)-entry equal to i+j.
print("A1.")
def array(n):
	a = []
	for i in range(n):
	    a.append([])
	    for j in range(n):
	             a[i].append(i+j)
	print(a)

n=int(input("Enter size of 2d array:"))
array(n)

#2.Create a numpy array which contains odd numbers below 20. Arrange it to a 2x5 matrix. Compute the log of each element.
print("--------------")
print("--------------")
print("A2.")
y=np.arange(1,20,2)
x=reshape(y,(2,5))
print('2x5 array is:')
print(x)
print("--------------")
print("Log of each element:")
print(np.log(x))
print("--------------")	

print("--------------")

#3.Create a function which creates an n×n random array. Subtract the average of each row of the matrix 
print("A3.")
def randomfn(m):
	r=np.random.randint(5,size=(m,m))
	return r

m=int(input("Enter size of random array:"))
r=randomfn(m)
print(r)
z=r.mean(axis=1)
print(z)
for i in range(m):
	for j in range(m):
		r[i][j]=z[i]-r[i][j]
print("Averaged matrix:",r)
print("--------------")
print("--------------")


#4.Create a function which creates an n×n random array. Write a program to find the nearest value from a given value in the array.
print("A4.")
def find_nearest(array,value):
	idx = (np.abs(array-value)).argmin()
	print(idx)
	return array[idx]

m=int(input("Enter size of array to find nearest value:"))
array= np.random.randint(100,size=(m,m))
print(array)
array=array.flatten()
print(array)
value=int(input("Enter value:"))


print("Nearest value:",find_nearest(array, value))
print("--------------")
print("--------------")

#5.Write a function to check if two random arrays are equal or not. 

print("A5.")
def equal():
	f=1
	m=int(input("Enter size of 1st random array:"))
	a=randomfn(m)
	m=int(input("Enter size of 2nd random array:"))
	b=randomfn(m)
	e=np.array_equal(a,b)
	print("Array is equal?",e)
	print("--------------")
	print("--------------")
equal()

#6.Create a function to get the n largest values of an array.
print("A6.")
def largest():
	m=int(input("Enter size of array:"))
	x= np.random.randint(1,100,m)
	print("Original array:")
	print(x)
	n = 1
	print (x[np.argsort(x)[-n:]])
	print("--------------") 
largest()

	
