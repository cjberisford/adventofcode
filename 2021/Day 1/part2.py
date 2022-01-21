with open('input/input.txt') as f:
    depths = f.read().splitlines()

print(depths)

count = 0


# Create new list with rolling sum
windows = []
i = 0
while i < (len(depths) - 2):
    windows.append(int(depths[i]) + 
                   int(depths[i+1]) + 
                   int(depths[i+2]))
    i += 1


for i, window in enumerate(windows, 1):
    if window > windows[i-2]:
        count += 1

# Solution to part 1: 1121
print(count)

