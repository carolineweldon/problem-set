import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0.0, 4.5, 0.5)

y1 = x         
y2 = x**2                 
y3 = 2**x      

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()