# imports
from datetime import date
import csv
import random

# define today
today = date.today()

# prompt user for how many random users they would like to review
number_of_users = int(raw_input
	("How many random users would you like to audit? "))

# create list to be populated
users = []

# open csv and throw contents into a list
with open('OktaPasswordHealth.csv') as csvfile:  
		reader = csv.DictReader(csvfile)
		for row in reader:
			user = row['Login']
			users.append(user)
	
# get the length of the list
users_qty = int(len(users))

# create a list of random numbers within a range from 0 to the number of users
# equal to the number specified by the user
random_numbers = random.sample(range(0, users_qty), number_of_users)

# write results to file
with open('users_to_audit.txt', 'a') as text_file:
    for i in random_numbers:
    	user = str(users[i])
        text_file.write(user)
        text_file.write('\n')

# update user
print("'%s_users_to_audit.txt' exported successfully") % (today)
