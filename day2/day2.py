from typing import List, NamedTuple
from dataclasses import dataclass

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

with open("input.txt", mode="r") as f:
    instructions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in f.readlines()]

print(f"Read {len(instructions)} measurements")

def calculate_position(instructions) -> List[int]:
    position = [0, 0]

    for instruction in instructions:
        match instruction[0]:
            case "forward": position[0] = position[0] + instruction[1]
            case "down": position[1] = position[1] + instruction[1]
            case "up": position[1] = position[1] - instruction[1]
            case _: raise ValueError("Unkown command")

    return position

position = calculate_position(instructions)
print(f"The answer for day 2 - 1 is {position[0] * position[1]}")

@dataclass
class Position:
    x: int = 0
    y: int = 0

def calculate_position_with_aim(instructions) -> List[int]:
    position = Position()
    aim = 0

    for instruction in instructions:
        command, value = instruction
        match command:
            case "forward":
                position.x = position.x + value
                position.y = position.y + value * aim if aim > 0 else position.y
            case "down": aim = aim + value
            case "up": aim = aim - value
            case _: raise ValueError("Unkown command")

    return position

position = calculate_position_with_aim(instructions)
print(f"Your position is {position}, this makes the answer {position.x * position.y}")
