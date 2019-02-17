import lark
from prettytable import PrettyTable
from nose.tools import assert_equals

from gedcom.models import Family, Individual
from gedcom.table import *
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


def test_table():
    parsetree = (lark.Lark.open('gedcom/gedcom.lark', parser='earley')
                 .parse(TEST_GEDCOM))
    tree = GedcomTransformer().transform(parsetree)
    families = {m.id: m for m in tree.children if isinstance(m, Family)}
    individuals = {m.id: m for m in tree.children
                   if isinstance(m, Individual)}

    # Create tables from parsing the TEST_GEDCOM
    family_table = create_family_table(families, individuals)
    individual_table = create_individual_table(individuals)

    # Create a table manually and get the string of it
    manual_family_table = PrettyTable()
    manual_family_table.field_names = [
        'ID',
        'Married',
        'Divorced',
        'Husband ID',
        'Husband Name',
        'Wife ID',
        'Wife Name',
        'Children',
    ]
    manual_family_table.add_row([
        '11',
        '1968-09-01',
        None,
        '11',
        'Leandro /Ritter/',
        '12',
        'Alyssia /Holcomb/',
        ['21',]
    ])

    manual_individual_table = PrettyTable()
    manual_individual_table.field_names = [
        'ID',
        'Name',
        'Gender',
        'Birthday',
        'Age',
        'Alive',
        'Death',
        'Child',
        'Spouse',
    ]
    manual_individual_table.add_row([
        '11',
        'Leandro /Ritter/',
        'M',
        '1945-04-23',
        '73',
        False,
        '1995-03-26',
        [],
        ['11',]
    ])
    manual_individual_table.add_row([
        '12',
        'Alyssia /Holcomb/',
        'F',
        '1950-12-24',
        '68',
        True,
        None,
        [],
        ['11',]
    ])
    manual_individual_table.add_row([
        '21',
        'Anita /Ritter/',
        'F',
        '1960-05-13',
        '58',
        True,
        None,
        ['11',],
        []
    ])

    # They should be equal
    assert_equals(str(manual_family_table), str(family_table))
    assert_equals(str(manual_individual_table), str(individual_table))
