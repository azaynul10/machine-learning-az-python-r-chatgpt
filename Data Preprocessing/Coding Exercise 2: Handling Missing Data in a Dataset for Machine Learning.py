# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
dataset=pd.read_csv('pima-indians-diabetes.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
# Identify missing data (assumes that missing data is represented as NaN)
print(dataset)
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(X[:,1:3])
# Print the number of missing entries in each column
X[:,1:3]=imputer.transform(X[:,1:3])
