import matplotlib.pyplot as plt
import numpy as np
#a)
'''
x = np.linspace(-1000,1000,100000)

f = lambda x: x - np.sin(x)-0.25

plt.plot(x,f(x))
plt.grid()
plt.show()

x0 = 10#determined approximately from the graph
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
         print("the method has found the exact solution")
         return xn
      dfx = df(xn)
      if dfx==0:
         print("derivative is zero!")
         return None
      xn = xn - fx/dfx

x = np.linspace(-1000,1000,100000)

f = lambda x: x - np.sin(x)-0.25

df = lambda x: 1 - np.cos(x)

x0 = 10

eps = 0.0001

root = newton(f,df,x0,eps)

print(root)

print(f(root))

print("the total number of iterations: ",count)









