
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curr_min, curr_max = 1, 1
        for n in nums:
            # tmp for curr_max
            tmp = max(n, curr_max * n, curr_min * n)
            curr_min = min(n, curr_min * n, curr_max * n)
            curr_max = tmp

            res = max(res, curr_max)

        return res