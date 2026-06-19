# 1. Go through the whole 2D array, add all SAFE nodes to not_surrounded queue
#    Also add all of them to letter_os
# 2. BFS through queue, marking all the ones connected to the edge as True in letter_os
# 3. Go through letter_os, marking all True as "X"

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        not_surrounded = deque()
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # O(n * m)
        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    for dr, dc in dir:
                        new_r = i + dr
                        new_c = j + dc

                        # if this is out of bounds
                        if new_r not in range(ROWS) or new_c not in range(COLS):
                            not_surrounded.append((i, j))

        # O(n * m)
        while not_surrounded:
            # this node is not surrounded
            root_row, root_col = not_surrounded.popleft()
            board[root_row][root_col] = "S" # this node is not surrounded, this acts as our "visited" set (saving some memory)

            for dr, dc in dir:
                new_r = root_row + dr
                new_c = root_col + dc

                if (new_r in range(ROWS) and
                    new_c in range(COLS) and
                    board[new_r][new_c] == "O"):
                    board[new_r][new_c] = "S" # mark it safe as soon as it is visited
                    not_surrounded.append((new_r, new_c))

        # O(n * m)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"