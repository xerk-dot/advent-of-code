from aoc import get_input
import re
from math import gcd
from functools import cache

def parse_input(input_text):
    machines = []
    current_machine = []
    
    for line in input_text.strip().split('\n'):
        if line:
            numbers = [int(x) for x in re.findall(r'[+-]?\d+', line)]
            if line.startswith('Prize'):
                numbers = [abs(x) for x in numbers]
            current_machine.append(numbers)
            if len(current_machine) == 3:
                machines.append(current_machine)
                current_machine = []
    
    return machines

def calculate_tokens(machines):
    total_tokens = 0
    
    for machine in machines:
        ax, ay = machine[0]  # Button A's effect on (x,y)
        bx, by = machine[1]  # Button B's effect on (x,y)
        target_x, target_y = machine[2]  # Target coordinates
        
        print(f"Button A: ({ax},{ay}), Button B: ({bx},{by}), Target: ({target_x},{target_y})")
        
        # Try all possible combinations of button presses up to 100
        found_solution = False
        for a in range(101):
            for b in range(101):
                x = a * ax + b * bx
                y = a * ay + b * by
                if x == target_x and y == target_y:
                    tokens = a * 3 + b * 1
                    total_tokens += tokens
                    print(f"Found solution: A={a}, B={b}, Tokens={tokens}")
                    found_solution = True
                    break
            if found_solution:
                break
    
    return total_tokens

input_text = get_input(13)
machines = parse_input(input_text)
result = calculate_tokens(machines)
print("Part 1:", result)
