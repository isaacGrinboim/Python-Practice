import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1, 20)
y = x**3
print(x)
print(y)
#y = x + 5:
n = 10
plt.plot(x,y , "*-g")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('')


fig , axes = plt.subplots(nrows = 1, ncols = 10)
plt.tight_layout()

colors = ['g','b','r','c' , 'g','b','r','c']
i = 0
for axis in axes:
    axis.plot(x,x**i,colors[i%len(colors)])
    i+=1
fig
plt.show()