import numpy as np
import matplotlib.pyplot as plt
#the x and y arrays are given as data tables, they can be modified
#the A and B contain the coefficients which we get from the equations
x = np.array([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5],float)
y = np.array([-1,-0.7,0.2,1.5,2.1,3.2,3.5,3.6,3.3,3.6,4.2,5.7])
n = len(x)
plt.scatter(x,y,label = "data")
plt.grid()
A = np.array([[n,sum(np.sin(x)),sum(x**3)],
              [sum(np.sin(x)),sum((np.sin(x))**2),sum(x**3*np.sin(x))],
              [sum(x**3),sum(x**3*np.sin(x)),sum(x**6)]],float)
B = np.array([sum(y),sum(y*np.sin(x)),sum(y*x**3)],float)
X = np.linalg.inv(A).dot(B)
a = X[0]
b = X[1]
c = X[2]
print(f"f(x) = {a}+{b}*sin(x)+{c}*x^3")
f = lambda x: a + b*np.sin(x) + c * x**3
xm = np.linspace(-10,10,1000)
plt.plot(xm,f(xm),label = "function")
plt.plot(1.2,f(1.2),"rs")
plt.legend()
err = []
for i in range(len(x)):
   err.append(abs(f(x[i])-y[i]))
print("The errors: ")
for i in err:
   print(i)

plt.show()


