from collections import defaultdict
from typing import Dict


class Octopus:
    def __init__(self, energy_level: int) -> None:
        self.flashed = False
        self.energy_level = energy_level

    def energise(self) -> None:
        self.energy_level += 1

    def flash(self) -> None:
        self.flashed = True
        self.energy_level = 0

    def reset(self):
        self.flashed = False

    def __str__(self) -> str:
        return str(self.energy_level) + f"({'x' if self.flashed else ' '})" + "\t"


def load_input(filename: str) -> Dict[int, Dict[int, Octopus]]:
    data: Dict[int, Dict[int, Octopus]] = defaultdict(dict)
    with open(filename, mode="r") as f:
        for i, row in enumerate(f.readlines()):
            for j, col in enumerate([int(col) for col in row.strip()]):
                data[i][j] = Octopus(col)

    return data


data = load_input("day11.txt")


class Octopi:
    def __init__(self, data: Dict[int, Dict[int, Octopus]]):
        self._octopi = data
        self.flashes = 0

    def _raise_energy(self) -> None:
        for row in self._octopi:
            for col in self._octopi[row]:
                self._octopi[row][col].energise()

    def _flash(self) -> None:
        for row in self._octopi:
            for col in self._octopi[row]:
                if self._octopi[row][col].energy_level > 9:
                    self.flashes += 1
                    self._octopi[row][col].flash()
                    # print(f"after flashing {row}, {col}")
                    self._propagate(row, col)

    def _reset(self) -> None:
        for row in self._octopi:
            for col in self._octopi[row]:
                self._octopi[row][col].reset()

    def _all_zeroes(self) -> bool:
        for row in self._octopi:
            for col in self._octopi[row]:
                if self._octopi[row][col].energy_level != 0:
                    return False

        return True

    def step(self) -> bool:
        self._raise_energy()
        # print("after raising energy:")
        # print(self)
        self._flash()
        if self._all_zeroes():
            return True

        self._reset()
        return False

    def _propagate(self, row: int, col: int):
        r_min = row - 1 if row - 1 >= 0 else row
        r_max = row + 1 if row + 1 < len(self._octopi) else row

        c_min = col - 1 if col - 1 >= 0 else col
        c_max = col + 1 if col + 1 < len(self._octopi[row]) else col

        # print(f"Octopus r: {row}, c: {col} flashed, propagating to rows: {r_min, r_max}, and cols: {c_min, c_max}!")

        for r in range(r_min, r_max + 1):
            for c in range(c_min, c_max + 1):
                # print(f"For octopus {row}, {col} - Processing {r}, {c}")
                if not (r == row and c == col):
                    octopus = self._octopi[r][c]
                    if not octopus.flashed:
                        octopus.energise()
                        # print(self)
                        if octopus.energy_level > 9:
                            self._octopi[r][c].flash()
                            self.flashes += 1
                            # print(self)
                            self._propagate(r, c)

    def __str__(self) -> str:
        output: str = ""

        for row in data:
            for col in data[row]:
                output += str(data[row][col]) + "\t"

            output += "\n"

        return output


# octopi = Octopi(data)
# print(octopi)
# for step in range(100):
#     print(f"Step: {step + 1}")
#     octopi.step()
#     # print(octopi)
# print(f"A total of {octopi.flashes} flashes")

octopi = Octopi(data)
all_flashed = False
counter = 0

while not all_flashed:
    counter += 1
    all_flashed = octopi.step()
    print(octopi)

print(f"All octopi flashed at step {counter}")
