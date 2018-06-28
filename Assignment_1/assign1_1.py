import matplotlib.pyplot as plt
import numpy as np
# import pylab
# import pickle

    # matplotlib.pyplot to plot and visualize the data
    # numpy to generate the mathematical function
    # pylab to help with interactive plots
    # pickle to dump the data into a file for future use

t = np.arange(-10,10,0.1)
y = np.sin(t)
plt.ylim(-2,2)
plt.plot(t,y)
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude = sin(t)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()