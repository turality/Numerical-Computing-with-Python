from numpy import *

d = [1,4,3,3]

c = [4,1,4,0]

a = [3,2,1,0]

b = [1,1,1,1]
n = len(b)
x = zeros(n,float)
for i in range(1,n-1):
   d[i] = d[i]-(a[i-1]*c[i-1])/d[i-1]
   b[i] = b[i] - (a[i-1]*c[i-1])/d[i-1]
x[n-1] = b[n-1]/d[n-1]
for i in range(n-2,-1,-1):
   x[i] = (b[i]-c[i]*x[i+1])/d[i]
print(x)
