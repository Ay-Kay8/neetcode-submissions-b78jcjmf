class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i, n in enumerate(sorted_nums):
            if i > 0 and n == sorted_nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] < 0 - n:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] > 0 - n:
                    r -= 1
                else:
                    res.append([n, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
        return res