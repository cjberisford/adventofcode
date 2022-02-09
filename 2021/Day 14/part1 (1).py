import re
import numpy as np
from collections import Counter

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
    insertion_pairs = [(n.group(1), n.group(2)) for n in matches]

    return polymer_template[0], insertion_pairs

def CountOccurrences(string, substring):
    """Function stolen shamelessly from geeksforgeeks"""
  
    # Initialize count and start to 0
    count = 0
    start = 0
    indices = []
  
    # Search through the string till
    # we reach the end of it
    while start < len(string):
  
        # Check if a substring is present from
        # 'start' position till the end
        pos = string.find(substring, start)
  
        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            indices.append(pos)
            start = pos + 1

            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return indices

    
def main():
    polymer_template, insertion_pairs = import_file()

    for step in range(STEPS): 

        print(step)
        
        # Find all applicable transition rules
        applicable_rules = []
        for (state, transition) in insertion_pairs:
            indexes_of_match = CountOccurrences(polymer_template, state)
            if len(indexes_of_match) >= 0:
                for index_of_match in indexes_of_match:
                    applicable_rules.append((index_of_match, transition))

        # Sort applicable transition rules and then apply them
        applicable_rules.sort(key=lambda x: x[0])
        adjusted_index = 1
        for index, letter in applicable_rules:
            polymer_template = polymer_template[:index+adjusted_index] + letter + polymer_template[index+adjusted_index:]
            adjusted_index += 1

        
        # print(f"After step {step + 1}: {polymer_template}")

    # Count elements
    counts = Counter(polymer_template)
    most_common = max(counts.values())
    least_common = min(counts.values())
    print(most_common - least_common)


if __name__ == '__main__':
    main()