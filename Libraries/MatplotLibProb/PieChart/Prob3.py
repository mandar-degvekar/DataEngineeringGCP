import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('medals.csv')
country_data = df["Country"]
medal_data = df["Medals"]
colors = ["red", "green", "blue", "brown", "grey", "cyan"]
plt.pie(medal_data, labels=country_data, colors=colors, autopct='%1.1f%%', startangle=140)
plt.show()