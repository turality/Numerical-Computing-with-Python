
#1)Graphically
'''
import matplotlib.pyplot as plt
import numpy as np
def bisection(f,a,b,N):
   if f(a)*f(b)>0:
      print("bisection method fails to find the solution")
      return None
   for i in range(N):
      c = (a+b)/2
      if f(c) == 0:
         print("exact solution has been found!")
         return c
      if f(a)*f(c) < 0:
         b = c
      elif f(b)*f(c)<0:
         a = c
      else:
         print("bisection method fails to find a solution")
   return (a+b)/2

x = np.linspace(-100,100,10000)
a = 5
b = 10
f = lambda x: -0.6 * x**2 + 2.4 * x + 5.5
c = bisection(f,a,b,1000)
plt.plot(c,f(c),"rs")
plt.plot(x,f(x))

plt.grid()
plt.show()
'''
#2)bisection method
'''
def bisection(f,a,b,N):
   if f(a)*f(b)>0:
      print("bisection method fails to find the solution")
      return None
   for i in range(N):
      c = (a+b)/2
      if f(c) == 0:
         print("exact solution has been found!")
         return c
      if f(a)*f(c) < 0:
         b = c
      elif f(b)*f(c)<0:
         a = c
      else:
         print("bisection method fails to find a solution")
   return (a+b)/2
f = lambda x: -0.6*x**2 + 2.4*x + 5.5
a = 5
b = 10
N = 3
c = bisection(f,a,b,N)

print(c,f(c))
'''
#3)Error

def bisection(f,a,b,N):
   c = (a+b)/2
   if f(a)*f(b)>0:
      print("bisection method fails to find the solution")
      return None
   current = c
   prev = c
   for i in range(N):
      c = (a+b)/2
      current = c
      print(f"iteration num:{i} estimated error {abs(current-prev)}")
      if f(c) == 0:
         print("exact solution has been found!")
         return c
      if f(a)*f(c) < 0:
         b = c
      elif f(b)*f(c)<0:
         a = c
      else:
         print("bisection method fails to find a solution!")
   return (a+b)/2
f = lambda x: -0.6*x**2 + 2.4*x + 5.5
a = 5
b = 10
N = 30
c = bisection(f,a,b,N)

#4)Checking

print(f(c))






























