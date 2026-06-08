class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # [(row, col)]
        nb_islands = 0

        def bfs(root_row, root_col):
            queue = deque([(root_row, root_col)])

            while queue:
                row, col = queue.popleft()
                # up, down, left, right
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                # x and y are the increment in a direction
                for x, y in directions:
                    new_x = row + x
                    new_y = col + y
                    # check bounds
                    if (new_x in range(len(grid)) and
                       new_y in range(len(grid[0])) and
                       grid[new_x][new_y] == "1" and
                       (new_x, new_y) not in visited):

                       visited.add((new_x, new_y))
                       queue.append((new_x, new_y))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # bfs will propagate to all neighboring nodes and mark
                # the entirety of the island as visited
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    nb_islands += 1

        return nb_islands
