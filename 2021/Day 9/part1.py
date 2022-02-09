import numpy as np
from pathlib import Path
path = Path(__file__).parent / "input/input.txt"

def import_file():
    with open(path) as f:
        input_list = f.read().split('\n')

    truncated_list = list(filter(None, input_list))
    map = np.array([[int(x) for x in line] for line in truncated_list])

    return map

def get_neighbours(map, row, col):

    # Obviously replace this with some adjacency matrix or connected graph

    neighbours = []
    max_row, max_col = map.shape

    # NORTH
    if row != 0:
        neighbours.append(map[row-1][col])
    # SOUTH
    if row != (max_row-1):
        neighbours.append(map[row+1][col])
    # EAST
    if col != (max_col-1):
        neighbours.append(map[row][col+1])
    # WEST
    if col != 0:
        neighbours.append(map[row][col-1])

    return neighbours

def search_minima(map):

    local_minima = [] # -> (x, y)

    # For each value in the graph, return its neigbours
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            neighbours = get_neighbours(map, i, j)

            if element < min(neighbours):
                # print(f"Element {element} in location {i, j} has been found to be smaller than {neighbours}")
                local_minima.append((i, j))
            

    return local_minima

def calculate_risk(map, minima):
    risk = 0
    for local_minimum in minima:
        x, y = local_minimum
        risk +=  (map[x, y] + 1)

    return risk

def main():

    map = import_file()
    minima = search_minima(map)
    risk = calculate_risk(map, minima)
    print(risk)

if __name__ == '__main__':
    main()