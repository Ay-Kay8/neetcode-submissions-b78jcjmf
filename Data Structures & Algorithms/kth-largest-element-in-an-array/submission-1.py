class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        # Heap will always be of size k
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappushpop(heap, n)   
        # Since we're always popping the smallest in the heap, we'll eventuall end up with the k largest values 
        return heap[0]