import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 4)

sns.boxplot(
    data=data,
    showfliers=True,
    fliersize=7,
    linewidth=2
)

plt.title("Box Plot")
plt.xlabel("Columns")
plt.ylabel("Values")

plt.show()