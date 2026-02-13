import pandas as pd

df1 = pd.DataFrame({'ID1': [1, 2, 3],
         'ID2': [101, 102, 103],
                'Value1': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID1': [2, 3, 4],
         'ID2': [102, 103, 104],
                'Value2': ['X', 'Y', 'Z']})
df3 = pd.DataFrame({'ID3': [101, 102, 103],
                'Value3': ['Apple', 'Banana', 'Cherry']})

# Question 1
concat_df = pd.concat([df1, df2, df3])
print(f"\nQuestion 1:\n{concat_df}")

# Question 2
merge_df1 = pd.merge(df1, df2, on=['ID1', 'ID2'])
merge_df2 = pd.merge(merge_df1, df3, left_on='ID2', right_on='ID3')
print(f"\nQuestion 2:\n{merge_df2}")
