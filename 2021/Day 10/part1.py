import re 
from collections import Counter

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

def import_file():
    with open('input/input.txt') as f:
        input_list = f.read().split('\n')

    return input_list

def check_symmetric(line, errors):
    brackets = ['()', '[]', '{}', '<>']
    closing_brackets = [')', ']', '}', '>']

    while any(x in line for x in brackets):
        for br in brackets:
            line = line.replace(br, '')

    if any(x in line for x in closing_brackets):
        # Found unexpected character
        result = re.search(r'[\]\}\)\>]', line)
        errors.append(result.group())
        
    # Line is either valid or incomplete
    return errors


def main():


    navigation_subsystem = import_file()
    errors = []

    for line in navigation_subsystem:
        errors = check_symmetric(line, errors)

    # Count scores
    total = 0
    for char, count in Counter(errors).items():
        total += (points[char] * count)
 
    print(total)


if __name__ == '__main__':
    main()