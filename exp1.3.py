import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

print("First Five rows of the data set: ")
print(df.head())

print("\n Data set information: ")
print(df.info())

print("\n Number of rows and colomuns: ")
print(df.shape)