from typing import Dict, List, Tuple
from collections import defaultdict


def load_input(filename: str) -> Dict[str, List[str]]:
    data: Dict[str, List[str]] = defaultdict(list)
    with open(filename, mode="r") as f:
        for row in f.readlines():
            begin, end = row.strip().split("-")
            # data.
            data[begin].append(end)
            data[end].append(begin)

    return data


nodes = load_input("day12.txt")

for node in nodes:
    print(f"from {node} to {nodes[node]}")

queue: List[Tuple[str, List[str]]] = [("start", [])]
paths = 0

while len(queue) > 0:
    print(f"Queue remaining: {queue}")
    node, history = queue.pop(0)
    if node == "end":
        print(f"visiting end node for path {history}!")
        paths += 1
    else:
        neighbours = {
            n
            for n in nodes[node]
            if n != "start" and not (n.islower() and n in history)
        }
        print(f"neighbours to visit from node {node}: {neighbours}")
        for n in neighbours:
            queue.insert(0, (n, history + [node]))

print(f"Found {paths} paths")
