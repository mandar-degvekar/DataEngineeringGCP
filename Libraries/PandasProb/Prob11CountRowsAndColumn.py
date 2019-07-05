import pandas as pd
import  numpy as np
data = [['Anastasia', 12.5,1,'yes','c'], ['Dima', 9,2,'no','d'], ['Katherine', 14,1,'yes','e'],['James', 16.5,1,'yes','f'],['Emily', np.nan,1,'no','g']]
df=pd.DataFrame(data,columns=['name','score','attempts','qualify','labels'])
print(df)
print('\n')
print('column vise count of rows')
print(df.count())
total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print('\n')
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))