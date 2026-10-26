import pandas as pd

index = [
    ['Engineering', 'Engineering', 'Coding', 'Coding'],
    ['DS', 'CSE', 'Java', 'Python']
]

multi_index = pd.MultiIndex.from_arrays(
    index,
    names=['Department', 'Branch']
)

marks = pd.Series(
    [153, 900, 95, 78],
    index=multi_index
)

print("Original Series:")
print(marks)

print("\nData for Engineering:")
print(marks.loc['Engineering'])

print("\nData for DS:")
print(marks.loc[('Engineering', 'DS')])

print("\nData for Coding:")
print(marks.loc['Coding'])