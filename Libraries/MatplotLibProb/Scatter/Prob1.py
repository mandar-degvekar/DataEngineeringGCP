import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(50, 2), columns=['a', 'b'])
df.plot.scatter(x='a', y='b')
plt.show()
