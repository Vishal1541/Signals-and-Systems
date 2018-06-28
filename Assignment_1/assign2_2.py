from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t0 = 1.2
a = 2
b = 3.2
t = np.linspace(-4-2*t0,4+2*t0,500)
x1 = []	# Unit pulse
x2 = [] # Sin
x3 = []
y1 = []
y2 = []
y3 = []
y4 = []

def FuncY(x):
	return x

def unitPulse(t):
	if(t<0 or t>2):
		return 0
	else:
		return 1

for i in t:
	x1.append(unitPulse(2*i))
	x2.append(np.sin(2*i))
for i in range(0,len(x1)):
	x3.append(a*x1[i] + b*x2[i])
for i in x1:
	y1.append(FuncY(i))
for i in x2:
	y2.append(FuncY(i))
for i in x3:
	y3.append(FuncY(i))
for i in range(0,len(x1)):
	y4.append(a*y1[i] + b*y2[i])

plt.subplot(2,1,1)
plt.title("Linearity - Linear")
plt.plot(t, y3, color = "red")
plt.plot(t, y4, color = "green")
plt.ylim(-20, 20)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(("y(ax1 + bx2)","ay1 + by2"))

t2 = np.linspace(-4+t0,4+t0,500)
x4 = []
y4 = []
x5 = []
y5 = []

for i in t2:
	x4.append(unitPulse(i-t0))
	x5.append(unitPulse(i))
for i in x4:
	y4.append(FuncY(i))
for i in range(0,len(x5)):
	y5.append(FuncY(x5[i]))


plt.subplot(2,1,2)
plt.title("Time Invariance - No")
plt.plot(t, y4, color = "red")
plt.plot(t2, y5, color = "green")
plt.ylim(-4, 4)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(("x(t-t0)","y(t-t0)"))
plt.show()