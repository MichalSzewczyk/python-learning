import matplotlib
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
print(df.groupby(['Name']).aggregate(pd.np.sum).sort_values('Count', ascending=False).head(10))

# 1.7

most_popular_for_all = df.groupby(['Name']).aggregate(pd.np.sum).sort_values('Count', ascending=False).head(10)
most_popular_for_males = df[df.Gender == 'M'].groupby(['Name']).aggregate(pd.np.sum).sort_values('Count',
                                                                                                 ascending=False).head(
    10)
most_popular_for_females = df[df.Gender == 'F'].groupby(['Name']).aggregate(pd.np.sum).sort_values('Count',
                                                                                                   ascending=False).head(
    10)
plt_for_all = most_popular_for_all.plot(y='Count')
plt_for_all.set_xticklabels(most_popular_for_all.index)

plt_for_males = most_popular_for_males.plot(y='Count')
plt_for_males.set_xticklabels(most_popular_for_males.index)

plt_for_females = most_popular_for_females.plot(y='Count')
plt_for_females.set_xticklabels(most_popular_for_females.index)
# plt.show()

# 1.8
grouped = df.groupby(['Name'])
result = len(df.groupby(['Name']).aggregate(pd.np.sum))
print(result)


# 1.9
def name_generator(n):
    c = 0
    while c < n:
        c += 1
        yield df['Name'].sample().iat[0]


for i in name_generator(10):
    print(i)

# 1.10.1
print('Most frequent name: {}'.format(
    df.groupby(['Name']).aggregate(pd.np.sum).sort_values(by='Count', ascending=False).head(1).index[0]))

# 1.10.2
print('Mean: {}'.format(
    df.groupby(['Name']).aggregate(pd.np.sum).sort_values(by='Count', ascending=False).mean()['Count']))
print('Median: {}'.format(
    df.groupby(['Name']).aggregate(pd.np.sum).sort_values(by='Count', ascending=False).median()['Count']))
print('Std: {}'.format(
    df.groupby(['Name']).aggregate(pd.np.sum).sort_values(by='Count', ascending=False).std()['Count']))

# 2.1
df = pd.read_csv('lab11_files/occupation.csv', delimiter='|')

# 2.2
print('First 25 records: \n{}'.format(df.head(25)))

# 2.3
print('First 25 records: \n{}'.format(df.tail(10)))

# 2.4
print('Col number: {}'.format(len(df.columns)))
print('Row number: {}'.format(df.count()[0]))

# 2.5
print('Column names: {}'.format(df.columns.values))

# 2.6
plt.close('all')
print('Number of occupations: {}'.format(len(df.groupby(['occupation']))))

# 2.7
# All
df.groupby(['occupation']).count().plot.pie(y='user_id', autopct='%1.0f%%', figsize=(10, 10))
# Top ten
df.groupby(['occupation']).count().sort_values(by='user_id').head(10).append(
    pd.Series({'Inne': sum(df.groupby(['occupation']).count().sort_values(by='user_id')['user_id'])}),
    ignore_index=True).plot.pie(
    y='user_id',
    autopct='%1.0f%%',
    figsize=(10, 10))
# Top ten with others
top_ten_with_others = df.groupby(['occupation']).count().sort_values(by='user_id', ascending=False).head(10)
top_ten_with_others.loc['Inne'] = df.groupby(['occupation']).count().sort_values(by='user_id', ascending=False).sum()
top_ten_with_others.plot.pie(y='user_id')
# plt.show()

# 2.8
# Ten most popular occupations with males/females
plt.close('all')
males = df[df.gender == 'M'].groupby(['occupation'], as_index=False).count().sort_values(by='occupation',
                                                                                         ascending=False)[
    ['occupation', 'user_id']]
females = df[df.gender == 'F'].groupby(['occupation'], as_index=False).count().sort_values(by='occupation',
                                                                                           ascending=False)[
    ['occupation', 'user_id']]
males_and_females = pd.merge(males, females, on='occupation')
males_and_females.columns = ['occupation', 'males', 'females']

plt.close('all')

ax = males_and_females[['males', 'females']].plot(kind='bar')
ax.set_xticklabels(males_and_females.occupation)
# plt.show()

# 2.9
average_age = df.groupby(['occupation'], as_index=False).aggregate(pd.np.average)[['occupation', 'age']]
t = average_age.plot(figsize=(30, 5))
t.set_xticklabels(average_age['occupation'], rotation=90)
plt.show()
