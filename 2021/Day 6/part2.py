from input_parse import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from collections import Counter

NUM_DAYS = 256

def exponential(x, a, b):
    return a*np.exp(b*x)

def main():

    counts = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    # Import input data
    with open('input/input.txt') as f:
        fish_list = f.read().split(',')
    fish_list = np.array([int(x) for x in fish_list])

    # Init dict with imported values
    input_counts = Counter(fish_list)
    for key, value in input_counts.items():
        counts[key] = value

    print(counts)

    for day in range(NUM_DAYS):

        new_dict = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
        for key, value in counts.items():
            new_dict[key] = value

        for day, count in counts.items():
            if day == 0:
                new_dict[8] = count
                new_dict[6] += count
            else:
                new_dict[day-1] = count

        counts = new_dict
        print(counts)

    total = 0
    for _, val in counts.items():
        total += val
    print(total)

   
if __name__ == '__main__':
    main()