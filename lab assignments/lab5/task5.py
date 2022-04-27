from math import *
import numpy as np
import matplotlib.pyplot as plt
f = lambda x: np.tan(x)-x-1
x = (-50,50,2000)
plt.plot(x,f(x))
plt.grid()
x0 = 0
x1 = 1
x2 = 0
eps = 0.0000001
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
plt.plot(x2,f(x2),"rs")
plt.show()
