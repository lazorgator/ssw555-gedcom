# Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def validate_birth_after_divorce(individuals, families):
    """ US09 - Birth should occur after the marriage of parents """
    for individual in individuals:
        if individual.child_to:
            for family in families:
                if family.id in individual.child_to:
                    if family.divorce and family.divorce < individual.birthdate:
                        print('Individual {} born after divorce in family {}.'
                              .format(individual.id, family.id))
                        return False
    return True
