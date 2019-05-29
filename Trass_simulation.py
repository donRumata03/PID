from matplotlib import  pyplot as plt
import numpy as np


ms_x = sorted([1.92, 1.89, 1.8, 1.85, 1.87, 1.88, 1.94, 1.95, 1.97, 1.98, 2.00, 2.22, 2.35, 2.81])
ms_y = sorted([7.22, 5.64, 4.00, 3.50, 4.55, 4.86, 8.64, 9.68, 11.23, 12.27, 13.95, 37.2, 52.42, 100.52])

plt.plot(np.array(ms_x), np.array(ms_y))

plt.show()
