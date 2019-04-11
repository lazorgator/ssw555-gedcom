# Vaishnavi Gopalakrishnan
from datetime import datetime


def marriage_age(individuals, families):
    """ US11 - Marriage should be at least 14 years after the birth of both spouses """

    return_flag = True

    curr_date = datetime.today()
    min_birt = datetime(curr_date.year - 14,
                        curr_date.month, curr_date.day)

    for family in families:
        husband = None
        wife = None
        for individual in individuals:
            if individual.id == family.husbands[0].individual_id:
                husband = individual
            if individual.id == family.wives[0].individual_id:
                wife = individual
            # We have found both the husband and wife individuals
            if husband is not None and wife is not None:
                break

        if husband.birth.date > min_birt.date():
            print("Husband is married before 14 years old")
            return_flag = False

        if wife.birth.date > min_birt.date():
            print("Wife is married before 14 years old")
            return_flag = False
    return return_flag

