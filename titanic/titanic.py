# coding=utf-8
import random as ran
import csv
__authors__ = 'rnov, kherdu, redrurm'


myList=[]
keys=[]

def load_csv():
    with open('train.csv', mode='r') as infile:
        reader = csv.reader(infile)

        reader.next()
        for i in reader:
            myList.append(i)

    #keys= myList[0]
    #print myList

    return myList

def analyze_data():
    load_csv()
    myDict = dict()
    female = 0
    male = 0
    clas1 = 0
    clas2 = 0
    clas3 = 0
    avg_age = 0
    total = 0
    young = 0
    avg = 0
    old = 0

    for i in myList:
        print i[4]
        #for j in i:
        if i[1] == '1':
            total += 1
            if i[2] == '1':
                clas1 += 1
            elif i[2] == '2':
                clas2 += 1
            elif i[2] == '3':
                clas3 += 1

            if i[4] == 'male':
                male += 1
            elif [4] == 'female':
                female += 1


            if i[5] is not '':
                if float(i[5]) < 18:
                    young += 1
                elif 18 <= float(i[5]) < 35:
                    avg += 1
                elif float(i[5]) >= 35:
                    old += 1

                print i[5]
                avg_age = (float(i[5]) + avg_age) / 2

    print "Total survivors: " + str(total)
    print "Total male survivors: " + str(male)
    print "Total female survivors: " + str(total - male)
    print "Total class 1 survivors: " + str(clas1)
    print "Total class 2 survivors: " + str(clas2)
    print "Total class 3 survivors: " + str(clas3)
    print "Average age survivors: " + str(avg_age)
    print "Yoing survivors: " + str(young)
    print "Average survivors: " + str(avg)
    print "Old survivors: " + str(old)




    return 0




analyze_data()