import re
from pathlib import Path
path = Path(__file__).parent / "puzzle_inputs/1a.txt"

with open(path) as f:
    input = f.read().splitlines()

example_input = ['a1abc2a','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']

line_result = []
for line in input:
  match = re.search(r'\d', line)
  if match:
    first_digit = match.group()

  reverse_match = re.search(r'\d', line[::-1])
  if reverse_match:
    final_digit = reverse_match.group()

  # Concat values and store in line result array
    line_total = first_digit + final_digit
    line_result.append(int(line_total))


# Sum elements in line result array
solution = sum(line_result)
print(solution)