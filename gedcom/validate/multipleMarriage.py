# Amr Saleh

from gedcom.validate import validator


@validator
def validate_multipleMarriage(individuals, families):
    # US19 - polygamy is checked
    for family in families:
        if len(family.husbands) > 1 or len(family.wives) > 1:
            print(
                'Family {} is polgamous'
                .format(family.id))
            return False
    return True