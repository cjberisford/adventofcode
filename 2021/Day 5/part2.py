def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return int(m)

def draw_diagonal_line(vents, x1, x2, y1, y2):

    if x2 >= x1:
        # LTR rise OR LTR fall
        adj_x1 = x1
        adj_x2 = x2
        adj_y1 = y1
        adj_y2 = y2
    else:
        # RTL rise OR RTL fall (Change to LTR rise or LTR fall)
        adj_x1 = x2
        adj_x2 = x1
        adj_y1 = y2
        adj_y2 = y1

    # Determine orientation of line
    m = slope(int(adj_x1), int(adj_y1), int(adj_x2), int(adj_y2))

    i = range(adj_x1, adj_x2+1)
    j = range(adj_y1, adj_y2+m, m)

    # Draw line
    for i, j in zip(i, j):
        vents[j][i] += 1

    return vents