class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # (i, i)
        visited = set()

        # k = word index
        def backtrack(i, j, k):

            if k == len(word):
                return True
        
            # Violates conditions
            if (i < 0 or j < 0 or # Left and Up bounds check
                i >= len(board) or j >= len(board[0]) or # Right and Down bounds check
                (i, j) in visited or # Path is unique check
                word[k] != board[i][j]): # Current character matches check
                return False
            
            visited.add((i, j))

            res = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i, j - 1, k + 1)
            )
        
            visited.remove((i, j))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
            