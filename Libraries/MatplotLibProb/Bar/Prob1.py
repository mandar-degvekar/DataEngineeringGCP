import matplotlib.pyplot as plt
import pandas as pd
languages= ('Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++')
popularity= (22.2, 17.6, 8.8, 8, 7.7, 6.7)
plt.bar(languages, popularity)
plt.ylabel('popularity')
plt.title('Programming language usage')
plt.show()