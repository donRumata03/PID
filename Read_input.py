from matplotlib import  pyplot as plt
import numpy as np
flag = False
print(bool(''))
while not flag:jnzujotyyst pkjv

    s = open("C:\\VOVA\\TxtFiles\\PythonC++Syncro\\sync.txt", "r").read()
    if s is not '':
        s = int(s)
    flag = bool(s)
ms_x = list(map(float, str(open("C:\\VOVA\\TxtFiles\\PythonC++Syncro\\data_x.txt", "r").read()).split()))
ms_y = list(map(float, str(open("C:\\VOVA\\TxtFiles\\PythonC++Syncro\\data_y.txt", "r").read()).split()))

plt.plot(np.array(ms_x), np.array(ms_y))

plt.show()
