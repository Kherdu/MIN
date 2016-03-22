# coding=utf-8
import random as ran
import csv
__authors__ = 'rnov, kherdu, redrurm'


myList=[]
keys=[]

def load_csv():
    with open('train.csv', mode='r') as infile:
        reader = csv.reader(infile)

        #reader.next() skips the first line in the .csv that contains the name of each row
        reader.next()
        for i in reader:
            myList.append(i)

    #keys= myList[0]
    #print myList

    return myList



def analyze_data():
    load_csv()
    myDict = dict()
    female = 0.0
    male = 0.0
    total_male = 0.0
    total_female = 0.0
    clas1 = 0.0
    clas2 = 0.0
    clas3 = 0.0
    avg_age = 0.0
    total = 0.0
    young = 0.0
    avg = 0.0
    old = 0.0
    total_young = 0.0
    total_avg = 0.0
    total_old = 0.0
    deads = 0.0
    total_prim = 0.0
    total_terc = 0.0
    total_sec = 0.0

    for i in myList:
        print i[4]
        #for j in i:
        deads += 1


        if i[2] == '1':
            total_prim += 1.0
        elif i[2] == '2':
            total_sec += 1.0
        elif i[2] == '3':
            total_terc += 1.0

        if i[4] == 'male':
            total_male += 1.0
        elif [4] == 'female':
            total_female += 1.0


        if i[5] is not '':
            if float(i[5]) < 18:
                total_young += 1.0
            elif 18 <= float(i[5]) < 35:
                total_avg += 1.0
            elif float(i[5]) >= 35:
                total_old += 1.0


        if i[1] == '1':
            total += 1.0
            if i[2] == '1':
                clas1 += 1.0
            elif i[2] == '2':
                clas2 += 1.0
            elif i[2] == '3':
                clas3 += 1.0

            if i[4] == 'male':
                male += 1.0
            elif [4] == 'female':
                female += 1.0


            if i[5] is not '':
                if float(i[5]) < 18:
                    young += 1.0
                elif 18 <= float(i[5]) < 35:
                    avg += 1.0
                elif float(i[5]) >= 35:
                    old += 1.0

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
    print "Deads: " + str(deads)
    print "Percentage first class: " + str(clas1/total_prim)
    print "Percentage second class: " + str(clas2/total_sec)
    print "Percentage third class: " + str(clas3/total_terc)
    print "Percentage male survivors: " + str(male/total_male)
    print "Percentage female survivors: " + str((1-male/total_male))
    print "Percentage younger than 18: " + str(young/total_young)
    print "Percentage between 18 and 35: " + str(avg/total_avg)
    print "Percentage older than 35: " + str(old/total_old)




    return 0




analyze_data()