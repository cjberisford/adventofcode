# Import puzzle input to dict
from pathlib import Path
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

possible_game_indices = []
for game_index, game_data in match_data.items():
    fail = False
    for round, colours in game_data.items():
        for colour, value in colours.items():
            if int(value) > int(COLOUR_LIMITS[colour]):
                fail = True
    if not fail:
        game_index_int = game_index.split(' ')[1]
        possible_game_indices.append(int(game_index_int))
    

# Sum these values
print(sum(possible_game_indices))
