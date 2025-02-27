from aoc import get_input
import math
data = get_input(2).splitlines()

# Convert the string data into a 2D array of integers
data = [list(map(int, line.split())) for line in data]

count = 0
for x in data:
    if all(x[i] < x[i+1] for i in range(len(x)-1)) and all(1 <= x[i+1] - x[i] <= 3 for i in range(len(x)-1)):
        count += 1
    elif all(x[i] > x[i+1] for i in range(len(x)-1)) and all(1 <= x[i] - x[i+1] <= 3 for i in range(len(x)-1)):
        count += 1
print(count)