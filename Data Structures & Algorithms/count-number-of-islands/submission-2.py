from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (x, y)
        num_islands = 0

        ROWS = len(grid)
        COLS = len(grid[0])


        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            while queue:

                start_x, start_y = queue.popleft()
                # left, right, down, up
                dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in dir:
                    x = start_x + dx
                    y = start_y + dy
                    if (0 <= x < ROWS and # horizontal bounds check
                        0 <= y < COLS and # vertical bounds check
                        grid[x][y] == "1" and
                        (x, y) not in visited):

                        visited.add((x, y))
                        queue.append((x, y))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_islands += 1
                    bfs(i, j)

        return num_islands