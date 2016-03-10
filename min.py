# coding=utf-8
import random as ran
__authors__ = 'rnov, kherdu, redrurm'

num_categories = 10  # nº of categories

category_size = 100  # nº of items per category
number_users = 1000  # nº of users

# dictionary user_items key : user_name, dictionary user_items values : item_list
user_items = {}
user_name = 'userName'

def set_categories(num_categories):
    """
    sets the number of items bought by a single user from each category.
    :param num_categories: nº of categories in the store.
    :return: list with the number of items per category.
    """
    category_List = [0]*num_categories  # list of products for each category
    categoryNum = int(ran.sample(xrange(0, 9), 1).pop())  # nº of categories a user bought products

    numItems = int(ran.sample(xrange(100, 120), 1).pop())  # user boughs from 100 to 120 items from different categories

    # calculate the number of
    positive_percentage = int(ran.sample(xrange(70, 85), 1).pop())  # % of positives 1's, from 70-85 %
    positives = positive_percentage * numItems / 100
    category_List[categoryNum] = positives
    remain_items = numItems - positives

    # while there are items which haven't been assigned to a cat. and there's still category which hasn't been assigned
    for categoryNum in range(0, 9):
        if category_List[categoryNum] == 0:
            # get random bought items for this category
            num_categ_items = int(ran.sample(xrange(0, remain_items), 1).pop())
            category_List[categoryNum] = num_categ_items
            remain_items -= num_categ_items

    return category_List


def random_list(positives, category_size):
    """
    generates random positions in each category for bought products.
    :param positives: number bought items (1's) in a category.
    :param category_size:  length of a category.
    :return: list with the products a user bought from a category.
    """
    bought_list = ran.sample(range(0, category_size), positives)  # position within a list of the positives, 1's
    products = [0]*category_size  # initialize list of user's product at 0 (not bought)

    for i in bought_list:  # insert 1's (bought) at the given position
        products[i] = 1

    return products


def cat_bought(user):
    """
    finds the categories a user has bought item/s
    :param user: user items list
    :return: list with bought items
    """
    categories_bought = [0]*num_categories
    a = 0
    for cat in user:
        if cat.count(1) >= 1:
            categories_bought[a] = 1
        a += 1
    return categories_bought


def compare(userA, userB):
    """
    compares the bought items for each category of two users. 
    :param userA: items first user
    :param userB: items second user
    :return: returns a list which contains the Jaccard ratios for each category. 
    """
    catA = cat_bought(userA)
    catB = cat_bought(userB)
    jaccardIndexes = [0.0]*num_categories
    for i in range(0,num_categories-1):
        if catA[i] == catB[i] and catA[i]==1:
            union = 0.0
            intersection = 0.0
            for j in range(0, category_size):
                union += userA[i][j]
                union += userB[i][j]
                if userA[i][j] == userB[i][j] and userA[i][j] == 1:
                    union -= 1
                    intersection += 1
            jaccardIndexes[i] = intersection/union

    return jaccardIndexes


# generates random items and users.
for i in range(number_users):
    item_list = []
    user_list = set_categories(num_categories)
    for category_positive in user_list:
        item_list.append(random_list(category_positive, category_size))
    # add user - categories to the dictionary
    user_items[user_name+str(i)] = item_list

# compares the Jaccard ratios of a user to each other and if the ratio of one category (the prevailing in general)
# is more than 0.6 prints that its a match
for i in range(number_users):
    for j in range(number_users):
        j += 1  # para comparar el 0 con el 1, 1 con 2... etc
        if j < number_users and i != j:
            userA = user_items[user_name+str(i)]
            userB = user_items[user_name+str(j)]
            coincidenceRate = compare(userA, userB)
            for c in coincidenceRate:
                if c > 0.6:
                    print('el usuario ' + user_name+str(i) + ' y el ' + user_name+str(j) +
                          ' son recomendables entre si con ratio ' + str(c))
                    #  nos basamos en todas las categorias para sacar el ratio
