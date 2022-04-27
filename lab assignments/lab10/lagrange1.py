import numpy as np
import matplotlib.pyplot as plt
def Lagrange_polynom(x,y,x_new):
    n=len(x)
    f=0
    for i in range(n):
        cardinals=1
        for j in range(n):
            if i==j:
                continue
            cardinals*=(x_new-x[j])/(x[i]-x[j])
        f+=y[i]*cardinals
    return f

x=np.array([1,4,6])
y=np.array([0,1.386294,1.791760])

x_new=np.linspace(-10,10,200)
y_new=Lagrange_polynom(x,y,x_new)
y1=Lagrange_polynom(x,y,2)
print(y1)
plt.plot(2,y1,"rs")
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.grid()
plt.show()
