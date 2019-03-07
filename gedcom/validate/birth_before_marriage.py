# Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def validate_birth_before_marriage(individuals, families):
    """ US09 - Birth should occur after the marriage of parents """
    return_flag = True

    # Loop through individuals to compare their birth date
    # with the marriage/divorce dates of their parents
    for individual in individuals:
        # Some individuals do not have parents defined
        # if they are the oldest generation in the gedcom file,
        if len(individual.child_to) > 0:
            # locate family of individual
            for family in families:
                if family.id == individual.child_to[0]:
                    # Checks for a child born before marriage
                    if family.marriage:
                        if family.marriage > individual.birthdate:
                            print("Child is born before marriage")
                            return_flag = False

    return return_flag
