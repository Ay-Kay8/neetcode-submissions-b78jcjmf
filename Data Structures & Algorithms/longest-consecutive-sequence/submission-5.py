class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in s:
                # This is the start of a sequence
                curr = n
                sequence_length = 1
                while (curr + 1) in s:
                    sequence_length += 1
                    curr += 1

                longest = max(longest, sequence_length)

        return longest