import pandas as pd

# Question 1
data = pd.read_csv('Problem_Set_5/planets.csv')
print(f"Head of Dataset:\n{data.head()}\n")
# Description: dataset documents method, mass, orbital period, distance, and year data for planets

# Question 2
clean_data = data.dropna()
data_stats = clean_data.describe()

# Question 3
median_method = clean_data.groupby('method')['orbital_period'].median()
print(f"\nMedian Oribital Period According to Each Method:\n{median_method}")

# Question 4
mean_discover = clean_data.groupby('year')['number'].mean()
print(f"\nMean Planet Discovery According to Year:\n{mean_discover}")

# Question 5
clean_data['decade'] = (clean_data['year'] // 10) * 10
bool_mask = clean_data['year'] >= 1980
decade_total = clean_data[bool_mask].groupby('decade')['number'].sum()
print(decade_total)
