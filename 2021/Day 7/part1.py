import numpy as np

def import_file():
    with open('input/input.txt') as f:
        instructions = f.read().split(',')
    instructions = np.array([int(x) for x in instructions])
    return instructions


def main():

    instructions = import_file()

    min_x = np.min(instructions)
    max_x = np.max(instructions)

    fuel_costs = {}
    for centroid in range(min_x, max_x):
        distance = np.sum([np.abs(centroid - int(x)) for x in instructions])
        fuel_costs[centroid] = distance

    print(fuel_costs[min(fuel_costs, key=fuel_costs.get)])

if __name__ == '__main__':
    main()