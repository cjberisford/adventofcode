from pathlib import Path
path = Path(__file__).parent / "input/input.txt"

with open(path) as f:
    lines = f.read().split('\n')

coordinates = []
for line in lines:
    x1y1, _, x2y2 = line.partition(" -> ")
    coordinates.append((x1y1, x2y2))