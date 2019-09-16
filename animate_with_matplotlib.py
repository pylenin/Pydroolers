import random
from itertools import count
from matplotlib import pyplot as plt
from matplotlib import animation

x_values = []
y_values = []

start = count()
def animate(i):

    x_values.append(next(start))
    y = random.randint(0, 5)
    y_values.append(y)
    plt.cla()
    plt.plot(x_values,y_values)

anim = animation.FuncAnimation(plt.gcf(),
                               animate,
                               interval=200)

plt.show()
