# Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def validate_birth_after_parent_dead(individuals, families):
    """ US10 - Birth should occur before the death of parents """
    for individual in individuals:
        if individual.child_to:
            for family in families:
                if family.id in individual.child_to:
                    mothers = family.wives
                    fathers = family.husbands
                    for mother, father in zip(mothers, fathers):
                        if individual.birthdate > mother.death.date:
                            print(
                                'Individual {} born after death of mother in family {}.' .format(
                                    individual.id, family.id))
                            return False
                        if individual.birthdate > father.death.date:
                            print(
                                'Individual {} born after death of father in family {}.' .format(
                                    individual.id, family.id))
                            return False
    return True
