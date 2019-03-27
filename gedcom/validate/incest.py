# Amr Saleh
# never thought I'd make a py file called incest

from gedcom.validate import validator


@validator
def validate_incest(individuals, families):
    # US19 - Siblings can't get married, check if they share a parent
    for family in families:
        for husband, wife in zip(family.husbands, family.wives):
            husband_ind = [i for i in individuals
                           if i.id == husband.individual_id]
            wife_ind = [i for i in individuals if i.id == wife.individual_id]
            if husband_ind and wife_ind and husband_ind[0].child_to in wife_ind[0].child_to and len(husband_ind[0].child_to) > 0 and len(wife_ind[0].child_to) > 0:
                print(
                    'Individuals {} and {} are incestual (ew).'
                    .format(husband.individual_id, wife.individual_id))
                return False
    return True