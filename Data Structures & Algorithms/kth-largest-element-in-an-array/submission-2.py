class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] # heap of size k
        heapq.heapify(heap) # O(k)

        for n in nums[k:]:
            heapq.heappushpop(heap, n)

        return heap[0]