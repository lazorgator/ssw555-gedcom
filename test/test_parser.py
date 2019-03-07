import datetime

import lark
from nose.tools import assert_equals

from gedcom.models import *
from gedcom.transformer import GedcomTransformer


TEST_GEDCOM = """
0 NOTE Test Note
0 I11 INDI
1 NAME Leandro /Ritter/
1 BIRT
2 DATE 23 APR 1945
1 DEAT
2 DATE 26 MAR 1995
1 SEX M
1 FAMS F11

0 I12 INDI
1 NAME Alyssia /Holcomb/
1 BIRT
2 DATE 24 DEC 1950
1 SEX F
1 FAMS F11

0 I21 INDI
1 NAME Anita /Ritter/
1 BIRT
2 DATE 13 MAY 1960
1 SEX F
1 FAMC F11

0 F11 FAM
1 MARR
2 DATE 1 SEP 1968
1 HUSB I11
1 WIFE I12
1 CHIL I21
"""


def test_parser():
    # Create a Note using models only
    note = Note(content=' Test Note')

    # Create Individuals using models only
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

    # Create a Family using models only
    family = Family('11')
    family.marriages = [Marriage(datetime.date(1968, 9, 1)), ]
    family.husbands = [Husband('11'), ]
    family.wives = [Wife('12'), ]
    family.children = [Child('21'), ]

    # Put them into a list in order
    expected_output = [
        note,
        individual1,
        individual2,
        individual3,
        family
        ]

    # Parse the TEST_GEDCOM to get the AST
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                 .parse(TEST_GEDCOM))
    tree = GedcomTransformer().transform(parsetree)

    # Test that the AST and models are equivalent
    assert_equals(expected_output, tree.children)
