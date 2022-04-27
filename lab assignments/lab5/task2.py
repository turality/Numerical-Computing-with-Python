from math import *
import numpy as np
import matplotlib.pyplot as plt


f = lambda x: x*x - (np.exp(-2*x)-1)/x
x = np.linspace(-100,100,9000)
plt.plot(x,f(x))
plt.grid()


x0 = -10

x1 = 0.2
eps = 0.01

while True:
   x2 = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
   if abs(x2-x1)<eps:
      break
   if f(x2)==0:
      break
   x0 = x1
   x1 = x2
print(x2)
print(f(x2))
