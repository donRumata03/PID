import matplotlib.pyplot as plt
import numpy as np

lag = 0.01
length = 2000.0
x = np.arange(0.0, length, lag)

c = (np.sin(x/4) * 0.05 + np.sin(x/10)*0.1 + np.sin(x/100) + np.sin(x/1000))
# c = x
#c = np.array([1000] * int(length / lag))
l = np.arange(20, 40, 0.1)

x2 = np.arange(len(l))
ms = []
MIN = None
# plt.plot(x, c)
for i in l:
    Kp = i
    Ki = 0
    Kd = 100

    S = 0.0
    s = 0

    Sentensivity = 20000.0
    out = 0.0
    C = 5.0
    Elast = c[0] - out
    Speed = 0
    max_power = 0.01
    outs = []
    ##############################
    # Out = Integral(Integral(U))#
    ##############################

    for t in range(int(length / lag)):
        e = c[t] - out
        S += e
        s += e ** 4
        U = Kp * e + Ki * S * lag + Kd * (e - Elast) / lag
        if U < 0:
            U = max(U, -max_power)
        else:
            U = min(U, max_power)

        Speed += U / Sentensivity
        outs.append(out)
        out += Speed
        Elast = e

    ms.append(s)

    print(abs(s))
    # plt.grid(True)


plt.plot(l, np.array(ms))
plt.show()


