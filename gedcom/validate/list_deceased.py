# Vaishnavi Gopalakrishnan
from gedcom.validate import validator


@validator
def list_deceased(individuals, _):
    """ US14 - List the deceased individuals """
    deceased = []
    for individual in individuals:
        if individual.death is not None:
            deceased.append(individual)
    return deceased

