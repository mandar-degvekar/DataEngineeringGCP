import pandas as pd
import  numpy as np
data = [['Anastasia', 12.5,1,'yes','c'], ['Dima', 9,2,'no','d'], ['Katherine', 14,1,'yes','e'],['James', 16.5,1,'yes','f'],['Emily', np.nan,1,'no','g']]
df=pd.DataFrame(data,columns=['name','score','attempts','qualify','labels'])
print(df)
print('\n')
print('data after slicing \n')
print (df.iloc[[1, 3, 4], [0,1,4]])