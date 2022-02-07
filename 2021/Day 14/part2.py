import re
import numpy as np
from collections import Counter
import time

STEPS = 40

def import_file():
    with open('input/input.txt') as f:
        file = f.read().split('\n')

    index = file.index('')
    polymer_template, insertion_pairs = [file[:index], file[index + 1:]]

    # Sanitize insertion pairs
    pattern_text = r'(?P<state>\w*)\s*[-][>]\s*(?P<transition>.*)'
    pattern = re.compile(pattern_text)
    matches = [re.search(pattern, n) for n in insertion_pairs]
    insertion_pairs = dict([(n.group(1), n.group(2)) for n in matches])

    return polymer_template[0], insertion_pairs

def main():
    polymer_template, insertion_pairs = import_file()

    # Get last character
    last_char = polymer_template[-1:]

    # Tokenise input string
    mappings = dict.fromkeys(insertion_pairs.keys(), 0)
    for pos, char in enumerate(polymer_template):
        if pos == 0: continue
        seq = polymer_template[pos-1] + polymer_template[pos]
        mappings[seq] += 1 

    for step in range(STEPS):
        new_mappings = mappings.copy()
        for seq in mappings:
            current_amount = mappings[seq] 
            new_seq_a = seq[0] + insertion_pairs[seq]
            new_seq_b = insertion_pairs[seq] + seq[1]
            new_mappings[new_seq_a] += current_amount
            new_mappings[new_seq_b] += current_amount
            new_mappings[seq] -= current_amount
        mappings = new_mappings

    # Count total occurances of each letter and add back in last character
    letter_counts = dict.fromkeys(insertion_pairs.values(), 0)
    for key, value in mappings.items():
        letter_counts[key[0]] += value
    letter_counts[last_char] += 1

    most_common = max(letter_counts.values())
    least_common = min(letter_counts.values())
    print(most_common - least_common)

if __name__ == '__main__':
    main()