import numpy as np
import pandas as pd
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}
print(pd.Series(data=my_data, index=labels))
ser1 = pd.Series(data=[3, 1, 4, 2], index=['USA', 'Germany', 'Italy', 'Japan'])
ser2 = pd.Series(data=[2, 5, 1, 3], index=['USA', 'India', 'Italy', 'Japan'])
print(ser1 + ser2)
print(ser1['USA'])
np.random.seed(101)
data_frame = pd.DataFrame(data=np.random.randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
print(data_frame)
print(data_frame['W'])
data_frame['new'] = data_frame['X'] + data_frame['Z']
print(data_frame['new'])
print(data_frame)
# delete column
data_frame.drop('new', axis=1, inplace=True)
print(data_frame)
# delete row
data_frame.drop('E', axis=0, inplace=True)
print(data_frame)
# grabbing column
print(data_frame[['X', 'Y']])
# grabbing row
print(data_frame.loc['A'])
# or
print(data_frame.iloc[0])
print(data_frame.loc['B']['Y'])
# fetch subset for data frame
print(data_frame.loc[['A', 'B']][['W', 'Y']])
# conditions on a data frame
print(data_frame[data_frame > 0.5])
# passing in a series like below we don't get the Nan lines
print(data_frame[data_frame['W'] > 0])
# directly fetching 1 or more columns from the filtered data frame
print(data_frame[data_frame['W'] > 0][['X', 'Y']])
# multiple conditions to data frame
print(data_frame[(data_frame['X'] > 0) & (data_frame['Y'] > 0)])
# reset the index to be included as a column inplace is False to not make the change permanent change if needed
print(data_frame.reset_index(inplace=False))
print(data_frame)
country = 'UK US IND AUS'.split(' ')
print(country)
data_frame['Country'] = country
print(data_frame)
data_frame.set_index('Country', inplace=True)
print(data_frame)
