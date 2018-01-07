import pandas as pd
import matplotlib.pyplot as plt

# ex1
# 1.1
df = pd.read_csv('lab11_files/US_Baby_Names_right.csv')
print(df.dtypes)

# 1.2
print(len(df.index))

# 1.3
print(df[0:10])

# 1.4
del df['Unnamed: 0']
del df['Id']
print(df)

# 1.5
print(
    'Number of females: {}, and number of males: {}'.format(len(df[df.Gender == 'F']), len(df[df.Gender == 'M'])))

# 1.6
print(df.groupby(['Name']).size().reset_index(name='count').sort_values('count', ascending=False).head(10))

# 1.7

most_popular_for_all = df.groupby(['Name']).size().reset_index(
    name='count').sort_values('count', ascending=False).head(
    10)
most_popular_for_males = df[df.Gender == 'M'].groupby(['Name']).size().reset_index(name='count').sort_values('count',
                                                                                                             ascending=False).head(
    10)
most_popular_for_females = df[df.Gender == 'F'].groupby(['Name']).size().reset_index(name='count').sort_values('count',
                                                                                                               ascending=False).head(
    10)
print(df[df.Name == 'Elizabeth'].groupby(['Name']).size().reset_index(name='count').sort_values('count',
                                                                                                ascending=False).head(
    10))
plt_for_all = most_popular_for_all.plot(x='Name', y='count')
plt_for_all.set_xticklabels(most_popular_for_all.Name)

plt_for_males = most_popular_for_males.plot(x='Name', y='count')
plt_for_males.set_xticklabels(most_popular_for_males.Name)

plt_for_females = most_popular_for_females.plot(x='Name', y='count')
plt_for_females.set_xticklabels(most_popular_for_females.Name)

# plt.show()

# 1.8
print(df.groupby(['Name']))
