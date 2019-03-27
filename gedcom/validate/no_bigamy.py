# Vaishnavi Gopalakrishnan


def no_bigamy(individuals, families):
    """ US12 - Marriage should not occur during marriage to another spouse """
    # for each fams check for divorce or death prior to next fam
    return_flag = True

    for family in families:
        # check if husband is in any other families
        husband_uid = family.husband
        wife_uid = family.wife

        for fam_compare in families:
            # Make sure not comparing against self
            if fam_compare is family:
                continue

            if fam_compare.husband == husband_uid:
                if fam_compare.marriage > family.marriage:
                    wife = next(x for x in individuals if x.uid == family.wife)

                    # Family divorce should occur after or wife should die first
                    if ((family.divorce < fam_compare.marriage) or
                            (wife.death and (wife.death < fam_compare.marriage))):

                        print("Marriage occurred before divorce or death from/of wife")

            if fam_compare.wife == wife_uid:
                if fam_compare.marriage > family.marriage:
                    husb = next(x for x in individuals if x.uid == family.husband)

                    # Family divorce should occur after or wife should die first
                    if (family.divorce > fam_compare.marriage) or \
                        (husb.death and (husb.death < family.marriage)):
                            print("Marriage occurred before divorce or death of husband")

    return return_flag

