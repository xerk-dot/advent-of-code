from aoc import get_input

def word_search_partA(board_str: str, words: list) -> dict:
    # Convert the input string into a 2D list (board)
    board = [list(row) for row in board_str.strip().split('\n')]
    rows, cols = len(board), len(board[0]) if board else 0
    found_words = {}

    # Directions: right, down, diagonal down-right, left, up, diagonal up-left
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)   # diagonal up-right
    ]

    def search_word(word):
        positions = []
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    if check_word(word, r, c, dr, dc):
                        positions.append((r, c))  # Add the starting position to the list
        return positions

    def check_word(word, start_row, start_col, dr, dc):
        for i in range(len(word)):
            r, c = start_row + i * dr, start_col + i * dc
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
        return True

    for word in words:
        positions = search_word(word)
        found_words[word] = positions

    return found_words

def word_search_partB(board_str: str) -> dict:
    # Convert the input string into a 2D list (board)
    board = [list(row) for row in board_str.strip().split('\n')]
    rows, cols = len(board), len(board[0]) if board else 0

    def search_word():
        positions = []
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if check_word(r, c):
                    positions.append((r, c))  # Add the starting position to the list
        return positions

    def check_word(start_row, start_col):
        # Check if the word "MAS" is spelled on both diagonals
        # Assuming the diagonals are from top-left to bottom-right and top-right to bottom-left
        # M is on the opposite side of S on both diagonals
        diagonal1 = [board[start_row - 1][start_col - 1], board[start_row][start_col], board[start_row + 1][start_col + 1]]
        diagonal2 = [board[start_row + 1][start_col - 1], board[start_row][start_col], board[start_row - 1][start_col + 1]]
        configurations = [['M', 'A', 'S'], ['S', 'A', 'M']]
        return any(diagonal1 == config for config in configurations) and any(diagonal2 == config for config in configurations)

    return search_word()

resulta = word_search_partA(get_input(4), ["XMAS"])
resultb = word_search_partB(get_input(4))
print(f"XMAS has {len(resulta['XMAS'])} items")
print(f"X-MAS has {len(resultb)} items")
