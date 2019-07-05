import matplotlib.pyplot as plt
import pandas as pd
languages= ('Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++')
popularity= (22.2, 17.6, 8.8, 8, 7.7, 6.7)
colors = ["red", "green", "blue", "black", "grey", "cyan"]
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', startangle=140)
plt.show()