import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

filename = "hamiltonx.dat"

data = pd.read_csv(filename, sep='\t')

x = data.iloc[:, 1]
y = data.iloc[:, 2]
z = data.iloc[:, 3]
t = data.iloc[:, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = t

line = ax.scatter(x, y, z, c=colors, cmap='viridis')

ax.set_xlabel('q')
ax.set_ylabel('p')
ax.set_zlabel('H')

cbar = fig.colorbar(line)
cbar.set_label('Time (t)')

plt.show()
