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

@cache
def find_button_combination(ax, ay, bx, by, target_x, target_y, part2):
    if not part2:
        q = 101
        # Use simple approach for Part 1
        for a in range(q):
            for b in range(q):
                x = a * ax + b * bx
                y = a * ay + b * by
                if x == target_x and y == target_y:
                    return a, b
    else:
        # For Part 2, use linear equation solving
        # Solve: ax * a + bx * b = target_x
        #        ay * a + by * b = target_y
        det = ax * by - ay * bx
        if det == 0:  # No unique solution
            return None
            
        # Using Cramer's rule
        a = (target_x * by - target_y * bx) / det
        b = (ax * target_y - ay * target_x) / det
        
        # Check if we have integer solutions
        if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
            return int(a), int(b)
    
    return None

def calculate_tokens(machines, part2=False):
    total_tokens = 0
    
    for machine in machines:
        ax, ay = machine[0]
        bx, by = machine[1]
        target_x, target_y = machine[2]
        
        if part2:
            target_x += 10000000000000
            target_y += 10000000000000
        
        print(f"Button A: ({ax},{ay}), Button B: ({bx},{by}), Target: ({target_x},{target_y})")
        
        result = find_button_combination(ax, ay, bx, by, target_x, target_y, part2)
        if result:
            a, b = result
            tokens = a * 3 + b * 1
            total_tokens += tokens
            print(f"Found solution: A={a}, B={b}, Tokens={tokens}")
    
    return total_tokens

input_text = get_input(13)
machines = parse_input(input_text)
print("Part 1:", calculate_tokens(machines, False))
print("Part 2:", calculate_tokens(machines, True))
