from aoc import get_input
from typing import List, Tuple

SAMPLE_INPUT = get_input(8)


def _parse(data: str) -> List[List[str]]:
    return [list(row) for row in data.split('\n')]

def find_all_coordinates_on_same_line(x1: int, y1: int, x2: int, y2: int) -> List[List[int]]:
    
    # Get the step sizes
    step_x = x2 - x1
    step_y = y2 - y1
    
    # Start with original points
    coordinates = [[x1, y1], [x2, y2]]
    
    # Add points before x1,y1
    curr_x = x1 - step_x
    curr_y = y1 - step_y
    while 0 <= curr_x < 50 and 0 <= curr_y < 50:
        coordinates.append([curr_x, curr_y])
        curr_x -= step_x
        curr_y -= step_y
        
    # Add points after x2,y2
    curr_x = x2 + step_x
    curr_y = y2 + step_y
    while 0 <= curr_x < 50 and 0 <= curr_y < 50:
        coordinates.append([curr_x, curr_y])
        curr_x += step_x
        curr_y += step_y
    return [coord for coord in coordinates if 0 <= coord[0] < 50 and 0 <= coord[1] < 50]


def find_two_coordinates_on_same_line(x1: int, y1: int, x2: int, y2: int) -> List[List[int]]:
    # Assuming the coordinates are on the same line, we can find the slope and intercept of the line
    # Then we can find the other two coordinates on the line

    x0 = x1-(x2-x1)
    y0 = y1-(y2-y1)
    x3 = (x2 - x1) + x2
    y3 = (y2 - y1) + y2
    coordinates = [[x0, y0], [x3, y3]]
    return [coord for coord in coordinates if 0 <= coord[0] < 50 and 0 <= coord[1] < 50]

def combine_and_print(total_antinodes, antennas):
    for coord in total_antinodes:
        x, y = coord
        antennas[x][y] = "#"
    for row in antennas:
        print("".join(row))


def solution(antennas: List[List[str]]) -> int:
    total_features = {}
    total_antinodes = []
    for x in range(len(antennas)):
        for y in range(len(antennas[x])):
            if antennas[x][y] != ".":
                if antennas[x][y] not in total_features:
                    total_features[antennas[x][y]] = [[x, y]]
                else:
                    total_features[antennas[x][y]].append([x, y])
    #print(total_features)

    for feature, coordinates in total_features.items():
        print(feature)
        print(coordinates)
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):

                #additional_coordinates = find_two_coordinates_on_same_line(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                additional_coordinates = find_all_coordinates_on_same_line(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])

                for coord in additional_coordinates:
                    if coord not in total_antinodes:
                        total_antinodes.append(coord)

    #print(total_antinodes)
    combine_and_print(total_antinodes, antennas)
    
    return len(total_antinodes)

parsed_data = _parse(SAMPLE_INPUT)
#print(len(parsed_data))
#print(len(parsed_data[0]))

print(solution(parsed_data))

