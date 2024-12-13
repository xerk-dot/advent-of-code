from aoc import get_input

def calculate_cost(input):
    regions = {}
    visited = set()
    
    def flood_fill(i, j):
        if (i < 0 or i >= len(input) or 
            j < 0 or j >= len(input[0]) or
            (i,j) in visited or
            input[i][j] != letter):
            return 0, 0, set()
            
        visited.add((i,j))
        size = 1
        perimeter1 = 0
        perimeter2 = 0
        
        # Count individual edge cells for perimeter1 and continuous edges
        for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if (ni < 0 or ni >= len(input) or 
                nj < 0 or nj >= len(input[0]) or
                input[ni][nj] != letter):
                perimeter1 += 1

        # Recursively check adjacent cells
        for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            s, p1, e = flood_fill(ni, nj)
            size += s
            perimeter1 += p1
        
        return size, perimeter1, 0

    # Find all regions
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (i,j) not in visited and input[i][j].isalpha():
                letter = input[i][j]
                region_size, perimeter1, perimeter2 = flood_fill(i, j)
                
                # Find next available suffix number for duplicate letters
                suffix = ""
                base_name = letter
                while base_name + suffix in regions:
                    if suffix == "":
                        suffix = "1"
                    else:
                        suffix = str(int(suffix) + 1)
                regions[base_name + suffix] = [region_size, perimeter1, perimeter2]
                    
    print(regions)
    return regions
def parse_input(input):
    return [[char for char in line] for line in input.splitlines()]

input = get_input(12)
input = parse_input(input)
regions = calculate_cost(input)
print("part 1:", sum(size * perimeter1 for size, perimeter1, _ in regions.values()))
print("part 2:", sum(size * perimeter2 for size, _, perimeter2 in regions.values()))
