import re
import numpy as np

def import_file():
    with open('input/input.txt') as f:
        file = f.read().split('\n')

    index = file.index('')
    split_file = [file[:index], file[index + 1:]]

    dot_coords = [tuple(x.split(',')) for x in split_file[0]]

    pattern_text = r'(?P<name>\w)[=:](?P<value>.*)'
    pattern = re.compile(pattern_text)
    instruction_groups = [re.search(pattern, n) for n in split_file[1]]
    instructions = [(n.group(1), n.group(2)) for n in instruction_groups]

    return dot_coords, instructions

def draw_dots(dot_coords):
    # Get max width (x) and height (y)
    width = max([int(coord[0]) for coord in dot_coords]) + 1
    height = max([int(coord[1]) for coord in dot_coords]) + 1
    grid = np.zeros((height, width), dtype=float)

    for x, y in dot_coords:
        grid[int(y)][int(x)] = '1'

    return grid

def fold_paper(fold, paper):

    fold_position = int(fold[1]) 

    # Establish fold position
    if fold[0] == 'y':
        # Do vertical fold
        top = paper[:fold_position]
        bottom = paper[fold_position+1:]

        # Flip bottom and add it to top
        bottom_flipped = np.flip(bottom, axis=0)
        top += bottom_flipped

        paper = top
    else:
        # Do horizontal fold
        left = paper[:,:fold_position]
        right = paper[:,fold_position+1:]

        # Flip right and add it to left
        right_flipped = np.flip(right, axis=1)
        left += right_flipped

        paper = left

    return paper
 
    
def main():
    dot_coords, instructions = import_file()
    paper = draw_dots(dot_coords)

    for fold in instructions:
        paper = fold_paper(fold, paper)

    print(paper)
    print(np.count_nonzero(paper))

    # Replace nonzero elements
    paper = np.where(paper>0, 1, paper) 
    print(paper)

if __name__ == '__main__':
    main()