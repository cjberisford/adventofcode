import numpy as np

from pathlib import Path
path = Path(__file__).parent / "input/input.txt"

STEPS = 1000

def import_file():
    with open(path) as f:
        input_list = f.read().split('\n')

    map = np.array([[int(octopus) for octopus in line] for line in input_list])
    return map

def update_neighbour(octopus_map, row, col, locations, flash_count):

    max_row, max_col = octopus_map.shape

    # UPDATE N
    if row > 0:
        octopus_map[row-1][col] += 1
        if octopus_map[row-1][col] == 10:
            flash_count += 1
            locations.append((row-1, col))
    # UPDATE NE
    if row > 0 and col < (max_col-1):
        octopus_map[row-1][col+1] += 1
        if octopus_map[row-1][col+1] == 10:
            flash_count += 1
            locations.append((row-1, col+1))
    # UPDATE E
    if col < (max_col-1):
        octopus_map[row][col+1] += 1
        if octopus_map[row][col+1] == 10:
            flash_count += 1
            locations.append((row, col+1))
    # UPDATE SE
    if row < (max_row-1) and col < (max_col-1):
        octopus_map[row+1][col+1] += 1
        if octopus_map[row+1][col+1] == 10:
            flash_count += 1
            locations.append((row+1, col+1))
    # UPDATE S
    if row < (max_row-1):
        octopus_map[row+1][col] += 1
        if octopus_map[row+1][col] == 10:
            flash_count += 1
            locations.append((row+1, col))
    # UPDATE SW 
    if row < (max_row-1) and col > 0:
        octopus_map[row+1][col-1] += 1
        if octopus_map[row+1][col-1] == 10:
            flash_count += 1
            locations.append((row+1, col-1))
    # UPDATE W
    if col > 0:
        octopus_map[row][col-1] += 1
        if octopus_map[row][col-1] == 10:
            flash_count += 1
            locations.append((row, col-1))
    # UPDATE NW
    if row > 0 and col > 0:
        octopus_map[row-1][col-1] += 1
        if octopus_map[row-1][col-1] == 10:
            flash_count += 1
            locations.append((row-1, col-1))

    return octopus_map, locations, flash_count


def propagate_flashes(octopus_map, locations, flash_count, flash_history):

    # Remove locations that have already flashed this step
    to_remove = []
    for location in locations:
        if location in set(flash_history):
            to_remove.append(location)
    for location in to_remove:
        locations.remove(location)

    # Base case, exit when propagation finished
    if len(locations) == 0:
        # Base case - no more octopus to flash
        return octopus_map, locations, flash_count, flash_history

    # Propagate flash
    for location in set(locations):
        if location not in flash_history:
            # Flash event, so update neighbours 
            row, col = location
            octopus_map, locations, flash_count = update_neighbour(octopus_map, row, col, locations, flash_count)
            flash_history.append((row, col))

    return octopus_map, locations, flash_count, flash_history


def main():

    octopus_map = import_file()
    flash_count = 0
    for step in range(STEPS):

        # PART 2
        if (np.sum(octopus_map) == 0):
            print(step)
            break

        # Increment octopi
        octopus_map += 1

        # Process any naturally occuring flashes (where octopus == 9)
        flash_count += np.sum(octopus_map >= 10)


        # # Propagate flashes recursively until location list empty
        locations = [(ix,iy) for ix, row in enumerate(octopus_map) for iy, i in enumerate(row) if i >= 10]
        flash_history = []
        while len(locations) > 0:
            octopus_map, locations, flash_count, flash_history = propagate_flashes(octopus_map, locations, flash_count, flash_history)

        # Reset flashed octopi to 0
        octopus_map = np.where(octopus_map>=10, 0, octopus_map) 


    print(flash_count)

if __name__ == '__main__':
    main()