# Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True

            if (not (0 <= row < ROWS) or
                not (0 <= col < COLS) or 
                (row, col) in path or 
                board[row][col] != word[i]):
                return False

            # Only add to path if the character matches
            path.add((row, col))

            res = (
                dfs(row - 1, col, i + 1) or
                dfs(row + 1, col, i + 1) or
                dfs(row, col - 1, i + 1) or
                dfs(row, col + 1, i + 1)
                   )

            # path.pop() # can't use pop(), a set doesn't maintain the order
            path.remove((row, col))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False