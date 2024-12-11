from aoc import get_input

def count_digits(n):
    # Faster way to count digits without string conversion
    if n == 0:
        return 1
    count = 0
    while n:
        count += 1
        n //= 10
    return count

def solution(data, blinks):
    # Convert data to list if it isn't already
    data = list(data)
    
    for _ in range(1, blinks+1):
        i = 0
        while i < len(data):
            num = data[i]
            
            # Use direct integer comparison instead of string conversion for zero check
            if num == 0:
                data[i] = 1
            else:
                # Calculate even/odd length without string conversion
                num_length = count_digits(num)
                
                if num_length % 2 == 0:
                    # Split number using integer division
                    divisor = 10 ** (num_length // 2)
                    right_half = num % divisor
                    left_half = num // divisor
                    data[i] = left_half
                    data.insert(i + 1, right_half)
                    i += 1
                else:
                    data[i] = num * 2024
            i += 1
            
        if _ % 2 == 0:  # Only print every 10th blink to reduce I/O
            print(f"blink: {_}")
    
    return data

def parse_input(input_str):
    return [int(num) for num in input_str.split()]

if __name__ == "__main__":
    data = parse_input(get_input(11))
    print(len(solution(data,25)))

