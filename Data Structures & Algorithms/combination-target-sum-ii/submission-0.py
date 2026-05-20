class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or curr_sum > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            subset.pop()

            # 1, 2, 2, 4, 6 ...
            #    ^  ^
            #    i next_i
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1

            dfs(next_i, curr_sum)

        candidates.sort()
        dfs(0, 0)
        return res

            