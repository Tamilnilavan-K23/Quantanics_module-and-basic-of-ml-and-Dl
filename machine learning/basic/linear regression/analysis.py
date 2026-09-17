import numpy as np
import pandas as pd

cd=pd.read_csv(r'F:\quantanics\machine learning\dataset\stock_data.csv')

print("dimension:",np.shape(cd))

print("details of dataset:\n",cd.describe())

print("mean of dataset:\n",cd.mean)

print("mode of dataset:\n",cd.mode)

print("median of dataset:\n",cd.median)

print("coorelation of the dataset:\n",cd.corr)






