import matplotlib.pyplot as plt

import numpy as np

from math import *



f = lambda x: x**2 - 3 - sqrt(3)

a = -3

b = 1

eps = 10**(-4)

def bisection(f,a,b,eps):
   global count
   count = 0
   if f(a)*f(b)>0:
      print("bisection method failed to find a solution!")
      return None
   while True:
      if count > (log(b-a)-log(eps))/log(2):
         return c
         break
      c = (a+b)/2
      if f(c) == 0:
         return c
      if f(a)*f(c)<0:
         c = b
      if f(b)*f(c)<0:
         c = a
      count += 1
   return (a+b)/2

c = bisection(f,a,b,eps)
print(c)
print("the num of iterations: ", count)












