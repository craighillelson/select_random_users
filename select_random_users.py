"""Select random users from an OktaPasswordHealth csv for auditing purposes."""

import csv
import random
from datetime import date
import pyinputplus as pyip


def populate_lst():
    """Import 'OktaPasswordHealth.csv' and populate a list of logins."""
    lst = []
    with open('OktaPasswordHealth.csv') as csvfile:
        READER = csv.DictReader(csvfile)
        for row in READER:
            lst.append(row['Login'])

    return lst


def prompt_user():
    """Prompt user for the number of users they'd like to audit."""
    print('\nHow many random users would you like to audit?')
    a = pyip.inputInt('> ', max=TOTAL_USERS)
    return a


def write_to_file():
    """Write to file and update user."""
    TODAY = date.today()
    USERS_TO_AUDIT = f'{TODAY}_users_to_audit.txt'
    RANDOM_INTEGERS = random.sample(range(0, TOTAL_USERS), NUMBER_OF_USERS)
    with open(USERS_TO_AUDIT, 'w') as text_file:
        for integer in RANDOM_INTEGERS:
            user = str(USERS[integer])
            text_file.write(f'{user}\n')

    print(f'{USERS_TO_AUDIT} exported successfully\n')


USERS = populate_lst()
TOTAL_USERS = len(USERS)
NUMBER_OF_USERS = prompt_user()
write_to_file()
