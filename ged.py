import argparse

import lark

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
        print(tree.children)
        # TODO: Complete the rest


if __name__ == '__main__':
    main()
