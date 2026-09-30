import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x, y)

            new_weight = x - y
            if new_weight == 0:
                continue

            heapq.heappush(stones, -abs(new_weight))

        return 0 if len(stones) == 0 else -stones[0]