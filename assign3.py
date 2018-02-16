import numpy as np
from numpy import *
#1.
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

#2.
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

#3.
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


#4.
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

#5.
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

#6.
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

	
