class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        addends = []

        def dfs(curr, total):
            if total > target:
                return
            elif total == target:
                res.append(addends.copy())
                return

            for i in range(curr, len(nums)):
                addends.append(nums[i])
                dfs(i, total + nums[i])
                addends.pop()

        dfs(0, 0)
        return res