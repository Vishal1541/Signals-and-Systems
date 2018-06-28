import numpy as np
import math
import matplotlib.pyplot as plt

# INPUT
print "Enter the leftmost and rightmost (n) "
n1 = int(input())
n2 = int(input())
print "Enter the x[n]: "
xn = map(int,raw_input().split())

# PROCESS
modX = []
angleX = []
W = np.arange(0,10,0.02)
n_total = n2-n1+1
n = []
for i in range(n1,n2+1):
	n.append(i)
for w in W:
	A = 0
	B = 0
	for i in range(0,n_total):
		A += xn[i] * math.cos((n[i])*w)
		B += xn[i] * math.sin(n[i]*w)
	modX.append(math.sqrt(A**2 + B**2))
	angleX.append(math.atan(B / A))

plt.subplot(2,1,1)
plt.plot(n,xn,color="blue")
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(2,1,2)
plt.plot(W,modX,color = "red")
plt.plot(W,angleX,color = "green")
plt.xlabel('Frequency')
plt.ylabel('mod-red, angle-green')
plt.show()