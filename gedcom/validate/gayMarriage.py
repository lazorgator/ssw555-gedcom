import datetime

from prettytable import PrettyTable

from gedcom.validate import validator


@validator
def checkIfGay(family,individuals):
        individual1 = individuals[family.husbands[0].individual_id]
        individual2 = individuals[family.wives[0].individual_id]

        if individual1.sex == individual2.sex:
            return True

        if len(family.wives) > 1 and len(family.husbands) == 0 :
            return True

        if len(family.husbands) > 1 and len(family.wives) == 0 :
            return True

        return False


@validator
def createGayTable(families, individuals):
    table = PrettyTable()
    table.field_names = [
        'ID',
        'Married',
        'Divorced',
        'Husband ID',
        'Husband Name',
        'Wife ID',
        'Wife Name'
    ]


    try:
        sorted_families = sorted(families.items(), key=lambda f: f[0])
    except:
        return None

    counter = 0

    for _, family in sorted_families:
        husband = individuals[family.husbands[0].individual_id]
        wife = individuals[family.wives[0].individual_id]

        if checkIfGay(family, individuals): # only add gay couples to table
            table.add_row([
                family.id,
                family.marriages[0],
                family.divorces[0] if family.divorces else None,
                husband.id,
                husband.name,
                wife.id,
                wife.name
            ])
            counter += 1

    if counter == 0: # return none if there are no gay couples
        return None
    return table
