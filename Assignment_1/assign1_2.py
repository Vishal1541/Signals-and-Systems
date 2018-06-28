from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-4, 4, 500)
a = 0
b = 2
unit_impulse = []
for i in t:
	if(i<0 or i>2):
		unit_impulse.append(0)
	else:
		unit_impulse.append(1)
plt.plot(t, unit_impulse, color = "red")
plt.ylim(-2, 2)
plt.xlabel('Time')
plt.ylabel('Amplitude - Unit Pulse Function')
plt.show()