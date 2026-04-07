from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[i-1] * nums[i])

        post = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            post.append(post[-1] * nums[i])
        post.reverse() # O(n)

        pre.insert(0, 1) # O(n)
        post.append(1)

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i+1])
        return res