import sys
import os.path

import lark
from nose.tools import assert_equals

from gedcom.validate.marriage_age import marriage_age
from gedcom.transformer import GedcomTransformer
from gedcom.models import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


TEST_GEDCOM_1 = """
0 NOTE Test Note
0 I1 INDI
1 NAME John /Rit/
1 BIRT
2 DATE 9 MAR 1990
1 SEX M
1 FAMC F1

0 I2 INDI
1 NAME Jane /Richard/
1 BIRT
2 DATE 5 OCT 1992
1 DEAT
2 DATE 1 JAN 1999
1 SEX F
1 FAMC F1

0 F1 FAM
1 MARR
2 DATE 1 FEB 1998
1 HUSB I1
1 WIFE I2
"""

def test_marriage_age_true():
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                 .parse(TEST_GEDCOM_1))


    tree = GedcomTransformer().transform(parsetree)

    families = [f for f in tree.children if isinstance(f, Family)]
    individuals = [i for i in tree.children if isinstance(i, Individual)]

    assert_equals(True, marriage_age(individuals, families))

