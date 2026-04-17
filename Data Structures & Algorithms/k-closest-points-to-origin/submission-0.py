import math
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # list of tuples (dist [x, y])
        l = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(l)

        closests = []
        for i in range(k):
            closests.append(heapq.heappop(l)[1])

        return closests