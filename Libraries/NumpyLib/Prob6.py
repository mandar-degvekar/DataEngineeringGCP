import numpy as np
print('original array: \n')
x = np.ones((3,3))
print(x)
print('after padding: \n')
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)