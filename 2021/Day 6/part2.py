from input_parse import *
import numpy as np

NUM_DAYS = 200

def main():

    with open('input/example.txt') as f:
        fish_list = f.read().split(',')

    fish_list = np.array([int(x) for x in fish_list])

    total = 0
    for day in range(NUM_DAYS):
        print(day)
        zeros = fish_list.size - np.count_nonzero(fish_list)
        new_fish = [9] * zeros
        fish_list = np.append(fish_list, new_fish)
        fish_list = fish_list - 1
        fish_list = np.where(fish_list == -1, 6, fish_list)
        

    print(len(fish_list))

if __name__ == '__main__':
    main()