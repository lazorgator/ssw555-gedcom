# Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def validate_birth_after_parent_dead(individuals, families):
    """ US10 - Birth should occur before the death of parents """
    return_flag = True

    # Loop through individuals to compare their birth date
    # with the death date of their parents
    for individual in individuals:

        if len(individual.child_to) > 0:
            father = None
            father_id = None
            mother = None
            mother_id = None
            fam = None

            for family in families:
                if family.id == individual.child_to[0]:
                    father_id = family.husband
                    mother_id = family.wife
                    fam = family
                    break

            for ind in individuals:
                if ind.id == father_id:
                    father = ind
                if ind.id == mother_id:
                    mother = ind

            # Case when father dies more than 9 months before
            from datetime import timedelta
            if father and father.death is not None and \
                    father.death < individual.birthdate - timedelta(days=266):
                print("Child is born in more than 9 months after death of father")
                return_flag = False

            # Case when mother dies before birth of child.
            if mother and mother.death is not None and mother.death < individual.birthdate:
                print("Child is born after death of mother")
                return_flag = False
    return return_flag
