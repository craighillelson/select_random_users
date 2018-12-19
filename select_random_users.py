from collections import namedtuple
import csv
import random

# prompt user for how many random users they would like to review
number_of_users = raw_input("How many random users would you like to audit? ")
number_of_users = int(number_of_users)

# create list to be populated
users = []

# import a csv and throw it into a list
with open('OktaPasswordHealth.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        users.append(row)

# get the length of the list
users_qty = int(len(users))

# random_numbers = random.sample(range(1, 10), 3)
random_numbers = random.sample(range(1, users_qty), number_of_users)

# write results to file
with open('users_to_audit.txt', 'a') as text_file:
    for i in random_numbers:
        text_file.write(str(users[i]))
        text_file.write('\n')

# update user
print("'users_to_audit.txt' exported successfully")
