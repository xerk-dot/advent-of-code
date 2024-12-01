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

for x in column1:
    total += x*column2.count(x)

print(total)