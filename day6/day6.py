import functools
from typing import List, Tuple
import math
from functools import lru_cache


def load_input(filename: str) -> List[int]:
    with open(filename, mode="r") as f:
        return [int(num) for num in f.readline().split(",")]


starting_pop = load_input("day6.txt")
print(f"Starting pop: {starting_pop}")


def process_day(fishes):
    result = []
    old = []
    for i in range(len(fishes)):
        updated_fish = fishes[i] - 1

        if updated_fish != -1:
            old.append(updated_fish)
        else:
            result.append([6, 8])

    result.append(old)
    return result


@functools.cache
def no_of_fish(fishes: Tuple, days: int):
    if days == 0:
        return len(fishes)

    fishes = process_day(fishes)
    sum = 0
    for fish in fishes:
        sum += no_of_fish(tuple(fish), days - 1)

    return sum


print(no_of_fish(tuple(starting_pop), 256))
