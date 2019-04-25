# Amr made this

from gedcom.validate import validator

@validator
def validate_check_for_cheaters(individuals, families):
    """ US23 - Note infidelity """
    # for each fams check for divorce or death prior to next fam

    for family in families:
        # check if husband is in any other families
        husband = family.husband
        wife = family.wife

        for fam in families:
            if fam is family:
                continue

            if fam.husband == husband_uid:
                if fam.marriage > family.marriage:
                    wife = next(x for x in individuals if x.uid == family.wife)

                    if ((family.divorce < fam.marriage) or
                            (wife.death and (wife.death < fam.marriage))):
                        return False
                        print("husband is maried to tw people")

            if fam.wife == wife_uid and fam.marriage > family.marriage:
                if fam.marriage > family.marriage:
                    husb = next(x for x in individuals if x.uid == family.husband)

                    if (family.divorce > fam.marriage) or \
                            (husb.death and (husb.death < family.marriage)):
                        return False
                        print("wife is maried to two people")
    return True
