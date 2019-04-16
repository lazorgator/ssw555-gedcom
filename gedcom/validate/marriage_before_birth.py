"Trevor Miranda"
from gedcom.validate import validator


@validator
def validate_marriage_before_birth(individuals, families):
    for family in families:
        if family.husbands and family.wives:
            spouses = family.husbands + family.wives
            for spouse in spouses:
                individual = [i for i in individuals if i.id == spouse.individual_id]
                if len(individual):
                    for marriage in family.marriages:
                        if individual[0].birth.date > marriage.date:
                            print('Individual {} spouse born after marriage in family {}.'.format(spouse.individual_id, family.id))
                            return False
    return True
