from typing import List


def load_input(filename: str) -> List[str]:
    with open(filename, mode="r") as f:
        return [s.strip() for s in f.readlines()]


lines = load_input("day10.txt")
# print(lines)

start_tokens = {"(", "[", "{", "<"}
stop_tokens = {")", "]", "}", ">"}

tokens = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

autocomplete_score = {")": 1, "]": 2, "}": 3, ">": 4}

score = 0
auto_scores: List[int] = []
filtered_lines: List[str] = []

for line in lines:
    stack: List[str] = []
    auto_score = 0
    corrupted = False
    for token in line:
        if token in tokens:
            stack.append(token)
        else:
            start_token = stack.pop()
            if token != tokens[start_token]:
                score += points[token]
                corrupted = True
                break

    if not corrupted:
        # filtered_lines.append(line)
        while not len(stack) == 0:
            token = stack.pop()
            auto_score = auto_score * 5 + autocomplete_score[tokens[token]]

        auto_scores.append(auto_score)

print(f"Part 1: score is {score}")
auto_scores.sort()
print(auto_scores[int(len(auto_scores) / 2)])
