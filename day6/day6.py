import functools
from typing import List, Tuple
import math
from functools import lru_cache


def load_input(filename: str) -> List[int]:
    with open(filename, mode="r") as f:
        return [int(num) for num in f.readline().split(",")]


# def no_of_fish_after(starting_pop: List[int], days: int, period:int=7) -> int:
#     print(list(map(lambda fish: math.ceil(abs(fish - days)/period), starting_pop)))
#     return None


starting_pop = load_input("day6.txt")
print(f"Starting pop: {starting_pop}")
# print(no_of_fish_after(starting_pop=starting_pop, days=18))

# def process_day(fishes: List[int]) -> List[int]:
#     result = []
#     for i in range(len(fishes)):
#         updated_fish = fishes[i] - 1

#         if updated_fish == -1:
#             result.append(6)
#             result.append(8)
#         else:
#             result.append(updated_fish)

#     return result


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
    # print(fishes, days)
    if days == 0:
        # print(f"Days = 0, returning {len(fishes)}")
        return len(fishes)

    fishes = process_day(fishes)
    # print(fishes)
    sum = 0
    for fish in fishes:
        sum += no_of_fish(tuple(fish), days - 1)

    return sum
    # print(f"day {day + 1}. A total amount of {len(fishes)} fishes")


print(no_of_fish(tuple(starting_pop), 256))
