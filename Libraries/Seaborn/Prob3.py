import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('tips')
print(df)
sb.scatterplot(x = "day", y = "total_bill", data=df)
plt.show()