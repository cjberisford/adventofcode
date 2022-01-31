import xdrlib
import numpy as np

def import_file():
    with open('input/example.txt') as f:
        instructions = f.read().split(',')
    instructions = np.array([int(x) for x in instructions])
    return instructions

def compute_sequence(max_x):

    costs = {}
    total = 0
    values = []
    for i in range(max_x+1):
        values.append(i)
        costs[i] = sum(values)

    return costs

def main():

    instructions = import_file()

    max_x = np.max(instructions)

    fuel_index = compute_sequence(max_x)

    print(fuel_index)

    fuel_costs = {}
    for centroid in range(max_x):
        distance = np.sum([fuel_index[np.abs(centroid - int(x))] for x in instructions])
        fuel_costs[centroid] = distance

    print(fuel_costs[min(fuel_costs, key=fuel_costs.get)])

if __name__ == '__main__':
    main()