class Solution:
    # O(n! * n^2)
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):

                # What this loop does:
                # Let's say, p = [2, 3], and that nums[0] = 1
                # then res will be [[1, 2, 3], [2, 1, 3], [2, 3, 1]]

                p_copy = p.copy()
                p_copy.insert(i, nums[0]) # Inserting in the middle, O(n)
                res.append(p_copy)

        return res            