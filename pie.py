
import matplotlib.pyplot as plt
import pandas as pd
file = pd.read_excel('mydata.xlsx')
plt.pie(file['Y values'],labels=file['X values'])
plt.show()