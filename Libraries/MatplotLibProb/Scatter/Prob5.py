import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

w1=[88,8,89,87]
h1=[177,55,190,188]
w2=[81,60,110,35]
h2=[188,165,206,110]
w3=[70,65,75,89]
h3=[174,155,191,181]

plt.scatter(w1, h1, marker='*', color='red')
plt.scatter(w2, h2, marker='*', color='green')
plt.scatter(w3, h3, marker='*', color='blue')
plt.xlabel('weight')
plt.ylabel('height')
plt.show()