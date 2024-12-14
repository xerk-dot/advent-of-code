from aoc import get_input
from collections import defaultdict
import re
import numpy as np
def parse_input(input_lines):
    robots = []
    for line in input_lines.splitlines():
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
        robots.append(((px, py), (vx, vy)))
    return robots

def simulate_step(pos, vel, width, height):
    new_x = (pos[0] + vel[0]) % width
    new_y = (pos[1] + vel[1]) % height
    return (new_x, new_y)

def count_quadrants(positions, width, height):
    quadrants = defaultdict(int)
    mid_x = width // 2
    mid_y = height // 2
    
    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        quadrant = (int(x > mid_x)) + (2 * int(y > mid_y))
        quadrants[quadrant] += 1
    
    return [quadrants[i] for i in range(4)]

def solve(input_data):
    robots = parse_input(input_data)
    width, height = 101, 103
    
    positions = [pos for pos, _ in robots]
    velocities = [vel for _, vel in robots]
    
    for second in range(100):
        
        new_positions = []
        for pos, vel in zip(positions, velocities):
            new_pos = simulate_step(pos, vel, width, height)
            new_positions.append(new_pos)
        positions = new_positions
    
    quadrant_counts = count_quadrants(positions, width, height)
    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count
    
    return safety_factor

data = get_input(14)
print(solve(data))