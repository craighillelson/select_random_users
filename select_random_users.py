""" __doc__ """

# imports
import csv
import random
from datetime import date

# define today
TODAY = date.today()

# prompt user for how many random users they would like to review
NUMBER_OF_USERS = int(input("How many random users would you like to audit? "))

# create list to be populated
USERS = []

# open csv and throw contents into a list
with open("OktaPasswordHealth.csv") as csvfile:
    READER = csv.DictReader(csvfile)
    for row in READER:
        USERS.append(row["Login"])

# get the length of the list
USERS_QTY = int(len(USERS))

# create a list of random numbers within a range from 0 to the number of users
# equal to the number specified by the user
RANDOM_INTEGERS = random.sample(range(0, USERS_QTY), NUMBER_OF_USERS)

# write results to file
USERS_TO_AUDIT = f"{TODAY}_users_to_audit.txt"
with open(USERS_TO_AUDIT, "w") as text_file:
    for integer in RANDOM_INTEGERS:
        user = str(USERS[integer])
        text_file.write(f"{user}\n")

# update user
print(f"{USERS_TO_AUDIT} exported successfully")
