from math import*
import numpy as np
import matplotlib.pyplot as plt
def divided_diff(x,y):
    n=len(x)
    coef=np.zeros([n,n])
    coef[:,0]=y
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j]=(coef[i+1][j-1]-coef[i][j-1])/(x[i+j]-x[i])
    return coef
x=np.array([1,2,3,5,7,8])
y=np.array([3,6,19,99,291,444])
b=divided_diff(x,y)[0,:]

def polynom(b,x,x_new):
    n=len(x)
    f=0
    for i in range(n):
        p=1
        for j in range(i):
            p*=(x_new-x[j])
        f+=b[i]*p
    return f

for i in range(len(x)):
    print(f'b{i}={b[i]}')

x_new=np.linspace(0,18,100)
y_new=polynom(b,x,x_new)
y1=polynom(b,x,8)
print(y1)
plt.scatter(x,y,label="data")
plt.plot(x_new,y_new,label="Polynom")
plt.plot(8,y1,"rs")
plt.grid()
f_4 = polynom(b,x,4)
print('f(4) = ', f_4)
plt.title("Newton Interpolation")
plt.show()
