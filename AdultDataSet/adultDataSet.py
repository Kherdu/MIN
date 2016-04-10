__author__ = 'rnov, kherdu, redrurm'

import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

train_df = pd.read_csv('data.csv', header=0, index_col=0)

# data = read.table("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
#         sep=",",header=F,col.names=c("age", "type_employer", "fnlwgt", "education",
#                 "education_num","marital", "occupation", "relationship", "race","sex",
#                 "capital_gain", "capital_loss", "hr_per_week","country", "income"),
#         fill=FALSE,strip.white=T)


#First we take off education num and fnlwgt (no one knows what fnlwgt is)
train_df.drop = train_df.drop(['education-num', 'fnlwgt', 'relationship'], axis=1)




train_df['workclass'] = train_df['workclass'].map({
    'State-gov':0,
    'Self-emp-not-inc':1,
    'Private':2,
    'Federal-gov': 3,
    'Local-gov': 4,
    'Self-emp-inc': 5,
    'Without-pay': 6,
    'Never-worked': 7
    }
).astype(int)

train_df['sex'] = train_df['sex'].map({'Female': 0, 'Male': 1}).astype(int)


train_df['income'] = train_df['income'].map({'<=50K': 0, '>50K': 1}).astype(int)




train_df['occupation'] = train_df['occupation'].map({
    'Adm-clerical': 0,
    'Craft-repair': 1,
    'Exec-managerial': 2,
    'Farming-fishing': 3,
    'Handlers-cleaners': 4,
    'Machine-op-inspct': 5,
    'Other-service': 6,
    'Priv-house-serv': 7,
    'Prof-specialty': 8,
    'Protective-serv': 9,
    'Sales': 10,
    'Tech-support': 11,
    'Transport-moving': 12,
    'Armed-Forces': 13

}).astype(int)





train_df['native-country'] = train_df['native-country'].map({
    'Cambodia':0,
    'Canada':1,
    'China':2,
    'Columbia':3,
    'Cuba':4,
    'Dominican-Republic':5,
    'Ecuador':6,
    'El-Salvador':7,
    'England':8,
    'France':9,
    'Germany':10,
    'Greece':11,
    'Guatemala':12,
    'Haiti':13,
    'Holand-Netherlands':14,
    'Honduras':15,
    'Hong':16,
    'Hungary':17,
    'India':18,
    'Iran':19,
    'Ireland':20,
    'Italy':21,
    'Jamaica':22,
    'Japan':23,
    'Laos':24,
    'Mexico':25,
    'Nicaragua':26,
    'Outlying-US(Guam-USVI-etc)':27,
    'Peru':28,
    'Philippines':29,
    'Poland':30,
    'Portugal':31,
    'Puerto-Rico':32,
    'Scotland':33,
    'South':34,
    'Taiwan':35,
    'Thailand':36,
    'Trinadad&Tobago':37,
    'United-States':38,
    'Vietnam':39,
    'Yugoslavia':41


}).astype(int)






train_df['education'] = train_df['education'].map({
    '10th':0,
    '11th':1,
    '12th':2,
    '1st-4th':3,
    '5th-6th':4,
    '7th-8th':5,
    '9th':6,
    'Assoc-acdm':7,
    'Assoc-voc':8,
    'Bachelors':9,
    'Doctorate':10,
    'HS-grad':11,
    'Masters':12,
    'Preschool':13,
    'Prof-school':14,
    'Some-college':15

}).astype(int)


train_df['race'] = train_df['race'].map({
    'White': 0,
    'Black': 1,
    'Amer-Indian-Eskimo': 2,
    'Asian-Pac-Islander': 3,
    'Other': 4

}).astype(int)


train_df['marital-status'] = train_df['marital-status'].map({
    'Never-married':0,
    'Married-civ-spouse': 1,
    'Divorced': 2,
    'Married-spouse-absent': 3,
    'Separated': 4,
    'Married-AF-spouse': 5,
    'Widowed': 6


}).astype(int)





# TEST DATA
test_df = pd.read_csv('test.csv', header=0, index_col=0)        # Load the test file into a dataframe

print test_df


test_df.drop = test_df.drop(['education-num', 'fnlwgt', 'relationship'], axis = 1)


test_df['workclass'] = test_df['workclass'].map({
    'State-gov':0,
    'Self-emp-not-inc':1,
    'Private':2,
    'Federal-gov': 3,
    'Local-gov': 4,
    'Self-emp-inc': 5,
    'Without-pay': 6,
    'Never-worked': 7,
    'None': 8
    }
).astype(int)

test_df['sex'] = test_df['sex'].map({'Female': 0, 'Male': 1}).astype(int)







test_df['occupation'] = test_df['occupation'].map({
    'Adm-clerical': 0,
    'Craft-repair': 1,
    'Exec-managerial': 2,
    'Farming-fishing': 3,
    'Handlers-cleaners': 4,
    'Machine-op-inspct': 5,
    'Other-service': 6,
    'Priv-house-serv': 7,
    'Prof-specialty': 8,
    'Protective-serv': 9,
    'Sales': 10,
    'Tech-support': 11,
    'Transport-moving': 12,
    'Armed-Forces': 13,
    'None': 14

}).astype(int)





test_df['native-country'] = test_df['native-country'].map({
    'Cambodia':0,
    'Canada':1,
    'China':2,
    'Columbia':3,
    'Cuba':4,
    'Dominican-Republic':5,
    'Ecuador':6,
    'El-Salvador':7,
    'England':8,
    'France':9,
    'Germany':10,
    'Greece':11,
    'Guatemala':12,
    'Haiti':13,
    'Holand-Netherlands':14,
    'Honduras':15,
    'Hong':16,
    'Hungary':17,
    'India':18,
    'Iran':19,
    'Ireland':20,
    'Italy':21,
    'Jamaica':22,
    'Japan':23,
    'Laos':24,
    'Mexico':25,
    'Nicaragua':26,
    'Outlying-US(Guam-USVI-etc)':27,
    'Peru':28,
    'Philippines':29,
    'Poland':30,
    'Portugal':31,
    'Puerto-Rico':32,
    'Scotland':33,
    'South':34,
    'Taiwan':35,
    'Thailand':36,
    'Trinadad&Tobago':37,
    'United-States':38,
    'Vietnam':39,
    'Yugoslavia':41,
    'None': 42


}).astype(int)






test_df['education'] = test_df['education'].map({
    '10th':0,
    '11th':1,
    '12th':2,
    '1st-4th':3,
    '5th-6th':4,
    '7th-8th':5,
    '9th':6,
    'Assoc-acdm':7,
    'Assoc-voc':8,
    'Bachelors':9,
    'Doctorate':10,
    'HS-grad':11,
    'Masters':12,
    'Preschool':13,
    'Prof-school':14,
    'Some-college':15

}).astype(int)


test_df['race'] = test_df['race'].map({
    'White': 0,
    'Black': 1,
    'Amer-Indian-Eskimo': 2,
    'Asian-Pac-Islander': 3,
    'Other': 4

}).astype(int)


test_df['marital-status'] = test_df['marital-status'].map({
    'Never-married':0,
    'Married-civ-spouse': 1,
    'Divorced': 2,
    'Married-spouse-absent': 3,
    'Separated': 4,
    'Married-AF-spouse': 5,
    'Widowed': 6


}).astype(int)






# The data is now ready to go. So lets fit to the train, then predict to the test!
# Convert back to a numpy array
train_data = train_df.values
test_data = test_df.values


print 'Training...'
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(train_data[0::, 1::], train_data[0::, 0])

print 'Predicting...'
output = forest.predict(test_data).astype(int)

ids = test_df['PassengerId'].values





predictions_file = open("MINfuckers.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'
