import matplotlib.pyplot as plt
import pandas as pd

csv_data = pd.read_csv('FinancialData.csv', sep=',', parse_dates=False, index_col=0)
csv_data.plot()
plt.show()