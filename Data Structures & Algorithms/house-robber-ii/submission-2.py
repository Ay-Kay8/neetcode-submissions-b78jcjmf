class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber_1(left, right):
            prev2, prev1 = 0, 0
            for i in range(left, right):
                tmp = max(prev2 + nums[i], prev1)
                prev2 = prev1
                prev1 = tmp
                print(prev1)

            return prev1

        LEN = len(nums)
        return max(house_robber_1(1, LEN), house_robber_1(0, LEN - 1)) if len(nums) > 1 else nums[0]