from aoc import get_input

def calculate_id(numbers: list[int]) -> int:
    total = 0
    counter = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] != ".":
                total += numbers[i][j] * counter
                counter += 1
    return total

def find_earliest_dot(numbers: list[list[str]]) -> list[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] == ".":
                return [i, j]
    return [-1, -1]  # Return [-1,-1] if no dot is found

def move_file_blocks(numbers: list[list[str]]) -> list[list[str]]:
    n = len(numbers)
    for i in range(n-1, -1, -1):
        for j in range(len(numbers[i])-1, -1, -1):
            dot_pos = find_earliest_dot(numbers)
            print(f"i: {i}, j: {j}")
            print(f"dot_pos: {dot_pos}")

            if numbers[i][j] != ".":  # Only process non-dot elements
                if dot_pos != [-1, -1] and dot_pos[0] <= i:
                    numbers[dot_pos[0]][dot_pos[1]] = numbers[i][j]
                    print("Successfully moved: " + str(numbers[i][j]))
                    numbers[i][j] = "."
                else:
                    break;
        if i<=10500:
            break;
    return numbers

def place_dots(numbers: list[list[str]]) -> list[list[str]]:
    counter = 0
    for i in range(len(numbers)):
        if counter % 2 == 0:
            numbers[counter] = [counter//2] * numbers[i]
        else:
            numbers[counter] = ["."] * numbers[i]
        counter += 1
    return numbers

def main():
    input = get_input(9)
    numbers = [int(digit) for digit in input]
    #part 1
    numbers = place_dots(numbers)

       #numbers = move_file_blocks(numbers)
 

    with open('solutions/10b.txt', 'w') as f:
        for row in numbers:
            f.write("["+' '.join(str(x) for x in row) + "]\n")
    
    print(calculate_id(numbers))

if __name__ == "__main__":
    main()
