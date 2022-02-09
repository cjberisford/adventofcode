from input_parse import *
import numpy as np

NUM_DAYS = 80

def process_lanternfish(fish_list, fish, i):

    # Decrement fish
    fish_list[i] = fish - 1

    # Spawn new fish
    if fish_list[i] == -1:
        fish_list[i] = 6
        fish_list.append(9)

    return fish_list

def main():

    starting_count = len(fish_list)
    for day in range(NUM_DAYS):
        
        updated_fish_list = fish_list
        
        # updated = len(updated_fish_list) - starting_count
        # print(f"{updated} fish added")
        # starting_count = len(updated_fish_list)
      
        # Update fish each day
        for i, fish in enumerate(fish_list):
            updated_fish_list = process_lanternfish(updated_fish_list, fish, i)
    
        # print("AFTER DAY ", day + 1, "(s) FISH STATUS", fish_list)

    print(len(fish_list))
        

if __name__ == '__main__':
    main()