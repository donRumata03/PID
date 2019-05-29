import numpy as np
from matplotlib import pyplot as plt


def gauss(sigma = 3, miu = 1, length = 10, lag = 0.01):
    ms = [0] * int(length/lag)
    for i in range(len(ms)):
        x = i*lag
        ms[i] = (np.e**(-((x-miu)**2)/(2*(sigma**2)))/(sigma*np.sqrt(2*np.pi)))
    print(ms)
    return np.array(ms)


l = 20
la = 0.001


ms = gauss(length=l, lag=la, miu=int(l/2))
xs = np.arange(0, l, la)

plt.plot(xs, ms)
plt.show()
