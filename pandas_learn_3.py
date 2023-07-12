# missing data
import numpy as np
import pandas as pd
# d = pd.DataFrame(data=[[1, 5, 1], [2, np.nan, 2], [np.nan, np.nan, 3]], index=[0, 1, 2], columns=['A', 'B', 'C'])
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
# drop na columns with 2 or more Nan values
df.dropna(axis=1, inplace=True, thresh=2)
print(df)
# fill na
df.fillna(value='Fill Value', inplace=True)
print(df)
# fill value with mean of the column
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
df['A'].fillna(value=df['A'].mean(), inplace=True)
df['B'].fillna(value=df['B'].mean(), inplace=True)
print(df)
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)
df1 = df.groupby('Company')
# can use min() max() count() std() as well
print(df1)
print(df1.mean())
print(df1.describe().transpose()['MSFT'])
