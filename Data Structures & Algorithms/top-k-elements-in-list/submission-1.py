from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = [] # Size k

        for n in nums: # O(n)
            freq[n] += 1

        for a, b in freq.items(): # O(m log k)
            heapq.heappush(heap, (b, a))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [b for a, b in heap]