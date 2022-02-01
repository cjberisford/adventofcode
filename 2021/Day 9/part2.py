import numpy as np

def import_file():
    with open('input/input.txt') as f:
        input_list = f.read().split('\n')

    truncated_list = list(filter(None, input_list))
    map = np.array([[int(x) for x in line] for line in truncated_list])

    return map

def basin_BFS(map, row, col, visited):

    # Obviously replace this with some adjacency matrix or connected graph
    max_row, max_col = map.shape
    # visited.append((row, col))
    viable_neighbours = []

    # BASE CASE, location size 1
    basin_size = 1

    # NORTH
    if row != 0 and map[row-1][col] != 9:
        viable_neighbours.append((row-1, col))
    # SOUTH
    if row != (max_row-1) and map[row+1][col] != 9:
        viable_neighbours.append((row+1, col))
    # EAST
    if col != (max_col-1) and map[row][col+1] != 9:
        viable_neighbours.append((row, col+1))
    # WEST
    if col != 0 and map[row][col-1] != 9:
        viable_neighbours.append((row, col-1))

    # Filter previously existing neighbours

    visited.append((row, col))

    # print(viable_neighbours)

    for (row, col) in viable_neighbours:
        if (row, col) not in visited:
            basin_size += basin_BFS(map, row, col, visited)

    # print(f"Element at {row, col} has viable_neighbours at {viable_neighbours}")
    return basin_size

def scan_surface(map):

    basin_sizes = [] # -> (x, y)

    # For each value in the graph, return a BFS of all neighbours
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element != 9:
                basin_size = basin_BFS(map, i, j, [])
                basin_sizes.append(basin_size)
            
    return list(set(basin_sizes))

def main():

    map = import_file()
    basin_sizes = scan_surface(map)

    # Multiply three largest elements of set
    largest_basins = basin_sizes[-3:]
    solution = np.product(largest_basins)
    print(solution)

if __name__ == '__main__':
    main()