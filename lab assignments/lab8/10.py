import numpy as np
import matplotlib.pyplot as plt
#TASK1
'''
x = np.array([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5],float)
y = np.array([-1,-0.7,0.2,1.5,2.1,3.2,3.5,3.6,3.3,3.6,4.2,5.7],float)
plt.scatter(x,y,label="data")
n=len(x)
A=np.array([[sum((np.cos(x))**2), sum(np.exp(x)*np.cos(x)), sum(np.cos(x))],
            [sum(np.exp(x)*np.cos(x)), sum(np.exp(2*x)), sum(np.exp(x))],
             [sum(np.cos(x)), sum(np.exp(x)), n]])
B=np.array([sum(y*np.cos(x)), sum(y*np.exp(x)), sum(y)])
X = np.linalg.inv(A).dot(B)
a = X[0]
b = X[1]
c = X[2]
print(X)
xm = np.linspace(-5,6,200)
f = lambda x: a*(np.cos(x))+b*np.exp(x)+c
plt.plot(xm,f(xm),label = "function obtained")
plt.plot(1.2,f(1.2),"rs")
plt.grid()
print("f(x) = {:.4f}*cos(x) + {:.4f}*e^x+{:.4f}".format(a,b,c))
plt.legend()

err = []
for i in range(len(x)):
   err.append(abs(f(x[i])-y[i]))
print("errors:")
for i in err:
   print(i)
plt.show()
'''
#TASK2
'''
x = np.array([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5],float)
y = np.array([-1,-0.7,0.2,1.5,2.1,3.2,3.5,3.6,3.3,3.6,4.2,5.7])
n = len(x)
plt.scatter(x,y,label = "Data")
A = np.array([[sum(x**6),sum(x**5),sum(x**4),sum(x**3)],
              [sum(x**5),sum(x**4),sum(x**3),sum(x**2)],
              [sum(x**4),sum(x**3),sum(x**2),sum(x)],
              [sum(x**3),sum(x**2),sum(x),n]],float)
B = np.array([sum(y*(x**3)),sum(y*(x**2)),sum(x*y),sum(y)],float)
X = np.linalg.inv(A).dot(B)
a = X[0]
b = X[1]
c = X[2]
d = X[3]
print(f"f(x) = {a}*x^3+{b}*x^2+{c}*x+{d}")
plt.legend()
plt.grid()
xm = np.linspace(-10,10,1000)
f = lambda x: a*x**3+b*x**2+c*x+d
plt.plot(xm,f(xm))
plt.plot(1.2,f(1.2),"rs")
print("Errors:")
err = []
for i in range(len(x)):
   err.append(abs(f(x[i])-y[i]))
for i in err:
   print(i)
plt.show()
'''
#TASK3
'''
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
'''



















