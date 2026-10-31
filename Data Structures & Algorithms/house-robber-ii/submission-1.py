class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber_1(sub_nums):
            prev2, prev1 = 0, 0
            for i in range(len(sub_nums)):
                tmp = max(prev2 + sub_nums[i], prev1)
                prev2 = prev1
                prev1 = tmp

            return prev1

        return max(house_robber_1(nums[1:]), house_robber_1(nums[:-1])) if len(nums) > 1 else nums[0]