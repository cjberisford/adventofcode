from part1 import parse_board, check_winner, sum_board
import time

start = time.perf_counter()

boards = []
with open('input/input.txt') as f:
    boards = f.read().split('\n\n')

draw_order = boards[0].split(',')
parsed_boards = [parse_board(board) for board in boards[1:]]

total_boards = len(parsed_boards)


losing_board_located = False
for n in draw_order:
    parsed_boards = [[['x' if b == n else b for b in row] for row in board] for board in parsed_boards]

    losing_boards = []
    for board in parsed_boards:
        if not check_winner(board):
            losing_boards.append(board)

    if len(losing_boards) == 1:
        # Identified last board to win
        losing_board = losing_boards[0]

for n in draw_order:
    losing_board = [['x' if b == n else b for b in row] for row in losing_board]
    if check_winner(losing_board):
        losing_number = n
        break

 
total = sum_board(losing_board)

print(losing_number)
print(total * int(losing_number))


stop = time.perf_counter()
print(f"Executed in {stop-start:0.4f} seconds")


