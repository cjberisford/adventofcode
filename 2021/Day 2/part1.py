from pathlib import Path
path = Path(__file__).parent / "input/input.txt"

commands = []
with open(path) as f:
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