from typing import Dict, List, Optional, Tuple
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

queue: List[Tuple[str, List[str], bool]] = [("start", [], None)]
paths = 0
counted_paths = set()
while len(queue) > 0:
    node, history, double_visited = queue.pop(0)
    # print(f"Processing {node, history, double_visited}, queue remaining: {queue}")

    if node == "end":
        # print(f"visiting end node for path {history}!")
        history_tuple = tuple(history)
        if history_tuple not in counted_paths:
            paths += 1
            counted_paths.add(history_tuple)
    else:
        # to_visit = []
        # # A -> b, A -> c
        # # b, (double: b) - b, (double: c)
        # # if not double_visited:
        # #     for m in [n for n in nodes[node] if n.islower()]:
        # if double_visited and node == double_visited[0]:
        #     print(f"We're visiting our double node {node} twice")
        #     double_visited = (node, True)

        # for n in [n for n in nodes[node] if n != "start"]:
        #     if not double_visited:
        #         if n.isupper() or (n.islower() and n not in history):
        #             to_visit.insert(0, (n, history + [node], None))
        #             for double in [n for n in nodes[node] if n.islower() and n != "end" and n != "start"]:
        #                 to_visit.insert(0, (n, history + [node], (double, False)))
        #     else:

        #         if n.isupper():
        #             to_visit.insert(0, (n, history + [node], double_visited))

        #         if n.islower():
        #             if n is double_visited[0] and double_visited[1] is False:
        #                 to_visit.insert(0, (n, history + [node], double_visited))
        #             if n not in history:
        #                 to_visit.insert(0, (n, history + [node], double_visited))

        # print(f"Appending to queue: {to_visit}")
        # queue.extend(to_visit)
        # input()
        if node.islower() and node in history:
            # print(f"Double visiting {node}")
            double_visited = True

        neighbours = {
            n
            for n in nodes[node]
            if n != "start"
            and (not double_visited or not (n.islower() and n in history))
        }
        # print(f"neighbours to visit from node {node}: {neighbours}. Double visited small cave: {double_visited}")
        for n in neighbours:
            queue.insert(0, (n, history + [node], double_visited))

print(f"Found {paths} paths")
