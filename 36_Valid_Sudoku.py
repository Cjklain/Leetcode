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
# print(test)


class Solution3:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        data = defaultdict(list)
        col_data = defaultdict(list)
        row_data = defaultdict(list)

        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == ".":
                    continue
                if el in col_data[i] or el in row_data[j]:
                    return False
                else:
                    col_data[i].append(el)
                    row_data[j].append(el)
                if el in data[f"{i//3}{j//3}"]:
                    return False
                else:
                    data[f"{i//3}{j//3}"].append(el)

        return True


test3 = Solution3().isValidSudoku(
    board=[
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
)
# print(test3)


class Solution4:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_collection = defaultdict(set)
        col_collection = defaultdict(set)
        square_collection = defaultdict(set)

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in row_collection[i]
                    or board[i][j] in col_collection[j]
                    or board[i][j] in square_collection[f"{i//3}{j//3}"]
                ):
                    return False
                else:
                    row_collection[i].add(board[i][j])
                    col_collection[j].add(board[i][j])
                    square_collection[f"{i//3}{j//3}"].add(board[i][j])
        return True


test4 = Solution4().isValidSudoku(
    board=[
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "2", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(test4)
