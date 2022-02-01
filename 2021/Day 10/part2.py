import re 
from collections import Counter

points = {')': 1, ']': 2, '}': 3, '>': 4}

def import_file():
    with open('input/input.txt') as f:
        input_list = f.read().split('\n')

    return input_list

def evaluate_string(line):

    total = 0
    for char in line:
        total *= 5
        total += points[char]

    return total

def mirror_string(line):
    line = line.replace('{', '}').replace('[', ']').replace('(', ')').replace('<', '>')
    return line[::-1]

def autocomplete(line, scores):
    brackets = ['()', '[]', '{}', '<>']
    closing_brackets = [')', ']', '}', '>']

    while any(x in line for x in brackets):
        for br in brackets:
            line = line.replace(br, '')

    if not any(x in line for x in closing_brackets):
        # Line is either valid or incomplete, so count closing brackets
        line = mirror_string(line)
        value = evaluate_string(line)
        if value > 0:
            scores.append(value)
    return scores

def main():

    navigation_subsystem = import_file()
    scores = []
    for line in navigation_subsystem:
        scores = autocomplete(line, scores)

    scores.sort()

    # Take middle score
    middle = int(((len(scores) + 1) / 2) - 1)
    print(scores[middle])


if __name__ == '__main__':
    main()