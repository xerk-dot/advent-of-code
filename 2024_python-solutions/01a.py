from aoc import get_input
import math
data = get_input(1).splitlines()

column1 = []
column2 = []
total = 0
for line in data:
    num1, num2 = line.split()
    column1.append(int(num1))
    column2.append(int(num2))

for x in range(len(column1)):
    total += abs(min(column1) - min(column2))
    column1.remove(min(column1))
    column2.remove(min(column2))
    print(column1)
    print(column2)
    
print(total)