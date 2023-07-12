import numpy as np
import pandas as pd
# Index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
higher_index = list(zip(outside, inside))
print(higher_index)
higher_index = pd.MultiIndex.from_tuples(higher_index)
print(higher_index)
data = np.random.randn(6, 2)
# create multi index data frame
df = pd.DataFrame(data=data, index=higher_index, columns=['A', 'B'])
print(df)
# exact value fetch
print(df.loc['G1'].loc[1]['B'])
# giving index names
df.index.names = ['Outer', 'Inner']
# column fetch
print(df['A'])
# return cross-section from data frame
print(df.xs(1, level='Inner'))
