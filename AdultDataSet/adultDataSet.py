__author__ = 'rnov, kherdu, redrurm'

import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

train_df = pd.read_csv('data.csv', header=0)

# data = read.table("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
#         sep=",",header=F,col.names=c("age", "type_employer", "fnlwgt", "education",
#                 "education_num","marital", "occupation", "relationship", "race","sex",
#                 "capital_gain", "capital_loss", "hr_per_week","country", "income"),
#         fill=FALSE,strip.white=T)


#First we take off education num and fnlwgt (no one knows what fnlwgt is)

train_df['workclass'] = train_df['workclass'].map({
    'State-gov':0,
    'Self-emp-not-inc':1,
    'Private':2,
    'Federal-gov': 3,
    'Local-gov': 0,
    'Self-emp-inc': 1,
    'Without-pay': 4,
    'Never-worked': 4
    }
).astype(int)

train_df['sex'] = train_df['sex'].map({'Female': 0, 'Male': 1}).astype(int)


train_df['income'] = train_df['income'].map({'<=50K': 0, '>50K': 1}).astype(int)


train_df['occupation'] = train_df['occupation'].map({
    'Adm-clerical': 1,
    'Craft-repair': 2,
    'Exec-managerial': 5,
    'Farming-fishing': 2,
    'Handlers-cleaners': 2,
    'Machine-op-inspct': 2,
    'Other-service': 4,
    'Priv-house-serv': 4,
    'Prof-specialty': 7,
    'Protective-serv': 3,
    'Sales': 6,
    'Tech-support': 3,
    'Transport-moving': 2,
    'Armed-Forces': 0

}).astype(int)


train_df['native-country'] = train_df['native-country'].map({
    'Cambodia':0,
    'Canada':2,
    'China':1,
    'Columbia':3,
    'Cuba':4,
    'Dominican-Republic':5,
    'Ecuador':3,
    'El-Salvador':3,
    'England':2,
    'France':6,
    'Germany':6,
    'Greece':7,
    'Guatemala':5,
    'Haiti':5,
    'Holand-Netherlands':6,
    'Honduras':5,
    'Hong':1,
    'Hungary':7,
    'India':2,
    'Iran':4,
    'Ireland':2,
    'Italy':6,
    'Jamaica':5,
    'Japan':4,
    'Laos':0,
    'Mexico':5,
    'Nicaragua':5,
    'Outlying-US(Guam-USVI-etc)':5,
    'Peru':3,
    'Philippines':0,
    'Poland':7,
    'Portugal':7,
    'Puerto-Rico':5,
    'Scotland':2,
    'South':7,
    'Taiwan':1,
    'Thailand':0,
    'Trinadad&Tobago':5,
    'United-States':8,
    'Vietnam':0,
    'Yugoslavia':7


}).astype(int)


train_df['education'] = train_df['education'].map({
    '10th':0,
    '11th':0,
    '12th':0,
    '1st-4th':0,
    '5th-6th':0,
    '7th-8th':0,
    '9th':0,
    'Assoc-acdm':3,
    'Assoc-voc':3,
    'Bachelors':2,
    'Doctorate':5,
    'HS-grad':4,
    'Masters':6,
    'Preschool':0,
    'Prof-school':1,
    'Some-college':4

}).astype(int)


train_df['race'] = train_df['race'].map({
    'White': 1,
    'Black': 2,
    'Amer-Indian-Eskimo': 3,
    'Asian-Pac-Islander': 4,
    'Other': 0
}).astype(int)


train_df['marital-status'] = train_df['marital-status'].map({
    'Never-married': 1,
    'Married-civ-spouse': 2,
    'Divorced': 3,
    'Married-spouse-absent': 3,
    'Separated': 3,
    'Married-AF-spouse': 2,
    'Widowed': 4


}).astype(int)


train_df = train_df.drop(['education-num', 'fnlwgt', 'relationship'], axis=1)


# TEST DATA
test_df = pd.read_csv('test.csv', header=0)        # Load the test file into a dataframe

print test_df


test_df = test_df.drop(['education-num', 'fnlwgt', 'relationship'], axis = 1)


test_df['workclass'] = test_df['workclass'].map({
    'State-gov': 0,
    'Self-emp-not-inc': 1,
    'Private': 2,
    'Federal-gov': 3,
    'Local-gov': 0,
    'Self-emp-inc': 1,
    'Without-pay': 4,
    'Never-worked': 4,
    'None': 5
}).astype(int)

test_df['sex'] = test_df['sex'].map({'Female': 0, 'Male': 1}).astype(int)


test_df['occupation'] = test_df['occupation'].map({
     'Adm-clerical': 1,
    'Craft-repair': 2,
    'Exec-managerial': 5,
    'Farming-fishing': 2,
    'Handlers-cleaners': 2,
    'Machine-op-inspct': 2,
    'Other-service': 4,
    'Priv-house-serv': 4,
    'Prof-specialty': 7,
    'Protective-serv': 3,
    'Sales': 6,
    'Tech-support': 3,
    'Transport-moving': 2,
    'Armed-Forces': 0,
    'None': 8

}).astype(int)


test_df['native-country'] = test_df['native-country'].map({
  'Cambodia':0,
    'Canada':2,
    'China':1,
    'Columbia':3,
    'Cuba':4,
    'Dominican-Republic':5,
    'Ecuador':3,
    'El-Salvador':3,
    'England':2,
    'France':6,
    'Germany':6,
    'Greece':7,
    'Guatemala':5,
    'Haiti':5,
    'Holand-Netherlands':6,
    'Honduras':5,
    'Hong':1,
    'Hungary':7,
    'India':2,
    'Iran':4,
    'Ireland':2,
    'Italy':6,
    'Jamaica':5,
    'Japan':4,
    'Laos':0,
    'Mexico':5,
    'Nicaragua':5,
    'Outlying-US(Guam-USVI-etc)':5,
    'Peru':3,
    'Philippines':0,
    'Poland':7,
    'Portugal':7,
    'Puerto-Rico':5,
    'Scotland':2,
    'South':7,
    'Taiwan':1,
    'Thailand':0,
    'Trinadad&Tobago':5,
    'United-States':8,
    'Vietnam':0,
    'Yugoslavia':7,
    'None': 9


}).astype(int)


test_df['education'] = test_df['education'].map({
   '10th':0,
    '11th':0,
    '12th':0,
    '1st-4th':0,
    '5th-6th':0,
    '7th-8th':0,
    '9th':0,
    'Assoc-acdm':3,
    'Assoc-voc':3,
    'Bachelors':2,
    'Doctorate':5,
    'HS-grad':4,
    'Masters':6,
    'Preschool':0,
    'Prof-school':1,
    'Some-college':4

}).astype(int)


test_df['race'] = test_df['race'].map({
   'White': 1,
    'Black': 2,
    'Amer-Indian-Eskimo': 3,
    'Asian-Pac-Islander': 4,
    'Other': 0
}).astype(int)


test_df['marital-status'] = test_df['marital-status'].map({
    'Never-married': 1,
    'Married-civ-spouse': 2,
    'Divorced': 3,
    'Married-spouse-absent': 3,
    'Separated': 3,
    'Married-AF-spouse': 2,
    'Widowed': 4


}).astype(int)


ids = test_df['Unnamed: 0'].values
# The data is now ready to go. So lets fit to the train, then predict to the test!
# Convert back to a numpy array
train_data = train_df.values
test_data = test_df.values

print 'Training...'
forest = RandomForestClassifier(n_estimators=100, n_jobs=4) #4 hilos
forest.fit(train_data[0::, 1::], train_data[0::, 12])

print 'Predicting...'
output = forest.predict(test_data).astype(int)


predictions_file = open("ShoddyCoders.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerows(zip(output))
predictions_file.close()
print 'Done.'
