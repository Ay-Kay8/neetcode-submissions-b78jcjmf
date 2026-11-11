class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        # represents # of ways onwards
        def dfs(i):

            if i == len(s):
                return 1
            if i > len(s):
                return 0

            if i in memo:
                return memo[i]

            ways = 0
            # Pick 1
            if s[i] != '0':
                ways += dfs(i + 1)

            # Pick 2
            if i < len(s) - 1 and 10 <= int(s[i] + s[i + 1]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)