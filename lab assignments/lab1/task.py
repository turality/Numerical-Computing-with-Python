pi = 0
import math

count  = 0
k=0

while True:
   
   if abs(math.pi-pi) <= 0.001:
      print(abs(math.pi-pi))
      break
   pi +=  (((-1)**k)*4)/(2*k+1)
   count+=1
   k+=1
print("the pi number obtained from math module: ",math.pi)
print("the pi number obtained from taylor's formula: ",pi)
print("the number of terms needed to be passed: ",count)
   
