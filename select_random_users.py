import csv
import random

# prompt user for how many random users they would like to review
number_of_users = raw_input("How many random users would you like selected? ")
# print(number_of_users)

# create list
users = []

# import a csv and throw it into a list
with open('OktaPasswordHealth.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		users.append(row)

# get the length of the list
users_qty = len(users)
print(users_qty)

# number_of_users = len(lst)
# for the number of users specified by the user, select a random user, throw 
# that user into a list random_user_lst and remove the same user from lst