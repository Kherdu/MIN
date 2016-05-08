__author__ = 'rnov'
import pandas as pd
from sklearn import linear_model
from sklearn.externals import joblib
import numpy as np

# read data from file. csv
train_df = pd.read_csv('allData.csv', header=0)     # Load the train file into a dataframe

# translate operations (+,-,/,*) from str to int
train_df['op'] = train_df['op'].map({'+': 0, '-': 1, '/': 2, '*': 4}).astype(int)

# 'nombre' is useless for learning
train_df = train_df.drop(['nombre'], axis=1)
# get the values
train_data = train_df.values

# print train_data[0::, :3:]  # from line 0 to end, gets all columns until 3th one
# print train_data[0::, 3]  # from line 0 to end, gets just the 3th column

print 'Training...'
# using linear model (regression, ridge, with multiple variables)for learning, since target are numbers (continuous)
#clf = linear_model.Ridge(alpha=.5)
clf = linear_model.LinearRegression()
clf.fit(train_data[0::, :3:], train_data[0::, 3])

# save the trained model,
joblib.dump(clf, 'operations.pkl')

#"""""
# shows attributes's type
print type(train_df['op'][2])
print type(train_df['op1'][2])
print type(train_df['op2'][2])
print type(train_df['tiempo'][2])
#print train_df
#"""

# sources: http://scikit-learn.org/stable/modules/linear_model.html
# http://scikit-learn.org/stable/modules/model_persistence.html