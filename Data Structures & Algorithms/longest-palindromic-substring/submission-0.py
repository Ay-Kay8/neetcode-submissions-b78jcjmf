class Solution:
    def longestPalindrome(self, s: str) -> str:

        # range, left, right
        longest_range = (0, 0, 0)

        def longest(l, r):
            nonlocal longest_range
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    longest_range = max(longest_range, (r - l, l, r))
                    l -= 1
                    r += 1
                else:
                    break
        for i in range(len(s)):
            longest(i, i + 1)
            longest(i - 1, i + 1)

        return s[longest_range[1]:longest_range[2] + 1]