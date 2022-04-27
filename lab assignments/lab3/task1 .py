import matplotlib.pyplot as plt
import numpy as np
# a)Graphically
'''
x = np.linspace(-1000,1000,100000)

f = lambda x: 2*x**3 - 11.7*x**2 +17.7*x-5

plt.plot(x,f(x))
plt.grid()
def bisection(f,a,b,max_iter):
   if f(a)*f(b)>0:
      print("bisection method fails to find a solution!");
      return None
   for i in range(max_iter):
      c = (a+b)/2
      if f(c) == 0:
         print("the method has found the exact solution!");
         return c
      if f(a)*f(c)<0:
         b = c
      if f(b)*f(c)<0:
         a = c
   return (a+b)/2
#by analysing the graph, i found out that the root is located somewhere
#between -250 and 250. as the signs of the function's values are different there
#i took them as intervals for bisection method to find the root
a = -250
b = 250
root = bisection(f,a,b,100)
print(f"root: {root}\nf(root): {f(root)}")
plt.plot(root,f(root),"rs")
plt.show()
'''
# b)Using 3 iterations of bisection method
'''
x = np.linspace(-50,50,10000)
f = lambda x: 2*x**3-11.7*x**2+17.7*x-5
def bisection(f,a,b,max_iter):
   if f(a)*f(b)>0:
      print("the bisection method fails to find a root")
      return None
   c = (a+b)/2
   prev = f(c)
   current = f(c)
   for i in range(max_iter):
      c = (a+b)/2
      current = f(c)
      if f(c) == 0:
         print("the method has exactly found the solution")
         return c
      if f(a)*f(c)<0:
         b = c
      if f(b)*f(c)<0:
         a = c
   global relErrorBi
   relErrorBi = abs(prev-current)/current;
   return (a+b)/2
a = -5
b = 5
max_iter = 3
print("by using 3 iterations!")
root = bisection(f,a,b,max_iter)
print(f"root: {root}\nf(root): {f(root)}")
print(f"relative error: {relErrorBi}")
'''
# c) using 3 iterations of Newton-Raphson method

def newton(f,df,x0,eps,max_iter):
   xn = x0
   prev = f(xn)
   current = f(xn)
   for k in range(max_iter):
      fx = f(xn)
      current = f(xn)
      if abs(fx)<eps:
         print("found solution!")
         return xn
      dfx = df(xn)
      if dfx == 0:
         print("zero derivative!")
         return None
      xn = xn - fx/dfx
   print("exceeded the max number of iterations")
   return None

f = lambda x: 2*x**3-11.7*x**2+17.7*x-5

df = lambda x: 6*x**2 - 11.7*2*x+17.7

max_iter = 3

eps = 3.5

x0 = 3

root = newton(f,df,x0,eps,max_iter)

print(root)

print(f(root))

























