#Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def dates_before_current(individuals, families):
    """ US16 All dates must be before the current date - ERROR"""

    return_flag = True
    # date of birth, death, marriage, or divorce must be before current date
    for family in families:
        if family.marriage and family.marriage > datetime.now():
            print("Marriage occurs after current date")
            return_flag = False

        if family.divorce and family.divorce > datetime.now():
            print("Divorce occurs after current date")
            return_flag = False

    for indi in individuals:
        if indi.birthdate and indi.birthdate > datetime.now():
            print("Birth occurs after current date")
            return_flag = False

        if indi.death and indi.death > datetime.now():
            print("Death occurs after current date")
            return_flag = False

    return return_flag

