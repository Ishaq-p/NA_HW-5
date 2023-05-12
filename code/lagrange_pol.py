from rounding import rounding as rnd
import numpy as np

xx=101
x=[0,43, 80, 94]
y=[13.649, 35.606, 70.586, 84.680]

L0 = ((xx-x[1])*(xx-x[2])*(xx-x[3]))/((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3]))
L1 = ((xx-x[0])*(xx-x[2])*(xx-x[3])) / ((x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3]))
L2 = ((xx-x[0])*(xx-x[1])*(xx-x[3])) / ((x[2]-x[0])*(x[2]-x[1])*(x[2]-x[3]))
L3 = ((xx-x[0])*(xx-x[1])*(xx-x[2])) / ((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2]))
Li=[L0,L1,L2,L3]

result=0
for i in range(4):
    print(Li[i]*y[i])
    result+=Li[i]*y[i]

print("\nL:\t",result)