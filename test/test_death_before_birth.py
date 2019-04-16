import lark

from nose.tools import assert_equals

from gedcom.models import *
from gedcom.transformer import GedcomTransformer
from gedcom.validate.death_before_birth import validate_death_before_birth


TEST_GEDCOM = """
0 NOTE Test Note
0 I11 INDI
1 NAME Leandro /Ritter/
1 BIRT
2 DATE 23 APR 1945
1 DEAT
2 DATE 26 MAR 1900
1 SEX M
1 FAMS F11
"""


def test_death_before_birth():
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley').parse(TEST_GEDCOM))
    tree = GedcomTransformer().transform(parsetree)

    families = [f for f in tree.children if isinstance(f, Family)]
    individuals = [i for i in tree.children if isinstance(i, Individual)]

    assert_equals(False, validate_death_before_birth(individuals, families))


TEST_GEDCOM_1 = """
0 NOTE Test Note
0 I11 INDI
1 NAME Leandro /Ritter/
1 BIRT
2 DATE 23 APR 1945
1 DEAT
2 DATE 26 MAR 1995
1 SEX M
1 FAMS F11
"""


def test_death_after_birth():
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley').parse(TEST_GEDCOM_1))
    tree = GedcomTransformer().transform(parsetree)

    families = [f for f in tree.children if isinstance(f, Family)]
    individuals = [i for i in tree.children if isinstance(i, Individual)]

    assert_equals(True, validate_death_before_birth(individuals, families))
