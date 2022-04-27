import numpy as np
import matplotlib.pyplot as plt
t = np.array([0,1,2,3],float)
x = np.array([0.1,0.4,0.2,0.2],float)
y = np.array([3,2,1,2],float)
n = len(x)

A = np.array([[n,sum(x),sum(t)],
              [sum(x),sum(x*x),sum(x*t)],
              [sum(t),sum(x*t),sum(t*t)]],float)
B = np.array([sum(y),sum(x*y),sum(t*y)],float)

X = np.linalg.inv(A).dot(B)
print(X)
