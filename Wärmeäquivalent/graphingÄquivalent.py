import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

x, y = np.loadtxt("dmechanischewärmeäquivalent.dat", delimiter=None, unpack=True, dtype=float, usecols=[0,1])

plt.scatter(x, y, label='Datos Experimentales', color='#a559aa', marker='o', s=5)

plt.xlabel('Número de Vueltas')
plt.ylabel('T (°C)')
plt.title('Equivalente Mecánico del Calor')
plt.legend(labels={'Datos Experimentales':'#a559aa'})
plt.grid(True)
plt.xticks(np.arange(0, 3801, 250))
plt.yticks(np.arange(23, 31, 0.5))

plt.errorbar(x, y, xerr=0, yerr=0.1, fmt='none', color='#a559aa', capsize=3)

plt.tight_layout()

plt.show()
