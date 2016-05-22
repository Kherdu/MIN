__author__ = 'rnov, Kherdu'
import pandas as pd
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn import cross_validation


# read data from file. csv
train_df = pd.read_csv('allData.csv', header=0)     # Load the train file into a dataframe

# 'nombre' is useless for learning
train_df = train_df.drop(['nombre'], axis=1)

# translate operations (+,-,/,*) from str to int
train_df['op'] = train_df['op'].map({'+': 1, '-': 1, '/': 1, '*': 4}).astype(int)

# add new feature that measures the operation weight
train_df['complexity'] = (train_df['op1'] + train_df['op2']) * train_df['op']

# get the values
train_data = train_df.values

#print train_data[0]
#print train_data[0::, [0, 1, 2, 4]][0]
#print train_data[0:, 3][0]


print 'Training cross validation'
# using linear model for learning, since target are numbers (continuous)

#clf = linear_model.Ridge(alpha=1)
clf = linear_model.LinearRegression()
# apply cross validation
scores = cross_validation.cross_val_score(clf, train_data[0::, [0, 1, 2, 4]], train_data[0:, 3], scoring='mean_absolute_error', cv=10)

print scores
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print 'mean score is: {}'.format(scores.mean())
print 'standard deviation score is: {}'.format(scores.std()*2)


# entrenar
clf.fit(train_data[0::, [0, 1, 2, 4]], train_data[0:, 3])

#print type(train_data)
for i in range(0, 10):
    k = train_data[0::, [0, 1, 2, 4]][i]
    k = k.reshape(1, -1)
    print 'for operation {0} ,prediction is : {1}'.format(k, clf.predict(k)[0])

# save the model trained model
joblib.dump(clf, 'operations.pkl')

# sources: http://scikit-learn.org/stable/modules/linear_model.html
# http://scikit-learn.org/stable/modules/cross_validation.html
# http://scikit-learn.org/stable/modules/model_persistence.html