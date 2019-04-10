def correct_gender_for_role(individuals, families):
    """ US13 - Correct Gender for Role; husband should be male, wife should be female"""

    global return_flag
    for family in families:
        husband_id = family.husband
        wife_id = family.wife

        husband = None
        wife = None

        for individual in individuals:
            if individual.uid == husband_id:
                husband = individual
            if individual.uid == wife_id:
                wife = individual

        if husband.sex is not "M":
            print("Husband is not a male")
            return_flag = False

        if wife.sex is not "F":
            print("Wife is not a female");
            return_flag = False
    return return_flag

