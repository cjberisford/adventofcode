import re
from pathlib import Path
path = Path(__file__).parent / "puzzle_inputs/3a.txt"

def check_cell_adjacency(matrix, row1, col1, row2, col2):
  rows, cols = len(matrix), len(matrix[0])

  # Check if the indices are within the valid range
  if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
    # Check if the cells are adjacent
    return abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1
  else:
    # Indices are out of range
    return False

with open(path) as f:
    input = f.read().splitlines()

# Get total of all numbers in grid
total = 0
for row in input:
    # Define the regular expression pattern for matching numbers
    pattern = r'\b\d+\b'

    # Use re.findall to find all occurrences of the pattern in the string
    numbers = re.findall(pattern, row)
   
    total += sum(numbers)

    # Find all total of all non-part numnbers

    for col in row:
      # Test if the character is numeric
      
      part_number = []
      if col.isnumeric():
        index_of_number = (input.index(col), row.index(col))
        part_number.append(index_of_number)
      else:
        

      # If it is, we've found a number so we need to:
       
      # store the current row, colum index
       
      # Find the number by concatenating all subsequenct chars
       
      # When we encounter a non-integer, the number is complete
       
      # Find the length of this number.
       
      # Now we can look to the left, right, and above (length + 2)
      # and below (length + 2). Add these characters to an array
       
      # Check the array for a presence of a symbol. 
       
      # If no symbol, add the original number to an array
       

       
      
    


