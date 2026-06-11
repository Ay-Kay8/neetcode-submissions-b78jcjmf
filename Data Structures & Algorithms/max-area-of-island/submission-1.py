class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def bfs(root_row, root_col) -> int:
            queue = deque([(root_row, root_col)])
            visited.add((root_row, root_col))
            area = 1

            # up, down, left, right
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while queue:
                row, col = queue.popleft()

                for x, y in dirs:
                    new_x = row + x
                    new_y = col + y

                    if (new_x in range(len(grid)) and
                        new_y in range(len(grid[0])) and
                        grid[new_x][new_y] != 0 and
                        (new_x, new_y) not in visited):
                            area += 1
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y))
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0 and (row, col) not in visited:
                    area = bfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area