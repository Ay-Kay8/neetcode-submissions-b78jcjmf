# Attempt #4
# Memoization
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            # res represents the # of decodings starting at i
            # each call gets its own "res"
            res = 0

            # 2263
            #     ^
            if i == len(s):
                return 1

            # 2263
            #      ^
            if i > len(s):
                return 0

            if i in memo:
                return memo[i]

            # Pick 1
            if s[i] != '0':
                res += dfs(i + 1)

            # Pick 2
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            memo[i] = res
            return res

        return dfs(0)