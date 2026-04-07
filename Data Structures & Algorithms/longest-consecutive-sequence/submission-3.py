class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in s:
                i = 0
                while n + i in s:
                    i += 1
                longest = max(longest, i)
        return longest
                