from aoc import get_input
from typing import List, Tuple
from math import prod

SAMPLE_INPUT = get_input(7)

def _parse(data: str) -> Tuple[List[int], List[List[int]]]:
    parsed_data = data.splitlines()
    ids = [int(line.split(":")[0]) for line in parsed_data if line]
    values = [list(map(int, line.split(":")[1].split())) for line in parsed_data if line]
    return ids, values
    

def is_valid_combination(values: List[int], target: int) -> bool:
    # Try all possible ways to combine numbers using + and *
    def try_combinations(nums: List[int], current_result: int, ops_used: List[str]) -> bool:
        if len(nums) == 0:
            if current_result == target:
                print(" ".join([str(values[0])] + [f"{op} {num}" for op, num in zip(ops_used, values[1:])]) + " = " + str(target))
            return current_result == target
        
        num = nums[0]
        remaining = nums[1:]
        
        if try_combinations(remaining, current_result + num, ops_used + ["+"]):
            return True
            
        if try_combinations(remaining, current_result * num, ops_used + ["*"]):
            return True
        
        if try_combinations(remaining, int(str(current_result) + str(num)), ops_used + ["||"]):
            return True
        
        return False
    
    # Start with first number and try all combinations
    return try_combinations(values[1:], values[0], [])


def solution(ids: List[int], values: List[List[int]]) -> int:
    counter = 0
    for x in range(len(ids)):
        if is_valid_combination(values[x], ids[x]):
            counter += ids[x]
    return counter

print(SAMPLE_INPUT)
ids, values = _parse(SAMPLE_INPUT)
print(ids)
print(values)
print(solution(ids, values))

