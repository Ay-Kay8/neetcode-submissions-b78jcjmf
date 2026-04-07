class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curr_water = min(heights[l], heights[r]) * (r - l)
            if curr_water > max:
                max = curr_water
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return max
        