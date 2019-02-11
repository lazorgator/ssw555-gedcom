import argparse

import lark

from gedcom.models import Family, Individual
from gedcom.table import create_family_table, create_individual_table
from gedcom.transformer import GedcomTransformer


def main():
    parser = argparse.ArgumentParser('Gedcom file evaluator')
    parser.add_argument('gedcom_file', type=argparse.FileType('r'),
                        help='Gedcom file')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        help='Output file')
    args = parser.parse_args()

    with args.gedcom_file as f:
        # Parse the given gedcom file based on the gedcom.lark grammar
        lark_parser = lark.Lark.open('gedcom/gedcom.lark', parser='earley')
        parsetree = lark_parser.parse(f.read())
        # Build the AST from the parsetree
        tree = GedcomTransformer().transform(parsetree)

        # We now have a list of all the individuals, families, and notes
        # Isolate Family and Individual models into dictionaries
        families = {m.id: m for m in tree.children if isinstance(m, Family)}
        individuals = {m.id: m for m in tree.children
                       if isinstance(m, Individual)}

        # Create and print the individual table
        individual_table = create_individual_table(individuals)
        print('Individuals')
        print(individual_table)

        # Create and print the family table
        family_table = create_family_table(families, individuals)
        print('Families')
        print(family_table)


if __name__ == '__main__':
    main()
