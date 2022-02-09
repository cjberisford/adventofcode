import os
import time

DAYS_COMPLETE = 14

for n in range(DAYS_COMPLETE):
    start = time.time()
    file_string = 'python ' + '"Day ' + str(n+1) + '/part1.py"' 
    os.system(file_string)
    finish = time.time()
    elapsed = round(finish - start, 4)
    print(f"Day {n+1} executed in {elapsed}s")
