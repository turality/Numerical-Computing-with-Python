import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**3-2*x**2+x-3
df = lambda x: 3*x**2-4*x+1

def newton(f,df,x0,eps,max_iter):
   xn = x0
   for k in range(max_iter):
      fx = f(xn)
      if abs(fx)<eps:
         print("found the solution!")
         return xn
      dfx = df(xn)
      if dfx == 0:
         print("zero derivative!")
         return None
      xn = xn - fx/dfx
   print("the loop exceeded the max number of iterations!")
   return None
x0 = 4

max_iter = 10

eps = 0.001

root = newton(f,df,x0,eps,max_iter)

print(f"{root} \n {f(root)}")


