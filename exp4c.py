import pandas as pd

df1 = pd.DataFrame(
    {
        'Name': ['Ravi', 'Vara', 'Prasad'],
        'Marks': [78,90,85.5],
        'Grade': ['A', 'B', None]
    },
    index=[101, 102, 103]
)

# Create the second DataFrame
df2 = pd.DataFrame(
    {
        'Name': ['Ravi', 'Vara', 'Prasad'],
        'Marks': [None,90.5,88.0],
        'Grade': [None, 'A', 'B']
    },
    index=[153, 154, 155]
)

print("First DataFrame:")
print(df1)

print("\nSecond DataFrame:")
print(df2)

merged = pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True,
    how='outer',
    suffixes=('_DF1', '_DF2')
)

print("\nMerged DataFrame:")
print(merged)

combined = df1.combine_first(df2)

print("\nDataFrame after combine_first():")
print(combined)