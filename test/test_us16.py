# Vaishnavi Gopalakrishnan

import os.path
import sys

import lark
from nose.tools import assert_true
from nose.tools import assert_false

from gedcom.validate.dates_before_current import dates_before_current
from gedcom.transformer import GedcomTransformer
from gedcom.models import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

TEST_GEDCOM_1 = """
0 NOTE DATES BEFORE CURRENT DATE PASS CASE
0 I1 INDI
1 NAME John /Doe/
1 SEX M
1 BIRT
2 DATE 9 MAR 1990
1 FAMC F1
0 I2 INDI
1 NAME Jane /Doe/
1 SEX F
1 BIRT
2 DATE 5 OCT 1980
1 DEAT
2 DATE 1 JAN 2000
1 FAMC F1
0 F1 FAM
1 HUSB I1
1 WIFE I2
1 MARR
2 DATE 2 JAN 1998
1 DIV
2 DATE 2 JAN 1999
"""


def test_dates_before_current():
    """ Unit test for dates_before_current"""

    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                 .parse(TEST_GEDCOM_1))
    tree = GedcomTransformer().transform(parsetree)

    if os.path.exists('fail_file') and os.path.exists('pass_file'):
        individuals, families = parse_ged(pass_file)
        self.assert_true(dates_before_current(individuals, families))
        individuals, families = parse_ged(fail_file)
        self.assert_false(dates_before_current(individuals, families))
    else:
        print("!!test_date_before_current acceptance file not found")
