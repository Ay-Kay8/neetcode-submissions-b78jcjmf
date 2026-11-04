class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def find_pal(i, j):
            nonlocal count
            while 0 <= i and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

        for i in range(len(s)):
            count += 1
            find_pal(i - 1, i + 1)
            find_pal(i, i + 1)

        return count