from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        mini_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in row_dict[row]
                    or board[row][col] in col_dict[col]
                    or board[row][col] in mini_dict[f"{int(row/3)}" + f"{int(col/3)}"]
                ):
                    return False
                row_dict[row].add(board[row][col])
                col_dict[col].add(board[row][col])
                mini_dict[f"{int(row/3)}" + f"{int(col/3)}"].add(board[row][col])
        return True


class Solution2:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        grid = defaultdict(set)

        for i, rows in enumerate(board):
            for j, element in enumerate(rows):
                if element == ".":
                    continue
                if (
                    element in row[i]
                    or element in col[j]
                    or element in grid[f"{int(i / 3)}{int(j / 3)}"]
                ):
                    return False
                grid[f"{int(i / 3)}{int(j / 3)}"].add(element)
                row[i].add(element)
                col[j].add(element)

        return True


test = Solution2().isValidSudoku(
    board=[
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "5", "5", ".", ".", ".", ".", "6", "."],
        ["5", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(test)
