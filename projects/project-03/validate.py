'Trevor Miranda'
import argparse
import re

TAGS = {
    0: ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'],
    1: ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR',
        'HUSB', 'WIFE', 'CHIL', 'DIV'],
    2: ['DATE', ]
}
EXPR_REGEX = re.compile(r'^(?P<level>\d+) (?P<tag>\w+)(\s(?P<args>.+))*$')


def validate(line):
    """Validate a line of GEDCOM."""
    match = EXPR_REGEX.match(line)
    level = match.group('level')
    tag = match.group('tag')
    args = match.group('args')
    valid_tag = 'Y' if tag in TAGS[int(level)] else 'N'
    # Check for exceptions
    if valid_tag != 'Y':
        valid_tag = 'Y' if args in TAGS[int(level)] else 'N'
        if valid_tag == 'Y':
            # Swap tag and arguments
            swap = tag
            tag = args
            args = swap
    return (level, tag, valid_tag, args)


def main():
    parser = argparse.ArgumentParser('Validate GEDCOM file.')
    parser.add_argument('gedcom_file', type=argparse.FileType('r'),
                        help='Gedcom file to validate.')
    parser.add_argument('-o', '--output', type=argparse.FileType('w+'),
                        help='Output file.')
    args = parser.parse_args()

    output = []
    individuals = {}
    families = {}
    current_family = None
    current_individual = None
    with args.gedcom_file as f:
        for line in f.readlines():
            line = line.strip('\n')
            output.append('--> {}'.format(line))
            validation = validate(line)
            output.append('<-- {level}|{tag}|{valid}|{args}'.format(
                level=validation[0], tag=validation[1], valid=validation[2],
                args=validation[3] or ''))
            tag = validation[1]
            arguments = validation[3] or ''
            # Rough, hacky parsing, should use a proper parser
            if tag == 'INDI':
                current_individual = arguments
            if tag == 'NAME':
                individuals[current_individual] = arguments
            if tag == 'FAM':
                current_family = arguments
            if tag == 'HUSB':
                if current_family not in families:
                    families[current_family] = {'husbands': [], 'wives': []}
                families[current_family]['husbands'].append(arguments)
            if tag == 'WIFE':
                if current_family not in families:
                    families[current_family] = {'husbands': [], 'wives': []}
                families[current_family]['wives'].append(arguments)

    sorted_individuals = sorted(individuals.items(), key=lambda i: i[0])
    print('')
    print('INDIVIDUALS')
    print('---')
    print('\n'.join('{} {}'.format(k, v) for k, v in sorted_individuals))
    sorted_families = sorted(families.items(), key=lambda f: f[0])
    print('')
    print('FAMILIES')
    print('---')
    for id_, spouses in sorted_families:
        print('{} FAMILY'.format(id_))
        for husband in spouses['husbands']:
            print('\tHUSBAND {}'.format(individuals[husband]))
        for wife in spouses['wives']:
            print('\tWIFE {}'.format(individuals[wife]))

    if args.output:
        with args.output as f:
            f.write('\n'.join(output))
    else:
        print('\n'.join(output))


if __name__ == '__main__':
    main()
