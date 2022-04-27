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

x=np.array([0,1,2,3,4,5])
y=np.array([0,0.5,0.8,0.9,0.941176,0.961538])

x_new=np.linspace(-10,15,400)
y_new=Lagrange_polynom(x,y,x_new)
y1=Lagrange_polynom(x,y,0.85)
print(y1)
plt.plot(0.85,y1,"rs")
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.grid()
plt.show()
