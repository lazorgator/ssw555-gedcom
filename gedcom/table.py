import datetime

from prettytable import PrettyTable


def create_individual_table(individuals):
    table = PrettyTable()
    table.field_names = [
        'ID',
        'Name',
        'Gender',
        'Birthday',
        'Age',
        'Alive',
        'Death',
        'Child',
        'Spouse',
        ]
    sorted_individuals = sorted(individuals.items(), key=lambda i: i[0])
    for _, individual in sorted_individuals:
        # Get age in years
        age = int(
            (datetime.date.today() -
             individual.birth.date).days /
            365.25)
        is_alive = individual.death is None
        table.add_row([
            individual.id,
            individual.name,
            individual.sex,
            individual.birth,
            age,
            is_alive,
            individual.death,
            [c.family_id for c in individual.child_to],
            [s.family_id for s in individual.spouse_to],
            ])
    return table


def create_family_table(families, individuals):
    table = PrettyTable()
    table.field_names = [
        'ID',
        'Married',
        'Divorced',
        'Husband ID',
        'Husband Name',
        'Wife ID',
        'Wife Name',
        'Children',
        ]
    sorted_families = sorted(families.items(), key=lambda f: f[0])
    for _, family in sorted_families:
        # TODO: How should we handle multiple husbands/wives?
        husband = individuals[family.husbands[0].individual_id]
        wife = individuals[family.wives[0].individual_id]
        table.add_row([
            family.id,
            # TODO: How should we handle multiple marriages and divorces?
            family.marriages[0],
            family.divorces[0] if family.divorces else None,
            husband.id,
            husband.name,
            wife.id,
            wife.name,
            [c.individual_id for c in family.children],
            ])
    return table
