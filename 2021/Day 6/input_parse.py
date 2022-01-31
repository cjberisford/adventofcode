with open('input/example.txt') as f:
    fish_list = f.read().split(',')

fish_list = [int(x) for x in fish_list]