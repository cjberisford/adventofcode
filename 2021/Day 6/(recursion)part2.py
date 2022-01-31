from input_parse import *
import numpy as np
import time
import math

NUM_DAYS = 256

def rec_fish_eval(current_day, total_days):

    # Add contribution of current fish
    branch_contribution = 1

    # Add descendents of current fish
    fish_born_on = list(range(current_day + 1, total_days, 7))

    for birthdate in fish_born_on:
        branch_contribution += rec_fish_eval(birthdate + 3, total_days) 

    return branch_contribution
         
def model_contribution(fish, total_days):

    k = 0 # Keep track of current day

    # Use recursion 
    contribution = rec_fish_eval(fish, total_days)

    return contribution

def main():
    # Convert to numpy array for efficiency
    total = 0
    for fish in fish_list:
        print("Calculating fish")
        total += print(model_contribution(fish, NUM_DAYS))

    print(total)

if __name__ == '__main__':
    main()