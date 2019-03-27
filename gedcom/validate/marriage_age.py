# Vaishnavi Gopalakrishnan
from datetime import datetime


def marriage_age(individuals, families):
    """ US11 - Marriage should be atleast 14 years after the birth of both spouses """

    return_flag = True

    curr_date = datetime.today()
    min_birt = datetime(curr_date.year - 14,
                        curr_date.month, curr_date.day)

    for family in families:
        husband = None
        wife = None
        for individual in individuals:
            if individual.uid == family.husband:
                husband = individual
            if individual.uid == family.wife:
                wife = individual
            # We have found both the husband and wife individuals
            if husband is not None and wife is not None:
                break

        if husband.birthdate > min_birt:
            print("Husband is married before 14 years old")
            return_flag = False

        if wife.birthdate > min_birt:
            print("Wife is married before 14 years old")
            return_flag = False
    return return_flag
