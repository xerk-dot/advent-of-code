from aoc import get_input

def parse_input(filename):
    
    lines = filename.splitlines()
    
    # Find where the map ends and movements begin
    map_lines = []
    for line in lines:
        if not line or all(c in '<>^v' for c in line):
            break
        map_lines.append(line)
    
    # Get movements (combine all remaining non-empty lines)
    movements = ''.join(line for line in lines[len(map_lines):] if line)
    
    return map_lines, movements

def find_robot_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                return (x, y)
    return None

def can_move(grid, pos, direction):
    new_x = pos[0] + direction[0]
    new_y = pos[1] + direction[1]
    
    # Check if position is within bounds and not a wall
    if (0 <= new_y < len(grid) and 
        0 <= new_x < len(grid[0]) and 
        grid[new_y][new_x] != '#'):
        return True
    return False

def try_move(grid, pos, direction):
    new_x = pos[0] + direction[0]
    new_y = pos[1] + direction[1]
    
    # If the new position contains a box
    if grid[new_y][new_x] == 'O':
        box_new_x = new_x + direction[0]
        box_new_y = new_y + direction[1]
        
        # Check if box can be pushed
        if (0 <= box_new_y < len(grid) and 
            0 <= box_new_x < len(grid[0]) and 
            grid[box_new_y][box_new_x] in '.@'):
            # Move box
            grid[box_new_y][box_new_x] = 'O'
            grid[new_y][new_x] = '@'
            grid[pos[1]][pos[0]] = '.'
            return True
        return False
    
    # If the new position is empty
    elif grid[new_y][new_x] == '.':
        grid[new_y][new_x] = '@'
        grid[pos[1]][pos[0]] = '.'
        return True
    
    return False

def calculate_gps_sum(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                total += (100 * y + x)
    return total

def solve(filename):
    # Parse input
    map_lines, movements = parse_input(filename)
    
    # Convert map to grid
    grid = [list(line) for line in map_lines]
    
    # Direction mappings
    directions = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    
    # Process movements
    for move in movements:
        robot_pos = find_robot_position(grid)
        direction = directions[move]
        
        if can_move(grid, robot_pos, direction):
            try_move(grid, robot_pos, direction)
    
    # Calculate final GPS sum
    return calculate_gps_sum(grid)

if __name__ == "__main__":
    result = solve(get_input(15))
    print(f"The sum of all boxes' GPS coordinates is: {result}")