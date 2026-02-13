import pandas as pd

data = pd.read_csv('Problem_Set_5/planets.csv')
clean_data = data.dropna()

# Question 1
method_totals = clean_data.groupby('method')['number'].sum()
mask = method_totals > 900
print(f"Methods Greater Than 900:\n{method_totals[mask]}")

# Question 2
orbital_range = clean_data.groupby('method')['orbital_period'].agg(['min', 'max'])
print(f"\nOrbital Range:\n{orbital_range}")

# Question 3
clean_data['numbers_each_year'] = clean_data.groupby('year')['number'].transform('sum').cumsum()
print(f"\nTotal Number of Planets Discoverd by Year:\n{clean_data.head(10)}")

# Question 4
max_periods = clean_data.groupby('method')['orbital_period'].max()
method_with_longest = max_periods.idxmax()
longest_value = max_periods.max()
print(f"Method with the longest orbital period is {method_with_longest} at {longest_value} days.")
