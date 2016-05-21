__author__ = 'rnov, Kherdu'
import pandas as pd
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn import cross_validation
from sklearn import svm
import numpy as np

# read data from file. csv
train_df = pd.read_csv('allData.csv', header=0)     # Load the train file into a dataframe

# translate operations (+,-,/,*) from str to int
train_df['op'] = train_df['op'].map({'+': 0, '-': 0, '/': 1, '*': 2}).astype(int)

#train_df['complexity'] = train_df['complexity'].map(len(train_df['op1'])>1 and len(train_df['op2'])> 1 : 15 ) #0 #por defecto complejidad 0 para todos


# 'nombre' is useless for learning
train_df = train_df.drop(['nombre'], axis=1)
train_df['complexity'] = 0

for c in range(0, len(train_df)):
    if train_df.op[c] == 2:  #mul
        if train_df.op1[c] > 9 and train_df.op2[c] > 9:
            train_df['complexity'][c] = 3
        else:
            train_df['complexity'][c] = 2
    elif train_df.op[c] == 1:  #div
        if train_df.op1[c] > train_df.op2[c]:
            train_df['complexity'] = 1

    elif train_df.op[c] == 0 and train_df.op1[c] > 9 and train_df.op2[c] > 9:  #suma y resta
        train_df['complexity'][c] = 1
# get the values
train_data = train_df.values
# print train_data[0::, :3:]  # from line 0 to end, gets all columns until 3th one
# print train_data[0::, 3]  # from line 0 to end, gets just the 3th column
train_data = np.roll(train_data, 2) #si se meten mas varibles aumentar este numero

print 'Training...'
# using linear model (regression, ridge, with multiple variables)for learning, since target are numbers (continuous)
#clf = linear_model.Ridge(alpha=.5)
clf = linear_model.LinearRegression()
#data[:, [1, 9]] selecciona las columnas 1 y 9
#clf.fit(train_data[0::, :3:], train_data[0::, 3])

scores = cross_validation.cross_val_score(clf, train_data[0::, 1::], train_data[0:, 0], scoring='mean_absolute_error', cv = 10)

print scores
print 'max score is: {}'.format(max(scores))
print 'mean score is: {}'.format(scores.mean())
print 'standard deviation score is: {}'.format(scores.std()*2)

# save the trained model,
#joblib.dump(clf, 'operations.pkl')

"""
# shows attributes's type
print type(train_df['op'][2])
print type(train_df['op1'][2])
print type(train_df['op2'][2])
print type(train_df['tiempo'][2])
#print train_df
"""

# sources: http://scikit-learn.org/stable/modules/linear_model.html
# http://scikit-learn.org/stable/modules/cross_validation.html
# http://scikit-learn.org/stable/modules/model_persistence.html