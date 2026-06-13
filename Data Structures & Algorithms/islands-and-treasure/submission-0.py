class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque() # (i, j, tiles away from treasure)
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        while queue:
            root_x, root_y, val = queue.popleft()

            # up, down, left, right
            dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for x, y in dir:
                new_x = root_x + x
                new_y = root_y + y
                if (new_x in range(len(grid)) and # vertical bounds check
                    new_y in range(len(grid[0])) and # horizontal bounds check
                    (new_x, new_y) not in visited and # not visited
                    grid[new_x][new_y] != -1 # not water
                    ):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, val + 1))
                    grid[new_x][new_y] = val + 1
