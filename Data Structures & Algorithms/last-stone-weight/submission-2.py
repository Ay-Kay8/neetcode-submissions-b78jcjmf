import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-x for x in stones]
        heapq.heapify(stones_heap)

        while len(stones_heap) > 1:
            stone1 = heapq.heappop(stones_heap)
            stone2 = heapq.heappop(stones_heap)

            new_stone_weight = stone1 - stone2
            if new_stone_weight < 0:
                heapq.heappush(stones_heap, new_stone_weight)

        return -stones_heap[0] if stones_heap else 0

        