import matplotlib.pyplot as plt
import numpy as np
from sys import stdout

lag = 0.01
length = 2000.0
x = np.arange(0.0, length, lag)

c = (np.sin(x/4) * 0.05 + np.sin(x/10)*0.1 + np.sin(x/100) + np.sin(x/1000))
# c = x
#c = np.array([1000] * int(length / lag))
Kps = np.arange(2, 15, 0.5)

ms2 = []
ms3 = []
l1 = 50
l2 = len(Kps)
for Kpx in range(l2):
    MIN = None
    ms = []
    Kpb = Kps[Kpx]
    l = np.arange(Kpb/2, Kpb*10, (Kpb*10 - Kpb/2)/l1)
    for i in range(l1):
        percent = ((100 * l1)* Kpx + i) / (l1*l2)
        stdout.flush()
        stdout.write("\r%d" % percent)
        stdout.write("%")

        Kp = Kpb
        Ki = 0
        Kd = l[i]

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

    ms2.append(min(ms))
    ms3.append(ms.index(min(ms)))

plt.plot(Kps, ms2)

plt.show()

plt.plot(Kps, ms3)

plt.show()


