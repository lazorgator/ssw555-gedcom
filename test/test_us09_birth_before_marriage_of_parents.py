from nose.tools import *

from gedcom.models import *
from gedcom.validate import validators


def test_birth_before_marriage_false():
    # Test with birth that happens after marriage
    individual1 = Individual('11')
    individual1.birth = Birth(datetime.date(1945, 4, 23))
    individual1.death = Death(datetime.date(1995, 3, 26))
    individual1.name = Name('Leandro', 'Ritter')
    individual1.sex = Sex('M')
    individual1.spouse_to = [FamilySpouse('11'), ]

    individual2 = Individual('12')
    individual2.birth = Birth(datetime.date(1950, 12, 24))
    individual2.name = Name('Alyssia', 'Holcomb')
    individual2.sex = Sex('F')
    individual2.spouse_to = [FamilySpouse('11'), ]

    individual3 = Individual('21')
    individual3.birth = Birth(datetime.date(1969, 5, 13))
    individual3.name = Name('Anita', 'Ritter')
    individual3.sex = Sex('F')
    individual3.child_to = [FamilyChild('11'), ]

    family = Family('11')
    family.marriages = [Marriage(datetime.date(1968, 9, 1)), ]
    family.husbands = [Husband('11'), ]
    family.wives = [Wife('12'), ]
    family.children = [Child('21'), ]

    individuals = [individual1, individual2, individual3]
    families = [family, ]

    result = validators['validate_birth_before_marriage'](individuals, families)
    assert_equal(True, result)


def test_birth_before_marriage_true():
    # Test with birth that happens before marriage
    individual1 = Individual('11')
    individual1.birth = Birth(datetime.date(1945, 4, 23))
    individual1.death = Death(datetime.date(1995, 3, 26))
    individual1.name = Name('Leandro', 'Ritter')
    individual1.sex = Sex('M')
    individual1.spouse_to = [FamilySpouse('11'), ]

    individual2 = Individual('12')
    individual2.birth = Birth(datetime.date(1950, 12, 24))
    individual2.name = Name('Alyssia', 'Holcomb')
    individual2.sex = Sex('F')
    individual2.spouse_to = [FamilySpouse('11'), ]

    individual3 = Individual('21')
    individual3.birth = Birth(datetime.date(1960, 5, 13))
    individual3.name = Name('Anita', 'Ritter')
    individual3.sex = Sex('F')
    individual3.child_to = [FamilyChild('11'), ]

    family = Family('11')
    family.marriages = [Marriage(datetime.date(1968, 9, 1)), ]
    family.husbands = [Husband('11'), ]
    family.wives = [Wife('12'), ]
    family.children = [Child('21'), ]

    individuals = [individual1, individual2, individual3]
    families = [family, ]

    result = validators['validate_birth_before_marriage'](individuals, families)
    assert_equal(True, result)


def test_birth_before_parent_death_false():
    # Test with birth that happens before parent death
    individual1 = Individual('11')
    individual1.birth = Birth(datetime.date(1945, 4, 23))
    individual1.death = Death(datetime.date(1995, 3, 26))
    individual1.name = Name('Leandro', 'Ritter')
    individual1.sex = Sex('M')
    individual1.spouse_to = [FamilySpouse('11'), ]

    individual2 = Individual('12')
    individual2.birth = Birth(datetime.date(1950, 12, 24))
    individual2.name = Name('Alyssia', 'Holcomb')
    individual2.sex = Sex('F')
    individual2.spouse_to = [FamilySpouse('11'), ]

    individual3 = Individual('21')
    individual3.birth = Birth(datetime.date(1969, 5, 13))
    individual3.name = Name('Anita', 'Ritter')
    individual3.sex = Sex('F')
    individual3.child_to = [FamilyChild('11'), ]

    family = Family('11')
    family.marriages = [Marriage(datetime.date(1968, 9, 1)), ]
    family.husbands = [Husband('11'), ]
    family.wives = [Wife('12'), ]
    family.children = [Child('21'), ]

    individuals = [individual1, individual2, individual3]
    families = [family, ]

    result = validators['validate_birth_after_parent_dead'](individuals, families)
    assert_equal(True, result)


def test_birth_before_parent_death_true():
    # Test with birth that happens after parent death
    individual1 = Individual('11')
    individual1.birth = Birth(datetime.date(1945, 4, 23))
    individual1.death = Death(datetime.date(1960, 3, 26))
    individual1.name = Name('Leandro', 'Ritter')
    individual1.sex = Sex('M')
    individual1.spouse_to = [FamilySpouse('11'), ]

    individual2 = Individual('12')
    individual2.birth = Birth(datetime.date(1930, 12, 24))
    individual2.name = Name('Alyssia', 'Holcomb')
    individual2.sex = Sex('F')
    individual2.spouse_to = [FamilySpouse('11'), ]

    individual3 = Individual('21')
    individual3.birth = Birth(datetime.date(1969, 5, 13))
    individual3.name = Name('Anita', 'Ritter')
    individual3.sex = Sex('F')
    individual3.child_to = [FamilyChild('11'), ]

    family = Family('11')
    family.marriages = [Marriage(datetime.date(1968, 9, 1)), ]
    family.husbands = [Husband('11'), ]
    family.wives = [Wife('12'), ]
    family.children = [Child('21'), ]

    individuals = [individual1, individual2, individual3]
    families = [family, ]

    result = validators['validate_birth_after_parent_dead'](individuals, families)
    assert_equal(True, result)
