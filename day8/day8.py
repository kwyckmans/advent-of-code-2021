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

from typing import Dict, List, Set, Tuple


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


data = load_input("day8.txt")

nr_of_easy_nrs = 0
for inp in data:
    # temp = sum(map(lambda out: len(out) in {2, 4, 3, 7}, inp[1]))
    # print(f"number of easy numbers in output {inp[1]}: {temp}")
    nr_of_easy_nrs += sum(map(lambda out: len(out) in {2, 4, 3, 7}, inp[1]))

print(f"part 1: {nr_of_easy_nrs}")

"""
    0
1       2
1       2
    3
4       5
4       5
    6
"""

# What segments belong to a number?
numbers_w_segments = {
    0: {0, 1, 2, 4, 5, 6},
    1: {2, 5},
    2: {0, 2, 3, 4, 6},
    3: {0, 2, 3, 5, 6},
    4: {1, 2, 3, 5},
    5: {0, 1, 3, 5, 6},
    6: {0, 1, 3, 4, 5, 6},
    7: {0, 2, 5},
    8: {0, 1, 2, 3, 4, 5, 6},
    9: {0, 1, 2, 3, 5, 6},
}

numbers_w_strings = {}

# Which potential characters belong to what segment?
solution = {
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set(),
}


def permutate(chars: List[Set[int]]) -> Set[int]:
    """
    Permutates a list of sets. Should return the length of the list, but also returns
    lists that are smaller because it may insert duplicates
    """
    # print(f"Permutating chars: {chars}")

    if len(chars) == 1:
        # print(f"returning {chars[0]}")
        return [{segment} for segment in chars[0]]
        # for segment in chars[0]:

    permutations = []

    # for character in chars:
    for segment in chars[0]:
        remainders = permutate(chars[1:])
        for remainder in remainders:
            # print(f"remainder: {remainder}")
            permutation = {segment}.union(remainder)
            # print(f"Generated: {permutation}")
            permutations.append(permutation)
            # print(f"Current permutations: {permutations}")
            permutation = {}

    return permutations


def update_solution_with_potential_characters(
    number: int, solution: Dict, numbers_w_segments: Dict
):
    remainder = numbers_w_strings[number]
    for key in solution:
        if key in numbers_w_segments[number]:
            print(
                f"Taking difference at index {key} between {numbers_w_strings[number]} and {solution[key]}"
            )
            remainder = remainder.difference(solution[key])

    print(f"Remainder: {remainder}")

    segments_to_update = {
        segment
        for segment in solution
        if len(solution[segment]) == 0 and segment in numbers_w_segments[number]
    }
    print(f"Segments to update: {segments_to_update}")
    for segment in segments_to_update:
        solution[segment].update(remainder)


test_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")
test_output = "cdfeb fcadb cdfeb cdbaf".split(" ")


def find_number_for_segment(inputs_of_length):
    for i in range(len(inputs_of_length)):
        char_to_segments = []

        print(f"Searching for {inputs_of_length[i]}")
        for char in inputs_of_length[i]:
            char_to_segments.append({k for k in solution if char in solution[k]})

        print(f"Potential segments for this sequence: {char_to_segments}")
        potential_numbers = [
            k
            for k in numbers_w_segments
            if len(numbers_w_segments[k]) == len(inputs_of_length[i])
        ]
        print(f"Potential numbers for this sequence: {potential_numbers}")

        permutations = permutate(char_to_segments)
        perms = [p for p in permutations if len(p) == len(inputs_of_length[i])]
        print(perms)
        number = next(x for x in numbers_w_segments if numbers_w_segments[x] in perms)
        numbers_w_strings[number] = set(inputs_of_length[i])


def process_known_entities(inp: List[str]):
    numbers_w_strings[1] = set(next(x for x in inp if len(x) == 2))
    update_solution_with_potential_characters(1, solution, numbers_w_segments)
    print(f"After processing 1: {solution}")

    # Get eafb from the example, it's the only one that can represent the no 4.
    numbers_w_strings[4] = set(next(x for x in inp if len(x) == 4))
    update_solution_with_potential_characters(4, solution, numbers_w_segments)
    numbers_w_strings[7] = set(next(x for x in inp if len(x) == 3))
    update_solution_with_potential_characters(7, solution, numbers_w_segments)
    numbers_w_strings[8] = set(next(x for x in inp if len(x) == 7))
    update_solution_with_potential_characters(8, solution, numbers_w_segments)


sum = 0
for i, o in data:
    numbers_w_strings = {}

    # Which potential characters belong to what segment?
    solution = {
        0: set(),
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
    }
    process_known_entities(i)
    print(f"Solution after known strings: {solution}")
    print(f"Strings and their numbers: {numbers_w_strings}")

    inputs_length_five = [x for x in i if len(x) == 5]
    find_number_for_segment(inputs_length_five)
    print(f"numbers and their strings, after length five: {numbers_w_strings}")

    inputs_length_six = [x for x in i if len(x) == 6]
    find_number_for_segment(inputs_length_six)
    print(f"numbers and their strings, after length six: {numbers_w_strings}")

    result = int(
        "".join(
            map(
                lambda o: str(
                    next(k for k in numbers_w_strings if numbers_w_strings[k] == set(o))
                ),
                o,
            )
        )
    )
    print(result)
    sum += result

print(sum)
