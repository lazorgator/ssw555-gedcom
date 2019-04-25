
import sys
import os.path

import lark
from nose.tools import assert_true

from gedcom.validate.incest import validate_incest
from gedcom.transformer import GedcomTransformer
from gedcom.models import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

TEST_GEDCOM_1 = """0 NOTE Grandparents (Generation 1)
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
0 NOTE Grandparents family
0 F11 FAM
1 MARR
2 DATE 1 SEP 1968
1 HUSB I11
1 WIFE I12
1 CHIL I21
0 NOTE wife
0 I21 INDI
1 NAME Anita /Ritter/
1 BIRT
2 DATE 13 MAY 1960
1 SEX F
1 FAMC F11
1 FAMS F21
1 FAMS F31
0 NOTE husband
0 I41 INDI
1 NAME Azra /Velez/
1 BIRT
2 DATE 12 JUL 1960
1 DEAT
2 DATE 30 OCT 1989
1 SEX M
1 FAMS F21
0 NOTE family
0 F21 FAM
1 MARR
2 DATE 25 SEP 1989
1 DIV
2 DATE 30 OCT 1989
1 HUSB I41
1 WIFE I21"""

def test_multiple_marriage():
    flag = True;

    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                 .parse(TEST_GEDCOM_1))
    tree = GedcomTransformer().transform(parsetree)

    families = [f for f in tree.children if isinstance(f, Family)]
    individuals = [i for i in tree.children if isinstance(i, Individual)]

    assert_true(flag)
