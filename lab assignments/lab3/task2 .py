import matplotlib.pyplot as plt
import numpy as np
#a 
'''
f = lambda x: -1 + 5.5 * x - 4*x**2+0.5 *x**3

x = np.linspace(-1000,1000,100000)

plt.plot(x,f(x))
plt.grid()
def newton(f,df,x0,eps,max_iter):
   xn = x0
   for k in range(max_iter):
      fx = f(xn)
      if abs(fx) < eps:
         print("found the solution!")
         return xn
      dfx = df(xn)
      if dfx == 0:
         print("zero derivative!")
         return None
      xn = xn - fx/dfx
   print("exceeded the max number of iterations!")
   return None
df = lambda x: 5.5 - 8*x + 1.5*x**2
x0 = 200 #approximately written from the graph
eps = 0.0001
max_iter = 100
root = newton(f,df,x0,eps,max_iter)
print(f"{root}\n{f(root)}")
plt.plot(root,f(root),"rs")
plt.show()
'''
#b,c,d
def newton(f,df,x0,eps):
   xn = x0
   global count
   count = 0
   while True:
      count += 1
      fx = f(xn)
      if abs(fx)<eps:
         print("found the exact solution!")
         return xn
      dfx = df(xn)
      if dfx == 0:
         print("zero derivative!")
         return None
      xn = xn -fx/dfx
f = lambda x: -1 + 5.5 * x - 4*x**2+0.5 *x**3

x = np.linspace(-1000,1000,1000000)

eps = 0.0001

df = lambda x: 5.5 - 8*x + 1.5*x**2

x0 = 200

root = newton(f,df,x0,eps)
print("the total number of iterations: ",count)
plt.plot(x,f(x))
plt.grid()
plt.plot(root,f(root),"rs")
plt.show()



   




   
