from numpy import *
a = array([[2,5,4,1],
           [1,3,2,1],
           [2,8,9,7],
           [3,8,9,2]])
b = array([20,11,40,37])

n = len(b)

x= zeros(n)

for k in range(n-1):
   for i in range(k,n):
      factor = a[i][k]/a[k][k]
      for j in range
      
