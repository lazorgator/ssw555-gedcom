"Trevor Miranda"
from gedcom.validate import validator


@validator
def validate_marriage_after_death(individuals, families):
    for family in families:
        if family.husbands and family.wives:
            spouses = family.husbands + family.wives
            for spouse in spouses:
                individual = [i for i in individuals if i.id == spouse.individual_id]
                if len(individual):
                    for marriage in family.marriages:
                        if individual[0].death and individual[0].death.date < marriage.date:
                            print('Individual {} died before they were married in family {}.'.format(individual[0].id, family.id))
                            return False
    return True
