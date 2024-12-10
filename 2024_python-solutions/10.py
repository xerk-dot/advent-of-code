from aoc import get_input

def print_mountains(mountains):
    for row in mountains:
        print(''.join(str(x) for x in row))

def part1(mountains, trailheads):
    def bfs(start_i, start_j):
        queue = [(start_i, start_j)]
        visited = {(start_i, start_j)}
        paths = 0
        
        while queue:
            i, j = queue.pop(0)
            curr_height = mountains[i][j]
            
            if curr_height == 9:
                paths += 1
                continue
                
            # Check adjacent cells (up, down, left, right)
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if (0 <= ni < len(mountains) and 
                    0 <= nj < len(mountains[0]) and 
                    (ni,nj) not in visited and
                    mountains[ni][nj] == curr_height + 1):
                    queue.append((ni, nj))
                    visited.add((ni, nj))
        
        return paths

    for i in range(len(mountains)):
        for j in range(len(mountains[i])):
            if mountains[i][j] == 0:
                trailheads[i][j] = bfs(i, j)
                    
    print_mountains(trailheads)
    return sum(sum(row) for row in trailheads)

def part2(mountains, trailheads):
    def count_paths(start_i, start_j, curr_path=None):
        if curr_path is None:
            curr_path = [(start_i, start_j)]
            
        i, j = curr_path[-1]
        curr_height = mountains[i][j]
        
        if curr_height == 9:
            return 1
            
        total_paths = 0
        # Check adjacent cells (up, down, left, right)
        for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if (0 <= ni < len(mountains) and 
                0 <= nj < len(mountains[0]) and 
                (ni,nj) not in curr_path and
                mountains[ni][nj] == curr_height + 1):
                curr_path.append((ni, nj))
                total_paths += count_paths(start_i, start_j, curr_path)
                curr_path.pop()
                
        return total_paths

    for i in range(len(mountains)):
        for j in range(len(mountains[i])):
            if mountains[i][j] == 0:
                trailheads[i][j] = count_paths(i, j)
                    
    print_mountains(trailheads)
    return sum(sum(row) for row in trailheads)


if __name__ == "__main__":
    input = get_input(10)
    mountains = [[int(digit) for digit in line] for line in input.split('\n') if line]
    trailheads = [[0 for digit in line] for line in input.split('\n') if line]
    print(part1(mountains, trailheads))
    print(part2(mountains, trailheads))
