import re
import numpy as np
from collections import Counter
import time

STEPS = 40

def import_file():
    with open('input/example.txt') as f:
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

    for step in range(STEPS): 

        start_stage_1 = time.time()

        # Construct string construction string
        construction_string = []
        adjusted_index = 0
        previous_element = polymer_template[0]
        for initial_position, element in enumerate(polymer_template):
            if (initial_position == 0): 
                construction_string.append((initial_position + adjusted_index, element))
                continue
            sequence = previous_element + element

            # Look up sequence in insertion pairs
            if sequence in insertion_pairs:
                construction_string.append((initial_position, insertion_pairs[sequence]))
                adjusted_index += 1

            construction_string.append((initial_position + adjusted_index, element))
            previous_element = element

        end_stage_1 = time.time()
        polymer_template = "".join([x[1] for x in construction_string])
        end_stage_2 = time.time()       

        time_1 = round(end_stage_1 - start_stage_1, 4)
        time_2 = round(end_stage_2 - end_stage_1, 4)
    
        print(f"Step {step}: Cycle time: {time_1}s. Constructed in {time_2}s. Polymer length: {len(polymer_template)} characters")

    # Count elements
    counts = Counter(polymer_template)
    most_common = max(counts.values())
    least_common = min(counts.values())
    print(most_common - least_common)


if __name__ == '__main__':
    main()