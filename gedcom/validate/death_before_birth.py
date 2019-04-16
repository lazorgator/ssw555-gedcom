"Trevor Miranda"
from gedcom.validate import validator


@validator
def validate_death_before_birth(individuals, families):
    for individual in individuals:
        if individual.death and individual.death.date < individual.birth.date:
            print('Individual {} died before they were born.'.format(individual.id))
            return False
    return True
