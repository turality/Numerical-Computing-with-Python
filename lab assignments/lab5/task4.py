from math import *
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(x)-3*x**2
x = np.linspace(-10,10,2000)
plt.plot(x,f(x))
plt.grid()
x0 = -2.5
x1 = 1
x2 = 0
eps = 0.00001
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
