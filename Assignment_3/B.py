import numpy as np
import math
import matplotlib.pyplot as plt
import soundfile as sf

# INPUT
xn1, rate = sf.read("part_0.wav")
xn2, rate = sf.read("part_19.wav")
xn3, rate = sf.read("part_22.wav")

# PROCESS
modX1 = []
angleX1 = []
modX2 = []
angleX2 = []
modX3 = []
angleX3 = []
W = np.arange(0,1.5,0.1)
n1 = []
n2 = []
n3 = []
for i in range(0,len(xn1)):
	n1.append(i)
for i in range(0,len(xn2)):
	n2.append(i)
for i in range(0,len(xn3)):
	n3.append(i)
for w in W:
	A1 = 0
	B1 = 0
	A2 = 0
	B2 = 0
	A3 = 0
	B3 = 0
	for i in range(0,len(xn1)):
		A1 += xn1[i] * math.cos(abs(n1[i])*w)
		B1 += xn1[i] * math.sin(n1[i]*w)
	for i in range(0,len(xn2)):
		A2 += xn2[i] * math.cos(abs(n2[i])*w)
		B2 += xn2[i] * math.sin(n2[i]*w)
	for i in range(0,len(xn3)):
		A3 += xn3[i] * math.cos(abs(n3[i])*w)
		B3 += xn3[i] * math.sin(n3[i]*w)
	modX1.append(math.sqrt(A1**2 + B1**2))
	angleX1.append(math.atan(B1 / A1))
	modX2.append(math.sqrt(A2**2 + B2**2))
	angleX2.append(math.atan(B2 / A2))
	modX3.append(math.sqrt(A3**2 + B3**2))
	angleX3.append(math.atan(B3 / A3))

plt.subplot(3,2,1)
plt.plot(n1,xn1,color="blue")
plt.xlabel('n1')
plt.ylabel('x1[n]')

plt.subplot(3,2,3)
plt.plot(n2,xn2,color="blue")
plt.xlabel('n1')
plt.ylabel('x1[n]')

plt.subplot(3,2,5)
plt.plot(n3,xn3,color="blue")
plt.xlabel('n1')
plt.ylabel('x1[n]')

plt.subplot(3,2,2)
plt.plot(W,modX1,color = "red")
plt.plot(W,angleX1,color = "green")
plt.xlabel('Frequency')
plt.ylabel('mod-red, angle-green')

plt.subplot(3,2,4)
plt.plot(W,modX2,color = "red")
plt.plot(W,angleX2,color = "green")
plt.xlabel('Frequency')
plt.ylabel('mod-red, angle-green')

plt.subplot(3,2,6)
plt.plot(W,modX3,color = "red")
plt.plot(W,angleX3,color = "green")
plt.xlabel('Frequency')
plt.ylabel('mod-red, angle-green')
plt.show()