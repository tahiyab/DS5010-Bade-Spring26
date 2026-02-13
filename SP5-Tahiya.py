import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Problem_Set_5/planets.csv')
clean_data = data.dropna()

# Question 1
yearly_planets = clean_data.groupby('year')['number'].sum()
print(f"Total planets discovered each year:\n{yearly_planets}")

yearly_planets.plot(
    kind='line', 
    figsize=(10, 6), 
    grid=True, 
    title='Total Planets Discovered per Year',
    xlabel='Year of Discovery',
    ylabel='Number of Planets'
    )
plt.legend()
plt.show()

# Question 2
method_planets = clean_data.groupby('method')['number'].sum()
print(f"\nTotal planets discovered by each method:\n{method_planets}")

method_planets.plot(
    kind='bar', 
    figsize=(12, 6), 
    grid=True, 
    title='Total Planets Discovered by Method',
    label='Planets Found'
    xlabel = 'Discovery Method'
    ylabel = 'Number of Planets'
)

plt.legend()
plt.show()
