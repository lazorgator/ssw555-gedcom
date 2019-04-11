import sys
import os.path

import lark
from nose.tools import assert_equals

from gedcom.validate.gay_marriage import validate_check_if_gay
from gedcom.transformer import GedcomTransformer
from gedcom.models import *

from gedcom.validate import validators

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_cousin_marriage():
    # Test with husband that married dead brother's widow
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

    result = validators['validate_check_if_cousin_marriage'](
        individuals, families)
    assert True