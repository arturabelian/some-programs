# График сигмойды.

from scipy.special import expit
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 121)
y = expit(x)
plt.plot(x, y)
plt.grid()
plt.xlim(-6, 6)
plt.xlabel('x')
plt.title("expit(x)")
plt.show()