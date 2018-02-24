import pandas as pd
from tabulate import tabulate


a = pd.read_csv("events.csv", index_col=0)
print(tabulate(a.iloc[::-1]))
