"Trevor Miranda"
from gedcom.validate import validator


@validator
def validate_divorce_after_death(individuals, families):
    for family in families:
        if family.husbands and family.wives:
            spouses = family.husbands + family.wives
            for spouse in spouses:
                individual = [i for i in individuals if i.id == spouse.individual_id]
                if len(individual):
                    for divorce in family.divorces:
                        if individual[0].death.date < divorce.date:
                            print('Individual {} spouse died before divorce in family {}.'.format(spouse.individual_id, family.id))
                            return False
    return True
