import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'category': ['A', 'B', 'C'],
    'values': [10, 20, 15]
})

df.plot(kind='bar', x='category', y='values')

plt.title("BarPlot")
plt.xticks(rotation=0)
plt.show()