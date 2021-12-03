import statistics
from typing import Callable, List
from collections import Counter


def get_nth_col(n: int, list: List[str]) -> List[str]:
    return [row[n] for row in list]


with open("input.txt", mode="r") as f:
    diagnostics = [line.strip("\n") for line in f.readlines()]

print(f"Read {len(diagnostics)} measurements")

gamma_bits = b"00000"
epsilon_bits = b"00000"

for n in range(0, len(diagnostics[0])):
    col = get_nth_col(n, diagnostics)

    # See https://www.reddit.com/r/learnpython/comments/5wsjra/why_does_maxsetl_keylcount_generate_the_mode_of_a/
    most_common_bit = bytearray(statistics.mode(col), "utf-8")

    epsilon_bits += b"0" if most_common_bit == b"1" else b"1"
    gamma_bits += most_common_bit

gamma = int(gamma_bits, 2)
epsilon = int(epsilon_bits, 2)
print(f"Solution for day 3, part 1: {gamma * epsilon}")


def get_max_value(list: List[str]) -> str:
    collection = Counter(list)
    commonalities = collection.most_common(2)

    if commonalities[0][1] == commonalities[1][1]:
        return "1"
    else:
        return commonalities[0][0]


def get_min_value(list: List[str]) -> str:
    collection = Counter(list)
    commonalities = collection.most_common(2)

    if commonalities[0][1] == commonalities[1][1]:
        return "0"
    else:
        return commonalities[1][0]


def filter_values(
    values: List[str], n: int, filter_fn: Callable[[List[str]], str] = get_max_value
) -> List[str]:
    col = get_nth_col(n, values)

    # Need to use a custom filter function to handle the case where there are multiple values with the same count.
    most_common_bit = filter_fn(col)

    return [row for row in values if row[n] == most_common_bit]


def get_rating(
    diagnostics: List[str], filter_fn: Callable[[List[str]], str] = get_max_value
) -> int:
    filtered_diagnostics = diagnostics
    for i in range(0, len(diagnostics[0])):
        filtered_diagnostics = filter_values(
            filtered_diagnostics, i, filter_fn=filter_fn
        )
        print(f"Filtered diagnostics: {filtered_diagnostics}")
        if len(filtered_diagnostics) is 1:
            return int(filtered_diagnostics[0], 2)

    print(f"Reached end of oxygen rating, have {len(filtered_diagnostics)} values left")
    return int(filtered_diagnostics[0], 2)


oxygen_rating = get_rating(diagnostics)
print(f"oxygen rating is {oxygen_rating}")
co_scrubber_rating = get_rating(diagnostics, filter_fn=get_min_value)
print(f"scrubber rating is {co_scrubber_rating}")
print(f"Solution for day 3, part 2: {oxygen_rating * co_scrubber_rating}")
