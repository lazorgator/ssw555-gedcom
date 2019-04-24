# Amr made this

from gedcom.validate import validator

from datetime import datetime

@validator
def validate_check_for_long_engagement(individuals, families):
    # just realized there are no engagements in GEDCOM, so I'm just going to highlight long marriages
    """ US-24 - note long engagements """

    curr_date = datetime.today()
    # a long marriage is one that lasts atleast 20 years
    min_marraige = datetime(curr_date.year - 20, curr_date.month, curr_date.day)
    # if the marriage is before this date, its long

    for family in families:
        f = family
        for marriage in family.marriages:
            # past < present = true
            if marriage.date < min_marraige.date():
                # marrriage old
                print("Marriage: {} is really long!", f.id)
                return True

    return False
