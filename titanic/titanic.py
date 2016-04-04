__author__ = 'rnov, kherdu, redrurm'

import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

# Data cleanup
# TRAIN DATA
train_df = pd.read_csv('train.csv', header=0)        # Load the train file into a dataframe

# I need to convert all strings to integer classifiers.
# I need to fill in the missing values of the data and make it complete.
# ------------------------------------------------------------------------

# str to int -> female = 0, Male = 1
train_df['Gender'] = train_df['Sex'].map({'female': 0, 'male': 1}).astype(int)
train_df['Gender2'] = np.int32(train_df['Sex'].map({'female': 0, 'male': 1}).astype(int) + (train_df.Pclass*2))
train_df['family'] = np.int32(train_df.Age - train_df['Parch'])



#train_df['Age*Class'] = np.int32(train_df.Age * train_df.Pclass)
#train_df['rich'] = np.int32(train_df['Fare'] / train_df.Pclass)
#train_df['woman_luck'] = np.int32(train_df['Gender']*3 + train_df.Pclass)

#print train_df['fare']

# Not relevant the embarked port, no need to fill the missing though
# Embarked from 'C', 'Q', 'S'
# Note this is not ideal: in translating categories to numbers, Port "2" is not 2 times greater than Port "1", etc.








Names = list(enumerate(np.unique(train_df['Name'])))
Names2 = []

for i in Names:
    if "Master." in i[1]:
        i[1] = 0
        #Names2.append(0)
    elif "Rev." in i[1]:
        i[1] = 1
    elif "Mr." in i[1]:
        i[1] = 2
    elif "Mrs.." in i[1]:
        i[1] = 3
    elif "Miss." in i[1]:
        i[1] = 4
print Names2
#Names_dict = {name2: i for i, name2 in Names2}


train_df['Name'] = train_df['Name'].map(lambda y: Names2[y]).astype(int)





# All missing Embarked -> just make them embark from most common place
if len(train_df.Embarked[train_df.Embarked.isnull()]) > 0:
    train_df.Embarked[train_df.Embarked.isnull()] = train_df.Embarked.dropna().mode().values

Ports = list(enumerate(np.unique(train_df['Embarked'])))    # determine all values of Embarked,
Ports_dict = {name: i for i, name in Ports}              # set up a dictionary in the form  Ports : index
train_df.Embarked = train_df.Embarked.map(lambda x: Ports_dict[x]).astype(int)     # Convert all Embark strings to int




# All the ages with no data -> make the median of all Ages, la edad media para hombres y para mujeres
median_age = train_df['Age'].dropna().median()
if len(train_df.Age[train_df.Age.isnull()]) > 0:
    train_df.loc[(train_df.Age.isnull()), 'Age'] = median_age

# Remove the Name column, Cabin, Ticket, Embarked, Fare,and Sex (since I copied and filled it to Gender)
train_df = train_df.drop(['Sex', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
print train_df.dtypes

# TEST DATA
test_df = pd.read_csv('test.csv', header=0)        # Load the test file into a dataframe

# I need to do the same with the test data now, so that the columns are the same as the training data
# I need to convert all strings to integer classifiers:
# female = 0, Male = 1
#test_df['Gender'] = test_df['Sex'].map({'female': 0, 'male': 1}).astype(int)
test_df['Gender'] = test_df['Sex'].map({'female': 0, 'male': 1}).astype(int)
test_df['Gender2'] = np.int32(test_df['Sex'].map({'female': 0, 'male': 1}).astype(int) + (test_df.Pclass*2))

#test_df['family'] = test_df['Parch'] + test_df['SibSp'] - test_df['Gender']
test_df['family'] = np.int32(test_df.Age - test_df['Parch'])


#test_df['Age*Pclass'] = np.int32(test_df.Age * test_df.Pclass)
#test_df['woman_luck'] = np.int32(test_df['Gender']*3 + test_df.Pclass)
#print test_df.Pclass
#print test_df['age']

# Embarked from 'C', 'Q', 'S'
# All missing Embarked -> just make them embark from most common place
if len(test_df.Embarked[test_df.Embarked.isnull() ]) > 0:
    test_df.Embarked[test_df.Embarked.isnull() ] = test_df.Embarked.dropna().mode().values
# Again convert all Embarked strings to int
test_df.Embarked = test_df.Embarked.map( lambda x: Ports_dict[x]).astype(int)



Names = list(enumerate(np.unique(test_df['Name'])))
Names2 = []

for i in Names:
    if "Master." in i:
        Names2.append(0)
    elif "Rev." in i:
        Names2.append(1)
    elif "Mr." in i:
        Names2.append(2)
    elif "Mrs.." in i:
        Names2.append(3)
    elif "Miss." in i:
        Names2.append(4)

Names_dict = {name2: i for i, name2 in Names2}
#test_df.Name = test_df.Name.map(lambda x: Names_dict[x]).astype(int)
test_df['Name'] = test_df['Name'].map(lambda y: Names_dict[y]).astype(int)



# All the ages with no data -> make the median of all Ages, la edad media para hombres y para mujeres
median_age = test_df['Age'].dropna().median()
if len(test_df.Age[test_df.Age.isnull()]) > 0:
    test_df.loc[(test_df.Age.isnull()), 'Age'] = median_age


# All the missing Fares -> assume median of their respective class
if len(test_df.Fare[test_df.Fare.isnull()]) > 0:
    median_fare = np.zeros(3)
    for f in range(0, 3):                                              # loop 0 to 2
        median_fare[f] = test_df[test_df.Pclass == f+1]['Fare'].dropna().median()
    for f in range(0, 3):                                              # loop 0 to 2
        test_df.loc[(test_df.Fare.isnull()) & (test_df.Pclass == f+1), 'Fare'] = median_fare[f]


# Collect the test data's PassengerIds before dropping it
ids = test_df['PassengerId'].values
# Remove the Name column, Cabin, Ticket, Embarked, Fare,and Sex (since I copied and filled it to Gender)
test_df = test_df.drop(['Sex', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
print test_df.dtypes

# The data is now ready to go. So lets fit to the train, then predict to the test!
# Convert back to a numpy array
train_data = train_df.values
test_data = test_df.values


print 'Training...'
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(train_data[0::, 1::], train_data[0::, 0])

print 'Predicting...'
output = forest.predict(test_data).astype(int)


predictions_file = open("titanic.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId", "Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'
