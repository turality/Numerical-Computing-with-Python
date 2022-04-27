import matplotlib.pyplot as plt
import numpy as np
#1)Graphically
'''
f = lambda x: 4*(x**3) -6*(x**2) + 7*x -2.3
x = np.linspace(-100,100,10000)
y = f(x)
plt.plot(x,y)
plt.grid()
plt.show()
'''
#2)bisection
a = 0
b = 1
eps = 10
f = lambda x: 4*x**3 -6*x**2 + 7*x -2.3

def bisection(f,a,b,eps):
   if f(a)*f(b)>0:
      print("bisection method failed to find a solution!")
      return None
   c = (a+b)/2
   last = f(c)
   prev = f(c)
   while True:
      c = (a+b)/2
      last = f(c)
      if abs(prev-last)/last<eps:
         break
      if f(c) == 0:
         return c
      if f(a)*f(c)<0:
         c = b
      if f(b)*f(c)<0:
         c = a
   return (a+b)/2
x = np.linspace(-1000,1000,1000000)

c = bisection(f,a,b,10)
print(f"{(c)}\n{(f(c))}")

#3)Checking

print(c,f(c))  










