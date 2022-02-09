from pathlib import Path
path = Path(__file__).parent / "input/input.txt"

with open(path) as f:
    fish_list = f.read().split(',')

fish_list = [int(x) for x in fish_list]