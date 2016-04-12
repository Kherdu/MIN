__author__ = 'rnov, kherdu, redrurm'

import pandas as pd
import numpy as np
import csv as csv
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
t0 = time.clock()

train_df = pd.read_csv('data.csv', header=0)

# data = read.table("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
#         sep=",",header=F,col.names=c("age", "type_employer", "fnlwgt", "education",
#                 "education_num","marital", "occupation", "relationship", "race","sex",
#                 "capital_gain", "capital_loss", "hr_per_week","country", "income"),
#         fill=FALSE,strip.white=T)


#First we take off education num and fnlwgt (no one knows what fnlwgt is)

def workClassDataMap(data):
    data['workclass'] = data['workclass'].map({
        'State-gov': 0,
        'Self-emp-not-inc': 1,
        'Private': 2,
        'Federal-gov': 3,
        'Local-gov': 0,
        'Self-emp-inc': 1,
        'Without-pay': 4,
        'Never-worked': 4,
        'None': 2 #none lo pasamos a la misma clase que privado porque sabemos que hay un 68% de trabajadores del sector privado, asique es el mas probable.
    }).astype(int)

    return data

def sexDataMap(data):
    data['sex']=data['sex'].map({'Female': 0, 'Male': 1}).astype(int)
    return data

def occupationDataMap(data):

    data['occupation'] = data['occupation'].map({

        'Exec-managerial': 0,
        'Prof-specialty': 0,
        'Tech-support': 3,
        'Adm-clerical': 3,
        'Craft-repair': 1,
        'Farming-fishing': 4,
        'Handlers-cleaners': 2,
        'Machine-op-inspct': 1,
        'Other-service': 4,
        'Priv-house-serv': 2,
        'Protective-serv': 4,
        'Sales': 1,
        'Transport-moving': 3,
        'Armed-Forces': 2,
        'None': 4
    }).astype(int)
    return data

def nativeCountryDataMap(data):
    data['native-country'] = data['native-country'].map({
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
        'None': 8 #lo pasamos a USA porque el 90% son usa
    }).astype(int)
    return data

def educationDataMap(data):
    data['education'] = data['education'].map({
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
    return data

def raceDataMap(data):

    data['race'] = data['race'].map({
        'White': 1,
        'Black': 2,
        'Amer-Indian-Eskimo': 3,
        'Asian-Pac-Islander': 4,
        'Other': 0
    }).astype(int)
    return data

def maritalStatusDataMap(data):

    data['marital-status'] = data['marital-status'].map({
        'Never-married': 1,
        'Married-civ-spouse': 2,
        'Divorced': 3,
        'Married-spouse-absent': 3,
        'Separated': 3,
        'Married-AF-spouse': 2,
        'Widowed': 4
    }).astype(int)
    return data

def marital_statMap(data):

    if data['capital-gain'].any() >= 5095.5 and data['capital-loss'].any() > 1782.5 and data['hours-per-week'].any() > 41.5 and \
                    data['occupation'].any() == 'Prof-specialty' and data['age'].any() > 34.5 and data['education'].any() == 'Bachelors' and \
                    data['marital-status'].any() == 'Married-civ-spouse':
        data['mar-stat'] = 1
    else:
        data['mar-stat'] = 0
    return data


#training data preparation
train_df = workClassDataMap(train_df)
train_df = sexDataMap(train_df)
train_df = occupationDataMap(train_df)
train_df = nativeCountryDataMap(train_df)
train_df = educationDataMap(train_df)
train_df = raceDataMap(train_df)
train_df = maritalStatusDataMap(train_df)
#train_df = marital_statMap(train_df)
train_df['income'] = train_df['income'].map({'<=50K': 0, '>50K': 1}).astype(int)
train_df = train_df.drop(['education-num', 'fnlwgt', 'relationship', 'Unnamed: 0'], axis=1)



# TEST DATA
test_df = pd.read_csv('test.csv', header=0)        # Load the test file into a dataframe


#test data preparation
test_df = workClassDataMap(test_df)
test_df = sexDataMap(test_df)
test_df = occupationDataMap(test_df)
test_df = nativeCountryDataMap(test_df)
test_df = educationDataMap(test_df)
test_df = raceDataMap(test_df)
test_df = maritalStatusDataMap(test_df)
#test_df = marital_statMap(test_df)
test_df = test_df.drop(['education-num', 'fnlwgt', 'relationship', 'Unnamed: 0'], axis = 1)

# The data is now ready to go. So lets fit to the train, then predict to the test!
# Convert back to a numpy array
train_data = train_df.values
test_data = test_df.values

print 'Training...'
forest = RandomForestClassifier(n_estimators=100, n_jobs=2) #2 hilos

forest.fit(train_data[0:, :11], train_data[0:, 11])

print 'Predicting...'
output = forest.predict(test_data).astype(int)
predictions_file = open("RafaelCaturla.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerows(zip(output))
predictions_file.close()


#comprobacion con data
alg= LogisticRegression(random_state=1)
scores= cross_validation.cross_val_score(alg, train_data[0:, :11], train_df['income'], cv=3)
print scores.mean()


print 'Done.'

print 'end time: ', time.clock() - t0
