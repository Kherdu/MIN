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
	'None': 2

	
	
}).astype(int)

    return data

def sexDataMap(data):
    data['sex']=data['sex'].map({'Female': 0, 'Male': 1}).astype(int)
    return data

def occupationDataMap(data):

    data['occupation'] = data['occupation'].map({
	# 0 -> 
	# 
        'Exec-managerial': 0,
        'Prof-specialty': 0,
        'Tech-support': 3,
        'Adm-clerical': 3,
        'Craft-repair': 3,
        'Farming-fishing': 3,
        'Handlers-cleaners': 3,
        'Machine-op-inspct':3,
        'Other-service': 3,
        'Priv-house-serv': 3,
        'Protective-serv': 3,
        'Sales': 3,
        'Transport-moving': 3,
        'Armed-Forces':3,
        'None': 3
    }).astype(int)
    return data

def nativeCountryDataMap(data):
	# europe -> 3
	# north-America -> 4
	# afrika -> 0
	# south-america -> 0
	# asia -> 0
	data['native-country'] = data['native-country'].map({
		'Cambodia':0,
		'Canada':4,
		'China':0,
		'Columbia':0,
		'Cuba':0,
		'Dominican-Republic':0,
		'Ecuador':0,
		'El-Salvador':0,
		'England':3,
		'France':3,
		'Germany':3,
		'Greece':2,
		'Guatemala':0,
		'Haiti':0,
		'Holand-Netherlands':3,
		'Honduras':0,
		'Hong':3,
		'Hungary':2,
		'India':0,
		'Iran':0,
		'Ireland':2,
		'Italy':2,
		'Jamaica':0,
		'Japan':3,
		'Laos':0,
		'Mexico':0,
		'Nicaragua':0,
		'Outlying-US(Guam-USVI-etc)':0,
		'Peru':0,
		'Philippines':0,
		'Poland':2,
		'Portugal':2,
		'Puerto-Rico':1,
		'Scotland':2,
		'South':0,
		'Taiwan':0,
		'Thailand':0,
		'Trinadad&Tobago':0,
		'United-States':4,
		'Vietnam':0,
		'Yugoslavia':2,
		'None': 4 #lo pasamos a USA porque el 90% son usa
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
	'Preschool':0,
	'HS-grad':4,
	'Bachelors':2,
	'Prof-school':1,
        'Assoc-acdm':3,
        'Assoc-voc':3,
        'Some-college':4,
        'Doctorate':5,
        'Masters':6
         
        
    }).astype(int)
    return data

def raceDataMap(data):

    data['race'] = data['race'].map({
        'White': 1,
        'Black': 4,
        'Amer-Indian-Eskimo': 2,
        'Asian-Pac-Islander': 2,
        'Other': 1
    }).astype(int)
    return data

def maritalStatusDataMap(data):

    data['marital-status'] = data['marital-status'].map({
        'Never-married': 1,
        'Married-civ-spouse': 4,
        'Divorced': 4,
        'Married-spouse-absent': 4,
        'Separated': 4,
        'Married-AF-spouse': 4,
        'Widowed': 1
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

#train_df['prueba'] = train_df['capital-gain'] - train_df['capital-loss']
#test_df['prueba'] = test_df['capital-gain'] - test_df['capital-loss']


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
