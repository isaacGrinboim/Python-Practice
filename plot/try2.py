import matplotlib.pyplot as plt
import numpy as np
size = 100   
x = [i/size for i in range(size)]
y = [i for i in range(size)]
def f(x):
    return np.sin(x)
colors = [i for i in range(size)]
plt.plot(x,[f(i) for i in x])
         #s=200, c = colors, cmap = "Reds")
plt.show()