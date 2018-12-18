import csv
import random

# prompt user for how many random users they would like to review
number_of_users = raw_input("How many random users would you like selected? ")
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

# print selected users
for i in random_numbers:
    print(users[i])