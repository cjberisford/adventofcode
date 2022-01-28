from input_parse import *
import numpy as np
import matplotlib.pyplot as plt
import part2
import math

def euclidean_distance(x1, x2, y1, y2):
    a = np.array((int(x1), int(y1)))
    b = np.array((int(x2), int(y2)))
    return np.linalg.norm(a-b)


def main():
    # Create empty grid
    k = len(lines)
    vents = np.zeros([1000, 1000])

    for coords in coordinates:

        x1, y1 = coords[0].split(',')
        x2, y2 = coords[1].split(',')

        # For horizontal vents
        if y1 == y2 and x1 != x2:
            start_x, end_x = int(x1), int(x2)
            if start_x <= end_x:
                vents[int(y1)][start_x:end_x+1] += 1
            else:
                vents[int(y1)][end_x:start_x+1] += 1

        # For vertical vents
        if x1 == x2 and y1 != y2:
            start_y, end_y = int(y1), int(y2)
            if start_y <= end_y:
                vents.T[int(x1)][start_y:end_y+1] += 1
            else:
                vents.T[int(x1)][end_y:start_y+1] += 1


        # For diagonal lines
        if x1 != x2 and y1 != y2:
            vents = part2.draw_diagonal_line(vents, int(x1), int(x2), int(y1), int(y2))

        # For points
        if x1 == x2 and y1 == y2:
            print("Point detected")
    
    unique, counts = np.unique(vents, return_counts=True)
    counts = dict(zip(unique, counts))
    solution = sum(item for key, item in counts.items() if key >= 2)
    print(solution)

    # Create visualisation
    pixel_plot = plt.imshow(vents, cmap='Greens', interpolation='nearest', origin='lower') 
    plt.colorbar(pixel_plot)
    plt.gca().invert_yaxis()
    plt.savefig('output/pixel_plot.png')

if __name__ == '__main__':
    main()