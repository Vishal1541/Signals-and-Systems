from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t0 = 1
a = 4
b = 3
t = np.linspace(-4,4,500)
x1 = []	# Unit pulse
x2 = [] # Sin
x3 = []
y1 = []
y2 = []
y3 = []
y4 = []

def FuncY(x):
	return np.exp(-x)

def unitPulse(t):
	if(t<0 or t>2):
		return 0
	else:
		return 1

for i in t:
	x1.append(unitPulse(i))
	x2.append(np.sin(i))
for i in range(0,len(x1)):
	x3.append(a*x1[i] + b*x2[i])
for i in x1:
	y1.append(FuncY(i))
for i in x2:
	y2.append(FuncY(i))
for i in x3:
	y3.append(FuncY(i))
for i in range(0,len(y1)):
	y4.append(a*y1[i] + b*y2[i])

plt.subplot(2,1,1)
plt.title("Linearity - Non Linear")
plt.plot(t, y3, color = "red")
plt.plot(t, y4, color = "green")
plt.ylim(-4, 40)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(("y(ax1 + bx2)","ay1 + by2"))

t2 = np.linspace(-4+t0,4+t0,500)
X1 = []
Y1 = []
X2 = []
Y2 = []

for i in t:
	X1.append(unitPulse(i-t0))
	X2.append(unitPulse(i))
for i in X1:
	Y1.append(FuncY(i))
for i in X2:
	Y2.append(FuncY(i))


plt.subplot(2,1,2)
plt.title("Time Invariance - Yes")
plt.plot(t, Y1, color = "red")
plt.plot(t2, Y2, color = "green")
plt.ylim(-4, 4)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(("x(t-t0)","y(t-t0)"))
plt.show()