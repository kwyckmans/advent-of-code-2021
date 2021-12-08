from typing import List


def load_input(filename: str) -> List[int]:
    with open(filename, mode="r") as f:
        return [int(num) for num in f.readline().split(",")]


crabs = load_input("day7.txt")

positions = [-1 for _ in range(max(crabs))]

for i in range(len(positions)):
    distance = sum([abs(crab - i) for crab in crabs])
    positions[i] = distance

print(f"Min fuel is {min(positions)}")

positions = [-1 for _ in range(max(crabs))]


def partial_sum(n: int) -> int:
    return int((n * (n + 1)) / 2)


for i in range(len(positions)):
    distance = sum([partial_sum(abs(crab - i)) for crab in crabs])
    positions[i] = distance

print(partial_sum(3))
print(f"Min fuel is {min(positions)}")
