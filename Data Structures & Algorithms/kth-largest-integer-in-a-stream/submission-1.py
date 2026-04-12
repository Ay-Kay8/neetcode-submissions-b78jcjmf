from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        copy = nums.copy()
        heapq.heapify(copy)
        for _ in range(len(nums) - k):
            heapq.heappop(copy)
        self.nums = copy

    def add(self, val: int) -> int: # O(log k)
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums) # Remove (k + 1)th value
        return self.nums[0]
