import sys
from aoc import get_input
from typing import List
def parse(data: str) -> List[List[str]]:
    return [list(row) for row in data.split('\n')]



import itertools
import sys

memo: list[list[bool]] = None


def get_travel(
    grid: list[str],
    origin: tuple[int, int],
    d: tuple[int, int],
    obj: tuple[int, int],
) -> bool:

    n, m = len(grid), len(grid[0])
    visited = [[set() for _ in range(m)] for _ in range(n)]
    extra_visited = []
    r, c = origin
    dr, dc = d
    while (dr, dc) not in visited[r][c]:
        visited[r][c].add((dr, dc))
        nr, nc = r + dr, c + dc
        if (nr in (-1, n) or nc in (-1, m)) and (nr, nc) != obj:
            extra_visited.append((nr, nc))
            break

        if (nr, nc) == obj or grid[nr][nc] == "#":
            dr, dc = dc, -dr

        else:
            r, c = nr, nc

    return 0 <= nr < n and 0 <= nc < m, visited, extra_visited


def part2() -> None:
    grid = parse(get_input(6))
    n, m = len(grid), len(grid[0])
    r, c = 0, 0
    while grid[r][c] != "^":
        c += 1
        if c == m:
            r += 1
            c = 0

    # (-1, 0) because it starts facing up ; (-1, -1) is for no initial obstacle
    _, travel, extra_steps = get_travel(grid, (r, c), (-1, 0), (-1, -1))
    print(
        sum(
            get_travel(grid, (r, c), (-1, 0), (i, j))[0]
            for i, j in itertools.product(range(n), range(m))
            if len(travel[i][j]) > 0 and (i, j) != (r, c)
        )  # normal positions
        + sum(get_travel(grid, (r, c), (-1, 0), pos)[0] for pos in extra_steps),  # border positions
    )

def main() -> None:
    grid = parse(get_input(6))
    n, m = len(grid), len(grid[0])
    r, c = 0, 0
    while grid[r][c] != "^":
        c += 1
        if c == m:
            r += 1
            c = 0

    visited = [[set() for _ in range(m)] for _ in range(n)]
    dr, dc = -1, 0
    while (dr, dc) not in visited[r][c]:
        visited[r][c].add((dr, dc))
        nr, nc = r + dr, c + dc
        if nr in (-1, n) or nc in (-1, m):
            break

        if grid[nr][nc] == "#":
            dr, dc = dc, -dr

        else:
            r, c = nr, nc

    print(sum(len(visited[i][j]) > 0 for i in range(n) for j in range(m)))


if __name__ == "__main__":
    main()
    part2()