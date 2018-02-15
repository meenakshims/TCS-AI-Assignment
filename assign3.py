import numpy as np
from numpy import *
#1.
def array(n):
	a = []
	for i in range(n):
	    a.append([])
	    for j in range(n):
	             a[i].append(i+j)
	print(a)

n=int(input("Enter size of 2d array"))
array(n)

#2.
y=np.array([1,3,5,7,9,11,13,15,17,19])
x=reshape(y,(2,5))
print('2x5 array is:',x)

#3.
def randomfn(m):
	r=np.random.randint(5,size=(m,m))
	return r

m=int(input("Enter size of random array"))
r=randomfn(m)
print(r)

#5.
def equal():
	f=1
	m=int(input("Enter size of 1st random array"))
	a=randomfn(m)
	m=int(input("Enter size of 2nd random array"))
	b=randomfn(m)
	e=np.equal(a,b)
	print("Array is equal?",e)

equal()

	
