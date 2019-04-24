def list_living_married(individuals, families):
    """ US15 - List the living married people """
    living = []
    for family in families:
        husband_id = family.husband
        wife_id = family.wife

        husband = None
        wife = None

        for individual in individuals:
            if individual.id == husband_id and individual.death is None:
                husband = individual
            if individual.id == wife_id and individual.death is None:
                wife = individual
        if wife is not None and husband is not None:
            living.append(wife)
            living.append(husband)
    return living

