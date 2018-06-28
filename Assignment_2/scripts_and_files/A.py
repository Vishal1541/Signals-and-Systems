import numpy as np
print ("Enter the x(n): ")
xn = map(float, raw_input().split())
print ("Enter the h(n): ")
hn = map(float, raw_input().split())
yn = np.convolve(xn,hn)
print yn