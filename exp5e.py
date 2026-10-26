import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.boxplot(data=np.random.randn(10014))
plt.title("Box plot")
plt.show()