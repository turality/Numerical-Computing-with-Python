from math import *
import numpy as np
import matplotlib.pyplot as plt

def secant(f, x0, x1, eps):
    while True:
        x2=x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
        if abs(x2-x1)<eps:
            return x2
        if f(x2)==0:
            return x2
        x0=x1
        x1=x2

f=lambda x: x*cos(x/(x-2))
x=np.linspace(-1, 1, 200)
y=x*np.cos(x/(x-2))
plt.plot(x, y, label="Original function")


x0=-1
x1=1
eps=0.000001

x2=secant(f, x0, x1, eps)
plt.plot(x2, f(x2), label="Root", marker="o", markersize=5)
print("Root: ", x2)
print("Value of function: ", f(x2))

plt.grid()
plt.legend()
plt.show()
