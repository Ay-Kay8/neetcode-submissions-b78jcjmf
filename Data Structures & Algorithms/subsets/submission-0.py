class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # Base case: we reach a leaf
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # Don't pick nums[i] (go left)
            dfs(i + 1) # Ok let's move on and do nothing

            # Pick nums[i] (go right), we need to do 3 things
            subset.append(nums[i]) # 1. Pick it
            dfs(i + 1) # 2. Move on
            subset.pop() # #. Backtrack
        
        dfs(0)
        return res

        