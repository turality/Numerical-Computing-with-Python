from numpy import *
d = [10,20,30,40,50]
c = [1,2,3,4]
a = [5,6,7,8]
b = [1,0.5,1,2]
n= len(b)
x= zeros(n)

for i in range(1,n):
    d[i]=d[i]-(a[i-1]*c[i-1])/d[i-1]
    b[i] = b[i] - a[i-1]*b[i-1]/d[i-1]
x[n-1] = b[n-1]/d[n-1]
for i in range(n-2,-1,-1):
    x[i] = (b[i]-c[i]*x[i+1])/d[i]
print(x)

