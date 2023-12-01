import re
from pathlib import Path
path = Path(__file__).parent / "puzzle_inputs/1a.txt"

with open(path) as f:
    input = f.read().splitlines()

example_input = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']

def get_digit(digitString):
  number_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
  }
  
  if digitString.isalpha():
    return str(number_mapping[digitString])
  else: 
    return digitString

line_result = []
for line in input:
  pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
  reversed_pattern = r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'
  matches = re.findall(pattern, line)
  reversed_matches = re.findall(reversed_pattern, line[::-1])
  if matches:
    first_digit = get_digit(matches[0])
    final_digit = get_digit(reversed_matches[0])

    # Concat values and store in line result array
    line_total = first_digit + final_digit
    line_result.append(int(line_total))

# Sum elements in line result array
solution = sum(line_result)
print(solution)