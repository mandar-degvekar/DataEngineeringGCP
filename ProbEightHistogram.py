import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

x = np.random.random_integers(1,200,5)
pt.hist(x,bins=20)
pt.ylabel('no')
pt.savefig("filname.pdf")