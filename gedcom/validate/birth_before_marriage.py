# Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def validate_birth_before_marriage(individuals, families):
    """ US09 - Birth should occur after the marriage of parents """
    for individual in individuals:
        if individual.child_to:
            for family in families:
                if family.id in individual.child_to:
                    if family.marriage and family.marriage > individual.birthdate:
                        print('Individual {} born before marriage in family {}'
                              .format(individual.id, family.id))
                        return False
    return True
