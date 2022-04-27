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

x=np.array([1,2,3,4,5,6,7])
y=np.array([1,0.5,0.3333,0.25,0.2,0.1667,0.1429])
x_new=np.linspace(-10,15,400)
y_new=Lagrange_polynom(x,y,x_new)

plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.grid()
plt.show()
