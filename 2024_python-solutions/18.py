from collections import deque
from aoc import get_input

def parse_input(data):
    """Parse input into list of (x,y) coordinates."""
    return [tuple(map(int, line.split(','))) for line in data.splitlines()]

def create_grid(corrupted_positions, size=71):
    """Create grid with corrupted positions marked."""
    grid = [[False] * size for _ in range(size)]
    for x, y in corrupted_positions:
        grid[y][x] = True
    return grid

def find_shortest_path(grid):
    """Find shortest path from (0,0) to (size-1,size-1) avoiding corrupted positions."""
    size = len(grid)
    queue = deque([(0, 0, 0)])  # (x, y, steps)
    visited = {(0, 0)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y, steps = queue.popleft()
        
        if x == size-1 and y == size-1:
            return steps
            
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 <= new_x < size and 
                0 <= new_y < size and 
                not grid[new_y][new_x] and 
                (new_x, new_y) not in visited):
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
    
    return None

def solve(data):
    # Parse first 1024 corrupted positions
    corrupted = parse_input(data)[:1024]
    
    # Create grid with corrupted positions
    grid = create_grid(corrupted)
    
    # Find shortest path
    return find_shortest_path(grid)

def solve_part2(data):
    """Find first byte that blocks all paths to exit."""
    corrupted = parse_input(data)
    size = 71
    
    # Try each byte in sequence
    for i, (x, y) in enumerate(corrupted):
        # Create grid with corrupted positions up to this byte
        grid = create_grid(corrupted[:i+1], size)
        
        # Check if path exists
        if find_shortest_path(grid) is None:
            return f"{x},{y}"
    
    return None

if __name__ == "__main__":
    # Part 1
    result = solve(get_input(18))
    print(f"Minimum steps needed to reach the exit: {result}")
    
    # Part 2
    result = solve_part2(get_input(18))
    print(f"First blocking byte coordinates: {result}")
