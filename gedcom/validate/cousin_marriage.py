# Amr made this
from prettytable import PrettyTable

from gedcom.validate import validator

@validator
def validate_check_if_cousin_marriage(individuals, families):
    for family in families:
        for husband, wife in zip(family.husbands, family.wives):
            husband_ind = [i for i in individuals if i.id == husband.individual_id]
            wife_ind = [i for i in individuals if i.id == wife.individual_id]
            # check for cousins (parent's sibling's child)

            wife_aunt_uncles = []
            husband_aunt_uncles =[]
            wife_fam = None
            husband_fam = None

            for f in families:
                if len(wife_ind[0].child_to) > 0:
                    if f.id == wife_ind[0].child_to[0].family_id:
                        wife_fam = f
                        wife_aunt_uncles = f.children

                if len(husband_ind[0].child_to) > 0:
                    if f.id == husband_ind[0].child_to[0].family_id:
                        husband_fam = f
                        husband_aunt_uncles = f.children

            # see if wife's dad is one of husband's uncles
            if wife_fam is not None:
                wife_dad = wife_fam.husbands[0]
                wife_mom = wife_fam.wives[0]

                if wife_dad in husband_aunt_uncles:
                    print("cousin marriage between {} and {}", wife_ind , husband_ind)
                    return False

                if wife_mom in husband_aunt_uncles:
                    print("cousin marriage between {} and {}", wife_ind , husband_ind)
                    return False
            
            if husband_fam is not None:
                husband_dad = husband_fam.husbands[0]
                husband_mom = husband_fam.wives[0]
                if husband_dad in wife_aunt_uncles:
                    print("cousin marriage between {} and {}", wife_ind , husband_ind)
                    return False

                if husband_mom in wife_aunt_uncles:
                    print("cousin marriage between {} and {}", wife_ind , husband_ind)
                    return False
    return True
