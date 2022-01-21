with open('input/input.txt') as f:
    depths = f.read().splitlines()

count = 0

for i, depth in enumerate(depths, 1):
    if depth > depths[i-2]:
        count += 1

# Solution to part 1: 1121
print(count)

