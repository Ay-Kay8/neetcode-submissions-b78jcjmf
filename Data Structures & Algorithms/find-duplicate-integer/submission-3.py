class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = set()
        for n in nums:
            if n in map:
                return n
            else:
                map.add(n)
