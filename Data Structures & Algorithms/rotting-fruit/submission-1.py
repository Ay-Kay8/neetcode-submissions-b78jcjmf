# TODO: handle edge cases (single element, single rotten etc)
# TODO: handle impossible cases


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minutes = 0
        fresh_oranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # is rotten
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        all_newly_rotten = len(queue)
        popped_within_minute = 0

        while queue:

            print(f"{popped_within_minute}/{all_newly_rotten}")
            if popped_within_minute == all_newly_rotten:
                minutes += 1
                all_newly_rotten = len(queue)
                popped_within_minute = 0

            popped_within_minute += 1
            root_row, root_col = queue.popleft()

            # up, down, left, right
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for x, y in directions:
                new_x = root_row + x
                new_y = root_col + y

                if (new_x in range(len(grid)) and # vertical bounds check
                    new_y in range(len(grid[0])) and # horizontal bounds check
                    grid[new_x][new_y] == 1 # is fresh
                    ):
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = 2 # mark as rotten so we don't visit it again (this acts like our visited set)
                    fresh_oranges -= 1 # keep track of how many fresh oranges there's left
        return minutes if fresh_oranges == 0 else -1