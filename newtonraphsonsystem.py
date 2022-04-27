from math import *
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
#1

f1 = lambda x,y: sin(x+1)-y -1.2
f2 = lambda x,y: 2*x +cos(y) - 2
f1x = lambda x,y: cos(x+1)
f1y = lambda x,y: -1
f2x = lambda x,y: 2
f2y = lambda x,y: -sin(y)

eps = 0.0001
x0 = 2
y0 = 2
x = np.linspace(-5,5,200)
y = np.sin(x+1)-1.2

plt.plot(x,y,label = "Equation")
plt.grid()

y =  np.linspace(-5,5,200)
x = (2-np.cos(y))/2

plt.plot(x,y,label = "Equation 2")
plt.legend()


count = 0
while count<100:
   X0 = np.array([[x0],[y0]])
   F = np.array([[f1(x0,y0)],[f2(x0,y0)]])
   DF = np.array([[f1x(x0,y0),f1y(x0,y0)],[f2x(x0,y0),f2y(x0,y0)]])
   X = X0 - inv(DF).dot(F)
   count += 1
   if abs(X[0]-X0[0])<=0.0001 and abs(X[1]-X0[1])<=0.0001:
      break
   x0= X[0][0]
   y0= X[1][0]
plt.plot(X[0][0],X[1][0],"rp",label = "Root")
print(f"x = {X[0][0]},y = {X[1][0]}")
print(f"Equation 1: {f1(X[0][0],X[1][0])}")
plt.show()
'''
#2
'''
f1 = lambda x,y: cos(x-1) + y - 0.5
f2 = lambda x,y: x - cos(y) - 3
f1x = lambda x,y: -sin(x-1)
f1y = lambda x,y: 1
f2x = lambda x,y: 1
f2y = lambda x,y: sin(y)

eps = 0.0001
x0 = 2
y0 = 2

x = np.linspace(-5,5,200)
y = 0.5 - np.cos(x-1)

plt.plot(x,y,label = "Equation 1")
plt.grid()

y = np.linspace(-5,5,200)
x = 3+np.cos(y)

plt.plot(x,y,label = "Equation 2")
plt.legend()
count = 0
while count < 100:
   X0 = np.array([[x0],[y0]])
   F = np.array([[f1(x0,y0)],[f2(x0,y0)]])
   DF = np.array([[f1x(x0,y0), f1y(x0,y0)], [f2x(x0,y0), f2y(x0,y0)]])
   X = X0 - inv(DF).dot(F)
   count += 1
   if abs(X[0]-X0[0])<=eps and abs(X[1]-X0[1])<=eps:
      break
   x0 = X[0][0]
   y0 = X[1][0]
plt.plot(X[0][0],X[1][0],"rp",label = "Root")
print(f"x = {X[0][0]},y = {X[1][0]}")
print(f"Equation 1: {f1(X[0][0],X[1][0])}")
plt.show()
