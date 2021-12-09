from typing import Dict, List, Tuple
import math
from collections import defaultdict


def load_input(filename: str) -> Dict[int, Dict[int, int]]:
    data = defaultdict(dict)
    with open(filename, mode="r") as f:
        for i, row in enumerate(f.readlines()):
            for j, col in enumerate([int(col) for col in row.strip()]):
                data[i][j] = col

    return data


grid = load_input("day9.txt")
low_points = []


def lower_than_adjecents(grid: Dict[int, Dict[int, int]], row: int, col: int) -> bool:
    print(f"Checking adjecents for {row}, {col}")
    if col - 1 in grid[row] and grid[row][col - 1] <= grid[row][col]:
        return False

    if col + 1 in grid[row] and grid[row][col + 1] <= grid[row][col]:
        return False

    if row + 1 in grid and grid[row + 1][col] <= grid[row][col]:
        return False

    if row - 1 in grid and grid[row - 1][col] <= grid[row][col]:
        return False

    return True


total = 0
# (row, col)
low_points: List[Tuple[int, int]] = []
for row in grid:
    for col in grid[row]:
        if lower_than_adjecents(grid, row, col):
            low_points.append((row, col))
            print(f"{grid[row][col]} is lower than adjacents")
            risk_level = 1 + grid[row][col]
            total += risk_level

print(f"Part 1: {total}, low points: {low_points}")

basins = []
visited_coords = set()


def get_adjacent_coordinates(
    grid: Dict[int, Dict[int, int]], row: int, col: int
) -> bool:
    print(f"Checking adjecents for {row}, {col}")
    if (
        col - 1 in grid[row]
        and grid[row][col - 1] != 9
        and (row, col - 1) not in visited_coords
    ):
        yield (row, col - 1)

    if (
        col + 1 in grid[row]
        and grid[row][col + 1] != 9
        and (row, col + 1) not in visited_coords
    ):
        yield (row, col + 1)

    if (
        row + 1 in grid
        and grid[row + 1][col] != 9
        and (row + 1, col) not in visited_coords
    ):
        yield (row + 1, col)

    if (
        row - 1 in grid
        and grid[row - 1][col] != 9
        and (row - 1, col) not in visited_coords
    ):
        yield (row - 1, col)


for low_point in low_points:
    basin = []
    print(f"Finding basin for {low_point}")
    queue = [low_point]
    visited_coords.add(low_point)

    while len(queue) > 0:
        point = queue.pop(0)
        basin.append(point)
        for neighbor in get_adjacent_coordinates(grid, row=point[0], col=point[1]):
            queue.append(neighbor)
            visited_coords.add(neighbor)

    print(f"Found basin {basin}")
    basins.append(basin)

basins.sort(key=lambda l: len(l), reverse=True)
print(f"Prodct of largest basins: {math.prod((map(lambda b: len(b),basins[0:3])))}")
