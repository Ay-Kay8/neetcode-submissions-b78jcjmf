class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l)//2
            curr_h = sum([math.ceil(p/k) for p in piles])

            if curr_h <= h:
                r = k
            elif curr_h > h:
                l = k+1
        return l