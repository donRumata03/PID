import matplotlib.pyplot as plt
import numpy as np
lag = 0.01
length = 5000.0
# x = np.arange(0.0, length, lag)

# c = (np.sin(x/10)*0.1 + np.sin(x/100) + np.sin(x/1000))
# c = x
c = np.array([1000] * int(length / lag))
l = np.array([0.05, 0.1, 0.5, 1, 5, 10])

x2 = np.arange(len(l))
ms = []
# plt.plot(x, c)
for i in l:
    Kp = i
    Ki = 0
    Kd = 0

    S = 0.0
    s = 0

    Sentensivity = 20000.0
    out = 0.0
    C = 5.0
    Elast = c[0] - out
    Speed = 0
    max_power = 0.1
    outs = []
    ##############################
    # Out = Integral(Integral(U))#
    ##############################


    for t in range(int(length/lag)):
        e = c[t] - out
        S += e
        s += e**4
        U = Kp*e + Ki*S*lag + Kd*(e-Elast)/lag
        if U < 0:
            U = max(U, -max_power)
        else:
            U = min(U, max_power)

        Speed += U/Sentensivity
        outs.append(out)
        out += Speed
        Elast = e




    #plt.plot(x, outs)
    #plt.plot(x,-np.cos(x*np.pi/400)*1000+1000)
    #plt.plot(np.array([0]), np.array([0]))

    #plt.grid(True)

    ms.append(round(s))

plt.plot(l, np.array(ms))
plt.show()


