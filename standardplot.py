#%%

import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np

x = np.linspace(0, 20, 100)
#print("type of x is "+type(x))
#print("x is "+x)
plt.plot(x, np.sin(x))
plt.show