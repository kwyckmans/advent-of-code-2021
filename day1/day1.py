from typing import List

test_input = """199
200
208
210
200
207
240
269
260
263"""

with open("input.txt", mode="r") as f:
    measurements = [int(line) for line in f.readlines()]

print(f"Read {len(measurements)} measurements")


def calculate_nr_of_increases(measurements: List[int]) -> int:
    prev_measurement = None
    increases = 0

    for measurement in measurements:
        if prev_measurement and measurement > prev_measurement:
            increases = increases + 1

        prev_measurement = measurement

    return increases


def calculate_increases_per_sliding_window(measurements: List[int]) -> int:
    increases = 0
    prev_sum = None

    for idx in range(0, len(measurements) - 2):
        cur_sum = sum(measurements[idx : idx + 3])

        if prev_sum and cur_sum > prev_sum:
            increases = increases + 1

        prev_sum = cur_sum

    return increases


increases = calculate_nr_of_increases(measurements)
print(f"{increases} values have increased over their previous one")

increases = calculate_increases_per_sliding_window(measurements)
print(f"{increases} sliding windows have increased over their previous one")
