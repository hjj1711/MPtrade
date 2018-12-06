import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)
y=2*x+1
y2=2**x
plt.figure()
plt.plot(x,y)
plt.figure()
plt.plot(x,y2)
plt.show()
