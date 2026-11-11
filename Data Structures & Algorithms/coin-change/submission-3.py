class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        # returns the shortest length from i to the end
        def dfs(i):

            if i > amount:
                return float('inf')

            if i == amount:
                return 0

            if i in memo:
                return memo[i]

            # fix this
            shortest = float('inf')
            for n in coins:
                shortest = min(shortest, dfs(i + n) + 1)
            memo[i] = shortest
            return shortest

        x = dfs(0)
        return x if x != float('inf') else -1