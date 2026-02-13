import pandas as pd

# Question 1
df1 = pd.DataFrame({'Id': [1, 2, 3, 4],
        'Value1':['A', 'B', 'C', 'D']})
df2 = pd.DataFrame({'Id': [1, 3, 5], 
         'Value2':['E','F','G']})
print(f"{df1}\n{df2}")

# Question 2
merged_df = pd.merge(df1, df2, on='Id')
print(f"\n Merged Data Frame:\n{merged_df}")

# Question 3
outer_merge = pd.merge(df1, df2, on='Id', how='outer')
print(f"\nOuter Merge Data Frame:\n{outer_merge}")

# Question 4
df4 = pd.DataFrame({'Id_x':[0,1,2,3,4],
        'Value1':['A','B','C','D','E'],
        'Id_y':[0,1,2,3,4],
        'Value2':['A','B','C','D','E']})
combined_df = df4.combine_first(outer_merge)
print(f"\nCombined Data Frames:\n{combined_df}")
