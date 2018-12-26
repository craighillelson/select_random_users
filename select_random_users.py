""" __doc__ """

# imports
from datetime import date
import csv
import random

# define today
TODAY = date.today()

# prompt user for how many random users they would like to review
NUMBER_OF_USERS = int(raw_input("How many random users would you like to audit? "))

# create list to be populated
USERS = []

# open csv and throw contents into a list
with open('OktaPasswordHealth.csv') as csvfile:
    READER = csv.DictReader(csvfile)
    for row in READER:
        user = row['Login']
        USERS.append(user)

# get the length of the list
USERS_QTY = int(len(USERS))

# create a list of random numbers within a range from 0 to the number of users
# equal to the number specified by the user
RANDOM_NUMBERS = random.sample(range(0, USERS_QTY), NUMBER_OF_USERS)

# write results to file
with open('users_to_audit.txt', 'a') as text_file:
    for i in RANDOM_NUMBERS:
        user = str(USERS[i])
        text_file.write(user)
        text_file.write('\n')

# update user
print("'%s_users_to_audit.txt' exported successfully") % (TODAY)
