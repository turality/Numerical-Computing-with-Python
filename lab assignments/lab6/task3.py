from numpy import array
from numpy import zeros
a = array([[4,2,-1],
           [5,3,-2],
           [3,2,-3]
])
b = array([1,2,0],float)
n = len(b)
x = zeros(n,float)
#forward
for k in range(n-1):
   for i in range(k+1,n):
      if a[i,k] == 0:
         continue
      factor = a[k,k]/a[i,k]
      for j in range(k,n):
         a[i,j] = a[k,j] - a[i,j]*factor
      b[i] = b[k] - b[i]*factor
print(a)
#backward
x[n-1] = b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
   sum_ax = 0
   for j in range(i+1,n):
      if a[i,j] == 0:
         continue
      else:
         sum_ax += a[i,j]*x[j]
   if a[i][i] == 0:
      continue
   else:
      x[i] = (b[i]-sum_ax)/a[i,i]
print("The solution of linear system is the following:")
print(x)
