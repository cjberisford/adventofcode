commands = []
with open("input/input.txt") as f:
    for line, instruction in enumerate(f):
        command, scalar = instruction.split()
        commands.append((command, int(scalar)))

horizontal_position = 0
depth = 0

for i, (command, scalar) in enumerate(commands):
    if command == 'up':
        depth -= scalar
    elif command == 'down':
        depth += scalar
    elif command == 'forward':
        horizontal_position += scalar

print(horizontal_position*depth)