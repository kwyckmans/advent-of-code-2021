from typing import List, Tuple, final


class Board:
    def __init__(self):
        self._board: List[List[int]] = []
        self._marks: List[List[bool]] = []

    def add_row(self, row: List[int]):
        print(f"Adding {row} to board")
        self._board.append(row)
        self._marks.append([False for _ in row])

    def _is_bingo(self) -> bool:
        for row in self._marks:
            if all(row):
                return True

        for i in range(0, len(self._marks[0])):
            if all([row[i] for row in self._marks]):
                return True

        return False

    def mark(self, num: int) -> bool:
        """Returns true if marking the number results in a bingo"""

        for row in range(0, len(self._board)):
            for col in range(0, len(self._board[row])):
                if self._board[row][col] == num:
                    self._marks[row][col] = True

                    if self._is_bingo():
                        return True

        return False

    def calculate_score(self) -> int:
        score = 0
        for row in range(0, len(self._board)):
            for col in range(0, len(self._board[row])):
                score += self._board[row][col] if not self._marks[row][col] else 0

        return score

    def __str__(self) -> str:
        repr = ""
        for row in range(0, len(self._board)):
            for col in range(0, len(self._board[row])):
                repr += f"{self._board[row][col]} ({'x' if self._marks[row][col] else ' '}) \t"

            repr += "\n"

        return repr


def load_input(filename: str) -> Tuple[List[int], List[Board]]:
    with open(filename, mode="r") as f:
        numbers = [int(num) for num in f.readline().split(",")]
        # There is a newline after the number input
        f.readline()

        boards = []
        line = f.readline()
        board = Board()
        while line:
            if line == "\n":
                boards.append(board)
                board = Board()
                print("newline")
            else:
                print()
                board.add_row(
                    [int(num) for num in line.strip().split(" ") if num is not ""]
                )

            line = f.readline()

        boards.append(board)

    return numbers, boards


numbers, boards = load_input("input.txt")


def find_first_winning_board(
    numbers: List[int], boards: List[Board]
) -> Tuple[int, int]:
    for num in numbers:
        for idx, board in enumerate(boards):
            bingo = board.mark(num)

            if bingo:
                print(
                    f"Found winning bingo board after calling {num}, board {idx} is the winning board:"
                )
                print(f"{board}")
                return idx, num


def find_last_winning_board(numbers: List[int], boards: List[Board]) -> Tuple[int]:
    boards_that_won = set()
    for num in numbers:
        for idx, board in enumerate(boards):
            bingo = board.mark(num)

            if bingo and idx not in boards_that_won:
                print(f"Board with idx {idx} won")
                boards_that_won.add(idx)

            if len(boards_that_won) == len(boards):
                return idx, num


winning_idx, final_no = find_first_winning_board(numbers=numbers, boards=boards)
score = boards[winning_idx].calculate_score()
print(
    f"Score of winning board: {score}, final no {final_no}, result {score * final_no}"
)

last_winning_idx, final_no = find_last_winning_board(numbers=numbers, boards=boards)
score = boards[last_winning_idx].calculate_score()
print(
    f"Score of last winning board: {score}, final no {final_no}, result {score * final_no}"
)
