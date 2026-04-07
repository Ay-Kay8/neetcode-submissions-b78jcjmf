class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                n = board[i][j]
                if n.isnumeric() and n in seen:
                    return False
                elif n.isnumeric():
                    seen.add(n)
        
        # Columns
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                n = board[j][i]
                if n.isnumeric() and n in seen:
                    return False
                elif n.isnumeric():
                    seen.add(n)

        # Squares
        dict = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                d = dict[i//3, j//3]
                n = board[i][j]
                if n.isnumeric():
                    if n in d:
                        return False
                    else:
                        d.add(n)

        return True 