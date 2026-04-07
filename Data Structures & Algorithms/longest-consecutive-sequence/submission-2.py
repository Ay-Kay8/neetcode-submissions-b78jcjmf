class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        startOfSequence = {}

        for n in s:
            if n - 1 not in s:
                startOfSequence[n] = 1

        for n in startOfSequence:
            for i in range(len(nums)):
                if n + i + 1 not in s:
                    break
                startOfSequence[n] += 1

        return max(startOfSequence.values(), default=0)
        