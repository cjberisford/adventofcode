import time
import numpy as np

def parse_board(string):
    parse = string.split('\n')
    arr = []
    for line in parse:
        arr.append([x for x in line.split(' ') if x])
    return [x for x in arr if x]


def check_winner(board):
    # Count row Xs
    for row in board:
        count = list(row).count('x')
        if count >= 5: 
            return True
    
    # Count col Xs
    for i in range(5):
        count = 0
        for row in board:
            if row[i] == 'x':
                count += 1
        if count >= 5:
            return True

    
start = time.perf_counter()

winner_found = False
winning_board = []

boards = []
with open('input/input.txt') as f:
    boards = f.read().split('\n\n')

draw_order = boards[0].split(',')
parsed_boards = [parse_board(board) for board in boards[1:]]
winner_found = False
winning_number = 0
for n in draw_order:
    parsed_boards = [[['x' if b == n else b for b in row] for row in board] for board in parsed_boards]

    # Check for winner
    for board in parsed_boards:
        if(check_winner(board)):
            winner_found = True
            winning_board = board
            winning_number = n
            break

    if winner_found:
        break

# Add all unmarked numbers together
total = 0
for row in winning_board:
    for number in row:
        if number != 'x':
            total += int(number)

print(winning_number)
print(total * int(winning_number))

     
stop = time.perf_counter()
print(f"Executed in {stop-start:0.4f} seconds")

