"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

0 -> 6 segments
1 -> 2 segments
2 -> 5 segments
3 -> 5 segments
4 -> 4 segments
5 -> 5 segments
6 -> 6 segments
7 -> 3 segments
8 -> 7 segments
9 -> 6 segments

=> 1, 4, 7 and 8 use unique segments, so an input of 2 characters can only be a 1
"""

from typing import List, Tuple


def load_input(filename: str) -> List[Tuple[List[str], List[str]]]:
    data = []
    with open(filename, mode="r") as f:
        for row in f.readlines():
            patterns = row.split("|")[0]
            outputs = row.split("|")[1]

            data.append(
                (
                    [pattern for pattern in patterns.strip().split(" ")],
                    [output for output in outputs.strip().split(" ")],
                )
            )

    return data


inputs = load_input("day8.txt")

nr_of_easy_nrs = 0
for inp in inputs:
    # temp = sum(map(lambda out: len(out) in {2, 4, 3, 7}, inp[1]))
    # print(f"number of easy numbers in output {inp[1]}: {temp}")
    nr_of_easy_nrs += sum(map(lambda out: len(out) in {2, 4, 3, 7}, inp[1]))

print(nr_of_easy_nrs)
