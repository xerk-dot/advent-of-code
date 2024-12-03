from aoc import get_input
import math
import re

data = get_input(3).splitlines()


pattern = r'mul\((\d+),\s*(\d+)\)'

total = 0
for line in data:
    matches = re.findall(pattern, line)
    print(matches)
    total += sum([int(x[0]) * int(x[1]) for x in matches])
    
print(total)


