from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums)):
            pre.append(prod(nums[:i+1]))
        pre.append(1)

        sub = [1]
        for i in range(len(nums)):
            sub.append(prod(nums[i:]))
        sub.append(1)

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * sub[i+2])
        return res