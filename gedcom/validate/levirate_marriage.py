# Amr made this
from prettytable import PrettyTable

from gedcom.validate import validator

@validator
def validate_check_if_levirate_marriage(individuals, families):
    # brother of dead guy married to widow
    wife = []
    # find all dead guys
    for i in individuals:
        if i.death is not None:
            # find their brothers
            bros = [x for x in individuals if x.child_to == i.child_to] # sex check
            # find the wife
            for family in families:   
                if family.id == i.spouse_to:
                    wife = family.wives
            
            # check if any of the bros are married to the the spouse
            for f in families:
                for z in bros:
                    for w in wife:
                        if z in f.husbands and w in f.wives:
                            return True
    return False