import numpy as np
import sys
import part1
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

def increment(x, n, k):
    y = int(x) + n + k
    if y > 9: y = y - 9
    return y

def unfold_map(risk_levels):

    rows = []
    for k in range(5):
        cols = []
        for n in range(5):

            cols.append(np.array([[increment(x, n, k) for x in row] for row in risk_levels]))

        rows.append(np.concatenate(np.array(cols), axis=1))
    new_map = np.concatenate(np.array(rows), axis=0)

    return new_map

def forward_pass(rewards, risk_levels, cascade):

    height, width = risk_levels.shape
    test_inc = 0

    for k in range(height+1):
        for row, col in zip(range(k), range(k-1, -1, -1)):

            current_risk = int(risk_levels[row][col])
            current_reward = rewards[row][col]
            north_reward = rewards[row-1][col]
            west_reward = rewards[row][col-1]

            lowest_weight = min(north_reward, west_reward)
            if row == 0:
                # Cell is at the top, so check value from left
                lowest_weight = rewards[row][col-1]
            if col == 0: 
                # Cell is at left, so check value above
                lowest_weight = rewards[row-1][col]
            if row == 0 and col == 0:
                # Cell is top left, so don't change
                continue

            if (lowest_weight + current_risk) < current_reward:
            
                cascade += 1

                rewards[row][col] = lowest_weight + current_risk         


        
    for k in range(height+1):
        for row, col in zip(range(height-1, k, -1), range(k+1, height+1, 1)):
            current_risk = int(risk_levels[row][col])
            current_reward = rewards[row][col]
            north_reward = rewards[row-1][col]
            west_reward = rewards[row][col-1]

            lowest_weight = min(north_reward, west_reward)

            if (lowest_weight + current_risk) < current_reward:

                cascade += 1

                rewards[row][col] = lowest_weight + current_risk      

    return rewards, cascade 
    

def main():

    risk_levels = part1.import_file()
    entire_risk_levels = risk_levels
    entire_risk_levels = unfold_map(risk_levels)
    rewards = part1.calculate_weights(entire_risk_levels)

    cascade = 1
    while cascade > 0:
        cascade = 0
        rewards, cascade = forward_pass(rewards, entire_risk_levels, cascade)
        print(cascade)

    accumulated_risk = 0
    starting_location = (0, 0)

    current_position = starting_location
    target_position = (entire_risk_levels.shape[0]-1, entire_risk_levels.shape[1]-1)

    while current_position != target_position:
        current_position = part1.select_direction(current_position, rewards)
        accumulated_risk += int(entire_risk_levels[current_position])
        # rewards[current_position] = np.inf

    print(accumulated_risk)

    plt.rcParams["figure.figsize"] = (10, 10)
    masked_array = np.ma.masked_where(rewards == np.inf, rewards)
    plt.imshow(entire_risk_levels, interpolation='none')
    cmap = plt.cm.binary
    cmap = plt.cm.get_cmap("binary").copy()
    cmap.set_bad(color='red')
    plt.axis('off')
    plt.imshow(masked_array, cmap=cmap)
    plt.savefig('output/path_3.png')


if __name__ == '__main__':
    main()