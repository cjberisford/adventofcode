import numpy as np
from collections import Counter

segment = { 0: 6,
            1: 2,
            2: 5,
            3: 5,
            4: 4,
            5: 5,
            6: 6,
            7: 3,
            8: 7,
            9: 6 }

segment_length = {  2: 1,
                    3: 7,
                    4: 4,
                    5: [2, 3, 5],
                    6: [0, 6, 9],
                    7: 8 } 

mapping = { 'a': [0, 2, 3, 5, 6, 7, 8, 9],
            'b': [0, 4, 5, 6, 8, 9],
            'c': [0, 1, 2, 3, 4, 7, 8, 9],
            'd': [2, 3, 4, 5, 6, 8, 9],
            'e': [0, 2, 6, 8],
            'f': [0, 1, 3, 4, 5, 6, 7, 8, 9],
            'g': [0, 2, 3, 5, 6, 8, 9] }       

def import_file():
    with open('input/input.txt') as f:
        input = f.read().split('\n')

    signal_patterns = []
    for line in input:
        input, output = line.split('|')
        signal_patterns.append((input, output))

    return signal_patterns

def segment_distance(first, second):
    common_letters = Counter(first) & Counter(second)
    return sum(common_letters.values())

def get_mapping(input):

    unique_segments = [segment[1], segment[4], segment[7], segment[8]]

    # Determine constraints algorithmically
    mapping = {}

    for sequence in input:
        sequence_length = len(sequence)
        
        # If known, add to mapping now
        if sequence_length in unique_segments:
            mapping[segment_length[sequence_length]] = sequence

    for sequence in input:
        sequence_length = len(sequence)
        if sequence_length == 5:
            # String is either 2, 3 or 5
            if (segment_distance(sequence, mapping[7])) == 3:
                # 3 is superset of 7, so check if contains 3
                mapping[3] = sequence
            elif (segment_distance(sequence, mapping[4])) == 3:
                mapping[5] = sequence
            else:
                # 4 and 5 overlap 3 times - 4 and 2 overlap twice
                mapping[2] = sequence
        elif sequence_length == 6:
            # String is either 0, 6 or 9
            if (segment_distance(sequence, mapping[1])) == 1:
                # Can only be 6
                mapping[6] = sequence
            elif (segment_distance(sequence, mapping[4])) == 4:
                # Must be 9
                mapping[9] = sequence
            else:
                # Must be 0
                mapping[0] = sequence

    inverted_map = {value:key for key, value in mapping.items()}

    return inverted_map 


def decode(input, output):
    parse_input = input.split(' ')
    parse_input = list(filter(None, parse_input))
    parse_output = output.split(' ')
    parse_output = list(filter(None, parse_output))

    mapping = get_mapping(parse_input)

    # Use mapping to get total values

    # Hacky workaround to order strings
    ordered_mapping = {}
    for key, value in mapping.items():
        new_key = sorted(key)
        ordered_key = "".join(new_key)
        ordered_mapping[ordered_key] = value

    number = []
    for digit in parse_output:
        new_digit = sorted(digit)
        ordered_digit = "".join(new_digit)
        value = ordered_mapping[ordered_digit]
        number.append(str(value))
 
    decoded_value = int("".join(number))
    return decoded_value



def main():
    signal_patterns = import_file()

    total = 0
    for input, output in signal_patterns:
        total += decode(input, output)

    print(total)

if __name__ == '__main__':
    main()