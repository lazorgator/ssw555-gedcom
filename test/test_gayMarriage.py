import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import datetime

import lark
from nose.tools import assert_equals
from prettytable import PrettyTable

from gedcom.models import *
from gedcom.transformer import GedcomTransformer
from gedcom.gayMarriage import checkIfGay, createGayTable

import unittest

# test GEDCOM of a gay couple
TEST_GEDCOM_1 = """ 
0 NOTE Test Note
0 I11 INDI
1 NAME Sarah /Ritter/
1 BIRT
2 DATE 23 APR 1945
1 DEAT
2 DATE 26 MAR 1995
1 SEX F
1 FAMS F11

0 I12 INDI
1 NAME Jane /Holcomb/
1 BIRT
2 DATE 24 DEC 1950
1 SEX F
1 FAMS F11

0 F11 FAM
1 MARR
2 DATE 1 SEP 1968
1 HUSB I11
1 WIFE I12
"""

# test gedcom of a straight couple
TEST_GEDCOM_2 = """
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

class TestGayMarriage(unittest.TestCase):

    def setUp(self):
        pass

    def testDetectGayCouple(self):
        # Parse the TEST_GEDCOM_1
        parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                .parse(TEST_GEDCOM_1))
        tree = GedcomTransformer().transform(parsetree)

        families = {m.id: m for m in tree.children if isinstance(m, Family)}

        individuals = {m.id: m for m in tree.children
                    if isinstance(m, Individual)}

        table = PrettyTable()
        table.field_names = [
            'ID',
            'Married',
            'Divorced',
            'Husband ID',
            'Husband Name',
            'Wife ID',
            'Wife Name'
        ]
        
        sorted_families = sorted(families.items(), key=lambda f: f[0])

        for _, family in sorted_families:
            fam = family
        
        self.assertTrue(checkIfGay(fam, individuals))
    

    def testReturnFalseOnStraightCouple(self):
        # Parse the TEST_GEDCOM_2
        parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                .parse(TEST_GEDCOM_2))
        tree = GedcomTransformer().transform(parsetree)

        families = {m.id: m for m in tree.children if isinstance(m, Family)}

        individuals = {m.id: m for m in tree.children
                    if isinstance(m, Individual)}

        table = PrettyTable()
        table.field_names = [
            'ID',
            'Married',
            'Divorced',
            'Husband ID',
            'Husband Name',
            'Wife ID',
            'Wife Name'
        ]
        
        sorted_families = sorted(families.items(), key=lambda f: f[0])

        for _, family in sorted_families:
            fam = family
        
        self.assertFalse(checkIfGay(fam, individuals))
    

    def testCreateTable(self):
        # Parse the TEST_GEDCOM_1
        parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                .parse(TEST_GEDCOM_1))
        tree = GedcomTransformer().transform(parsetree)

        families = {m.id: m for m in tree.children if isinstance(m, Family)}

        individuals = {m.id: m for m in tree.children
                    if isinstance(m, Individual)}
        
        table = createGayTable(families, individuals)

        self.assertIsNotNone(table)
    
    def testTableIsNoneWhenNoGayCoupleFound(self):
        # Parse the TEST_GEDCOM_2
        parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                .parse(TEST_GEDCOM_2))
        tree = GedcomTransformer().transform(parsetree)

        families = {m.id: m for m in tree.children if isinstance(m, Family)}

        individuals = {m.id: m for m in tree.children
                    if isinstance(m, Individual)}
        
        table = createGayTable(families, individuals)

        self.assertIsNone(table)

    def testDontBreakWithErroneousInput(self):
        table = createGayTable([12, "heelo"], [133, "not a table"])

        self.assertIsNone(table)


if __name__ == '__main__':
    unittest.main()

    