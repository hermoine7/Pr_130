import pandas as pd
import csv

df=pd.read_csv('final.csv')
print(df.shape)

del df["Luminosity"]

print(df.shape)
print(list(df))

df.to_csv("main.csv")