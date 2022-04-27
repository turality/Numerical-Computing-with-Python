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

x=np.array([1,3,5,7,13])
y=np.array([800,2310,3090,3940,4755])

x_new=np.linspace(-10,15,400)
y_new=Lagrange_polynom(x,y,x_new)
y1=Lagrange_polynom(x,y,10)
print(y1)
plt.plot(10,y1,"rs")
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.grid()
plt.show()
