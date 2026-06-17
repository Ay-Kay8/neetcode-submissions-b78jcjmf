class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Basically, we will create 2 sets for what cells can the pacific/atlantic reach
        # then, whatever values are common means they are reachable by both

        ROWS, COLS = len(heights), len(heights[0])
        reachable_pacific = set()
        reachable_pacific.update([(0, i) for i in range(COLS)]) # add closest row
        reachable_pacific.update([(i, 0) for i in range(1, ROWS)]) # add closest column

        reachable_atlantic = set()
        reachable_atlantic.update([(ROWS - 1, i) for i in range(COLS)])
        reachable_atlantic.update([(i, COLS - 1) for i in range(ROWS)])

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(reachable):
            queue = deque(reachable)
            while queue: 
                row, col = queue.popleft()
                for dr, dc in dir:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(ROWS) and
                        new_col in range(COLS) and
                        heights[new_row][new_col] >= heights[row][col] and # you're expanding inwards, don't mess up the inequality
                        (new_row, new_col) not in reachable
                        ):
                        # new_row, new_col is reachable from row, col, but not in the set yet
                        reachable.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        # so like this, we should find all paths that reach the pacific

        bfs(reachable_pacific)
        bfs(reachable_atlantic)

        return list(reachable_pacific & reachable_atlantic)