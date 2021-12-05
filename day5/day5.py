from typing import List, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    start: Point
    end: Point

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_diagonal(self) -> bool:
        return self.start.y != self.end.y and self.start.x != self.end.x


def load_input(filename: str) -> Line:
    with open(filename, mode="r") as f:
        lines = f.readlines()

        for line in lines:
            raw_start, raw_end = tuple(map(lambda p: p.strip(), line.split(" -> ")))
            x_start, y_start = tuple(int(coord) for coord in raw_start.split(","))
            x_end, y_end = tuple(int(coord) for coord in raw_end.split(","))
            yield Line(Point(x_start, y_start), Point(x_end, y_end))


grid = [[0 for _ in range(999)] for _ in range(999)]


def mark_line(grid: List[List[int]], line: Line):
    """
    Mark all points on in a line on a grid.
    """

    if line.is_diagonal():
        if line.start.y < line.end.y:
            y_diff = 1
            y_start = line.start.y
            y_end = line.end.y + 1
        else:
            y_diff = -1
            y_start = line.start.y
            y_end = line.end.y - 1

        if line.start.x < line.end.x:
            x_diff = 1
        else:
            x_diff = -1

        # print(f"Marking from {x_start, y_start} to {x_end, y_end}")

        x = line.start.x

        for y in range(y_start, y_end, y_diff):
            grid[y][x] += 1
            x += x_diff

    elif line.is_vertical():
        # print(f"Marking y values from {line.start.y} to {line.end.y} at {line.start.x}")
        if line.start.y > line.end.y:
            for y in range(line.end.y, line.start.y + 1):
                grid[y][line.start.x] += 1
        else:
            for y in range(line.start.y, line.end.y + 1):
                grid[y][line.start.x] += 1

    elif line.is_horizontal():
        # print(f"old: {line.start.y}, {line.end.y}. New: {line.is_vertical()}")
        if line.start.x > line.end.x:
            for x in range(line.end.x, line.start.x + 1):
                grid[line.start.y][x] += 1
        else:
            for x in range(line.start.x, line.end.x + 1):
                grid[line.start.y][x] += 1


def count_overlaps(grid: List[List[int]]) -> int:
    return sum(map(lambda row: sum(map(lambda n: n > 1, row)), grid))


def count_non_diagonal_overlaps() -> int:
    for line in load_input("day5.txt"):
        if line.start.x == line.end.x or line.start.y == line.end.y:
            mark_line(grid=grid, line=line)

    return count_overlaps(grid)


print(count_non_diagonal_overlaps())

grid = [[0 for _ in range(999)] for _ in range(999)]


def count_all_overlaps() -> int:
    for line in load_input("day5.txt"):
        mark_line(grid=grid, line=line)

    return count_overlaps(grid)


print(count_all_overlaps())
