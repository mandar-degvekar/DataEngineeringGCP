import math
import random
import matplotlib.pyplot as plt
balls = 25
x = [random.triangular() for i in range(balls)]
y = [random.gauss(0.5, 0.25) for i in range(balls)]
colors = [random.randint(1, 4) for i in range(balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(balls)]
# draw the plot
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()