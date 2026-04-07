class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reps = {}
        for num in nums:
            if num in reps:
                return True
            else:
                reps[num] = 1
        return False