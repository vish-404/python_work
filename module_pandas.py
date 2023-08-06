import numpy as np  # numpy is written in c
import pandas as pd

# pandas is a open source data analysis library written in python 
# highly robust data operations
# uses speed of numpy to make data analysis and preprocessing  easy 

dict1 = {
    "name" : ["A" , "b", "c", "d"],
    "marks" : [10, 20, 30, 15],
    "subject" : ["x", "y", "z", "zx"]

}

dp1 = pd.DataFrame(dict1)
print(dp1)

# dp1.to_csv("data.csv")  to make a csv sheet (spread sheet) of data
# dp1.to_csv("data.csv", index= False)  to avoid index in data sheet 

print(dp1.head(2), "\n\n", dp1.tail(1), "\n")

print(dp1["marks"][1])

print(dp1.describe())

# variable = pd.read_csv("csv_file.csv")

sr = pd.Series(np.random.rand(34))
print(sr, type(sr)) 

newd = pd.DataFrame(np.random.rand(34, 5), index= np.arange(34))
print(newd, "\n", newd.index)
print(newd.to_numpy())
print("\n\n", newd.T) # transpose
#  nedf.copy()  to make copy

print(newd.drop(4))