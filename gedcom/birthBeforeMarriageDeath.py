def us09_birth_before_marriage_of_parents(individuals, families):
    """ US09 - Birth should occur after the marriage of parents """
    return_flag = True

    # Loop through individuals to compare their birth date
    # with the marriage/divorce dates of their parents
    for individual in individuals:

        # Some individuals do not have parents defined
        # if they are the oldest generation in the gedcom file,
        # if len(individual.famc) > 0:
            # locate family of individual
            for family in families:
                if family.uid == individual.famc[0]:
                    # Checks for a child born before marriage
                    if family.marriage:
                        if family.marriage > individual.birthdate:
                            print("Child is born before marriage")
                            return_flag = False
                    # checks for child born after divorce
                    if family.marriage and family.divorce:
                        if family.divorce < individual.birthdate:
                            print("Child is born after divorce")
                            return_flag = False

    return return_flag


def us10_birth_before_death_of_parents(individuals, families):
    """ US10 - Birth should occur before the death of parents """
    return_flag = True

    # Loop through individuals to compare their birth date
    # with the death date of their parents
    for individual in individuals:

        if len(individual.famc) > 0:
            father = None
            father_id = None
            mother = None
            mother_id = None
            fam = None

            for family in families:
                if family.uid == individual.famc[0]:
                    father_id = family.husband
                    mother_id = family.wife
                    fam = family
                    break

            for ind in individuals:
                if ind.uid == father_id:
                    father = ind
                if ind.uid == mother_id:
                    mother = ind

            # Case when father dies more than 9 months before
            from datetime import timedelta
            if father.death is not None and \
                    father.death < individual.birthdate - timedelta(days=266):
                print("Child is born in more than 9 months after death of father")
                return_flag = False

            # Case when mother dies before birth of child.
            if mother.death is not None and mother.death < individual.birthdate:
                print("Child is born after death of mother")
                return_flag = False
    return return_flag
