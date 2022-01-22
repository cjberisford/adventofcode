commands = []
with open("input/input.txt") as f:
    for line, instruction in enumerate(f):
        command, scalar = instruction.split()
        commands.append((command, int(scalar)))

horizontal_position = 0
depth = 0
aim = 0

for i, (command, scalar) in enumerate(commands):
    if command == 'up':
        aim -= scalar
    elif command == 'down':
        aim += scalar
    elif command == 'forward':
        horizontal_position += scalar
        depth += (aim*scalar)

print(horizontal_position*depth)