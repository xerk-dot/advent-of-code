from aoc import get_input

def parse_input(data):
    """Parse input into patterns and designs."""
    patterns_str, designs_str = data.strip().split('\n\n')
    patterns = [p.strip() for p in patterns_str.split(',')]
    designs = designs_str.splitlines()
    return patterns, designs

def count_ways(design, patterns, memo=None):
    """Count number of ways to make design using available patterns."""
    if memo is None:
        memo = {}
    
    # Base case: empty design has one way to make it
    if not design:
        return 1
    
    # Check memoization
    if design in memo:
        return memo[design]
    
    # Try each pattern at the start of the design
    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            # Add ways to make the rest of the design
            total_ways += count_ways(design[len(pattern):], patterns, memo)
    
    memo[design] = total_ways
    return total_ways

def solve_part1(data):
    patterns, designs = parse_input(data)
    possible = sum(1 for design in designs if count_ways(design, patterns) > 0)
    return possible

def solve_part2(data):
    patterns, designs = parse_input(data)
    total_ways = sum(count_ways(design, patterns) for design in designs)
    return total_ways

if __name__ == "__main__":
    # Part 1
    result = solve_part1(get_input(19))
    print(f"Number of possible designs: {result}")
    
    # Part 2
    result = solve_part2(get_input(19))
    print(f"Total number of ways to make all designs: {result}")
