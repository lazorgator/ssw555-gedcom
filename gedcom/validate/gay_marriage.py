from gedcom.validate import validator


@validator
def validate_check_if_gay(individuals, families):
    for family in families:
        for husband, wife in zip(family.husbands, family.wives):
            husband_ind = [i for i in individuals
                           if i.id == husband.individual_id]
            wife_ind = [i for i in individuals if i.id == wife.individual_id]
            if husband_ind and wife_ind and husband_ind[0].sex == wife_ind[0].sex:
                print(
                    'Individuals {} and {} are in a gay marriage.'
                    .format(husband.individual_id, wife.individual_id))
                return False
    return True
