import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

x, y = np.loadtxt("dThermistor2.dat", delimiter=None, unpack=True, skiprows=1, dtype=float, usecols=[2,3])

plt.scatter(x, y, label='Datos Experimentales', color='#a559aa', marker='o', s=5)

plt.xlabel("T (°C)")
plt.ylabel("R (Ω)")
plt.title("Termorresistencia MF72-8D11")
plt.legend(labels={'Datos Experimentales':'#a559aa'})
plt.grid(True)

plt.errorbar(x, y, xerr=0.1, yerr=0.001, fmt='none', color='#a559aa', capsize=3)

plt.tight_layout()

plt.show()
