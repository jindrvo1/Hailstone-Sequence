import pandas as pd
import numpy as np


def hailstone(n):
    res = []
    while n > 1:
        res.append(n)
        n = n/2 if n%2 == 0 else 3*n + 1
    res.append(1)
    return res


# Get unique numbers from the file
unique = np.unique(pd.read_csv('data.csv', header=None).values)


# Calculate the sequences, pad them and output them to a file
pd.DataFrame([hailstone(n) for n in unique], dtype='int64')\
	.fillna(1)\
	.astype('int64')\
	.to_csv('results.csv', index=False, header=False)