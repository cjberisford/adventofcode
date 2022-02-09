import numpy as np
import sys
from pathlib import Path

path = Path(__file__).parent / "input/input.txt"

DIRECTIONS = ['S', 'E', 'N', 'W']

def import_file():

    with open(path) as f:
        file = f.read().split('\n')
    file = np.array([list(str(x)) for x in file])
    return file


def weight_update(height, width, row, col, rewards, risk_levels):
    if col == width-1:
        # If cell is at end of row update with value below
        rewards[row-1, col] = rewards[row, col]
    elif row == height:
        # If cell is at bottom of col, update += with value to right
        rewards[row-1, col] = rewards[row-1, col+1]
    else:
        # Update with minimum from right or below
        rewards[row-1, col] += min(rewards[row-1, col+1], rewards[row, col])
    # Add current risk level to total
    rewards[row-1, col] += int(risk_levels[row-1, col])

    return rewards

def calculate_weights(risk_levels):

    height, width = risk_levels.shape
    rewards = np.zeros((height, width))
    rewards[height-1, width-1] = risk_levels[height-1, width-1] 

    # First half of grid
    for k in range(height+1):
        for i, j in zip(range(height, height-k, -1), range(height-k, width, 1)):
            if i == height and j == width-1:
                continue
            rewards = weight_update(height, width, i, j, rewards, risk_levels)
        
    # Second half of grid
    for k in range(1, height+1, 1):
        for i, j in zip(range(height-k, 0, -1), range(0, width-k, 1)):
            if i == height and j == width-1:
                continue
            rewards = weight_update(height, width, i, j, rewards, risk_levels)

    return rewards

def select_direction(current_position, rewards):

    if min(current_position) < 0:
        print("Index less than 0, algorithm has failed.")
        sys.exit()

    row, col = current_position
    directions = dict.fromkeys(DIRECTIONS, np.inf)
    values = dict.fromkeys(DIRECTIONS, np.inf)

    if row > 0: directions['N'] = rewards[row-1, col]
    if col < rewards.shape[0]-1: directions['E'] = rewards[row, col+1]
    if row < rewards.shape[1]-1: directions['S'] = rewards[row+1, col]
    if col > 0: directions['W'] = rewards[row, col-1]

    direction = min(directions, key=directions.get)

    if direction == 'E':
        return (row, col+1)
    elif direction == 'S':
        return (row+1, col)
    elif direction == 'W':
        return (row, col-1)
    else:
        return (row-1, col)

def main():

    risk_levels = import_file()
    rewards = calculate_weights(risk_levels)

    print(rewards.shape)

    accumulated_risk = 0
    starting_location = (0, 0)

    current_position = starting_location
    target_position = (risk_levels.shape[0]-1, risk_levels.shape[1]-1)

    while current_position != target_position:
        current_position = select_direction(current_position, rewards)
        accumulated_risk += int(risk_levels[current_position])

    print(accumulated_risk)

if __name__ == '__main__':
    main()