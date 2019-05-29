from numpy import*
from matplotlib import pyplot as plt


class Turtle:
    def __init__(self, aim, v = 1, x = 0, y = 0):
        self.aim = aim
        self.v = v
        self.x = x
        self.y = y

    def move(self):
        dx = self.x - self.aim.x
        dy = self.y - self.aim.y

        if dx == 0:
            vy = v
            vx = 0

        elif dy == 0:
            vx = v
            vy = 0
        else:
            vx = v * sqrt(1 / (1 + dy / dx))
            vy = v * sqrt(1 / (1 + dx / dy))

        self.x += vx * lag
        self.y += vy * lag




msx1 = []
msy1 = []


msx2 = []
msy2 = []

msx3 = []
msy3 = []

msx4 = []
msy4 = []


lag = 0.0001
beta = 0.001

x1 = 1
y1 = 1
y2 = 0
x2 = 1
x3 = 0
y3 = 0
x4 = 0
y4 = 1


v = 1
t = 0

t1 = Turtle(aim=None, v=1, x=0, y=0)
t2 = Turtle(aim=t1, v=1, x=1, y=0)
t1.aim = t2

while True:
    if (t1.x-t2.x) ** 2 + (t1.x-t1.x) ** 2 <= beta:
        break
    t += lag

    #######################
    t1.move()
    t2.move()
    '''

    if dx1 == 0:
        vy1 = v
        vx1 = 0
    elif dy1 == 0:
        vx1 = v
        vy1 = 0
    else:
        vx1 = v * sqrt(1/(1 + dy1/dx1))
        vy1 = v * sqrt(1/(1 + dx1/dy1))

    if x1 > x2:
        vx1 *= -1
    if y1 > y2:
        vy1 *= -1

    ##################

    if dx2 == 0:
        vy2 = v
        vx2 = 0
    elif dy2 == 0:
        vx2 = v
        vy2 = 0
    else:
        vx2 = v * sqrt(1 / (1 + dy2 / dx2))
        vy2 = v * sqrt(1 / (1 + dx2 / dy2))

    if x2 > x3:
        vx2 *= -1
    if y2 > y3:
        vy2 *= -1

    #################

    if dx3 == 0:
        vy3 = v
        vx3 = 0
    elif dy3 == 0:
        vx3 = v
        vy3 = 0
    else:
        vx3 = v * sqrt(1 / (1 + dy3 / dx3))
        vy3 = v * sqrt(1 / (1 + dx3 / dy3))

    if x3 > x4:
        vx3 *= -1
    if y3 > y4:
        vy3 *= -1

    ####################

    if dx4 == 0:
        vy4 = v
        vx4 = 0
    elif dy4 == 0:
        vx4 = v
        vy4 = 0
    else:
        vx4 = v * sqrt(1 / (1 + dy4 / dx4))
        vy4 = v * sqrt(1 / (1 + dx4 / dy4))

    if x4 > x1:
        vx4 *= -1
    if y4 > y1:
        vy4 *= -1

    ####################

    x1 += vx1 * lag
    y1 += vy1 * lag
    y2 += vy2 * lag
    x2 += vx2 * lag
    x3 += vx3 * lag
    y3 += vy3 * lag
    x4 += vx4 * lag
    y4 += vy4 * lag
        
    '''

    msx1.append(t1.x)
    msy1.append(t1.y)

    msx2.append(t2.x)
    msy2.append(t2.y)


print(t)
plt.plot(msx1, msy1)
plt.plot(msx2, msy2)

plt.show()
