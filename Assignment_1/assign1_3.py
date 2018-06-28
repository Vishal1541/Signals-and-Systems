import matplotlib.pyplot as plt
import numpy as np
# import pylab
# import pickle

    # matplotlib.pyplot to plot and visualize the data
    # numpy to generate the mathematical function
    # pylab to help with interactive plots
    # pickle to dump the data into a file for future use

t = np.linspace(-10, 5, 500)
expo = []
for i in t:
	expo.append(np.exp(i))
plt.plot(t, expo, color = "green")
plt.ylim(-0.2, 100)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()