# Import puzzle input to dict
from pathlib import Path
import math
path = Path(__file__).parent / "puzzle_inputs/2a.txt"

with open(path) as f:
    input = f.read().splitlines()

COLOUR_LIMITS = {'red': 12, 'green': 13, 'blue': 14}
# For each entry, parse into:
  # Game ID (split on colon) 
  # Game data (split on semi colon)
  # Colour (split on comma)

match_data = {}
for line in input:
    game_id, game_data = line.split(':')
    round_color_data = game_data.split(";")
    round_data = {}
    round_index = 0
    for round in round_color_data:
        colours = round.split(',')
        colour_data = {}
        for colour in colours:     
          value, colour = colour.strip().split(' ')
          colour_data[colour] = value
        round_index += 1
        round_data[round_index] = colour_data
    match_data[game_id] = round_data
  

# Data stucture is dict:
  # Game ID: Game round #: Colour - Value pairs

# Flatten dict to rounds. Get game IDs where values do not exceed limits


print(match_data)



# Find highest number of each colour in each game

game_minimum_sets = {}
for game_index, game_data in match_data.items():
    print(game_data)

    minimum_set = {}
    for round in game_data.values():
        for colour, value in round.items():
            if colour not in minimum_set:
              minimum_set[colour] = 0
            if int(value) > int(minimum_set[colour]):
              minimum_set[colour] = value
    game_minimum_sets[game_index] = minimum_set

# Find power of set
total = 0
for game_index, minimum_set in game_minimum_sets.items():
  power_set = []
  for colour, value in minimum_set.items():
    power_set.append(int(value))
  total += math.prod(power_set)

print(total)
