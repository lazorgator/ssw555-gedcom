import lark
from nose.tools import assert_equals

from gedcom.models import *
from gedcom.transformer import GedcomTransformer
from gedcom.validate.marriage_before_birth import validate_marriage_before_birth


TEST_GEDCOM = """
0 NOTE Test Note
0 I11 INDI
1 NAME Leandro /Ritter/
1 BIRT
2 DATE 23 APR 1970
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


def test_marriage_before_birth():
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley').parse(TEST_GEDCOM))
    tree = GedcomTransformer().transform(parsetree)

    families = [f for f in tree.children if isinstance(f, Family)]
    individuals = [i for i in tree.children if isinstance(i, Individual)]

    assert_equals(False, validate_marriage_before_birth(individuals, families))


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


def test_marriage_before_birth():
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley').parse(TEST_GEDCOM_1))
    tree = GedcomTransformer().transform(parsetree)

    families = [f for f in tree.children if isinstance(f, Family)]
    individuals = [i for i in tree.children if isinstance(i, Individual)]

    assert_equals(True, validate_marriage_before_birth(individuals, families))
