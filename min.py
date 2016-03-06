# coding=utf-8
import random as ran
__author__ = 'p45'

# 100 usuarios 1000 productos 10 cat.
# usuarios {usr:list[],..}
#

# ran.randint(0, 1)
#ran.sample(xrange(1, 10), 1)  # category
#ran.sample(xrange(70, 85), 1)  # percentage of the major category


def set_categories():

    category_List = [0]*10
    categoryNum = int(ran.sample(xrange(0, 9), 1).pop())

    # user boughs from 100 to 150 items in several categories
    numItems = int(ran.sample(xrange(100, 150), 1).pop())
    # calculate the number of
    positive_percentage = int(ran.sample(xrange(70, 85), 1).pop())  # % of positives 1's, from 70-85 %
    #positives = int(float(positive_percentage[0]/100.0) * categories_size ) # total 1's in a given range, each cat 100 items
    positives = positive_percentage * numItems / 100
    category_List[categoryNum] = positives
    print "numItems (positive items): {0}".format(numItems)
    print "positives in max category: {0}".format(positives)
    remain_items = numItems - positives
    #print(remain_items)

    # while there are items which aren't been assigned to a cat. and there's still category which hasn't been assigned
    for categoryNum in range(0, 9):
        if category_List[categoryNum] == 0:
            # get random bought items for this category
            num_categ_items = int(ran.sample(xrange(0, remain_items), 1).pop())
            category_List[categoryNum] = num_categ_items
            remain_items -= num_categ_items

    print "category list: {0} = ".format(category_List)
    return category_List


def random_list(positives, category_size):
    """
    positives : number of positives (1's), category_size: length of a category
    """
    bought_list = ran.sample(range(0, category_size), positives)  # position within a list of the positives, 1's
    #print "bought list: {0}".format(bought_list)
    products = [0]*category_size  # initialize list of user's product at 0 (not bought)

    # insert 1's (bought) at the given position
    for i in bought_list:
        products[i] = 1
    '''
    print "products List: "
    print products
    print product.count(0)
    '''
    return products

# the 85% of 150 items max => 128 , the number of users x10 the number of items
category_size = 128
number_users = 12800
user_list = set_categories()  # size of category
#print user_list

# dictionary user_items key : user_name, dictionary user_items values : item_list
user_items = {}
user_name = 'userName'

for i in range(number_users):
    item_list = []
    for category_positive in user_list:
        item_list.append(random_list(category_positive, category_size))
    # add user - categories to the dictionary
    user_items[user_name+str(i)] = item_list

for i in range(number_users):
    print user_items[user_name+str(i)]
"""
total = 0
for k in item_list:
    total += k.count(1)
    print k

print "total positives {0}: ".format(total)
"""

