import numpy as np

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
        

def import_file():
    with open('input/input.txt') as f:
        input = f.read().split('\n')

    signal_patterns = []
    for line in input:
        input, output = line.split('|')
        signal_patterns.append((input, output))

    return signal_patterns

def count_output(output):

    parse_output = output.split(' ')
    parse_output = list(filter(None, parse_output))
    unique_segments = [segment[1], segment[4], segment[7], segment[8]]
    count = [1 if len(x) in unique_segments else 0 for x in parse_output]

    return sum(count)

def main():
    signal_patterns = import_file()

    count = 0
    for input, output in signal_patterns:
        count += count_output(output)

    print(count)
        
if __name__ == '__main__':
    main()